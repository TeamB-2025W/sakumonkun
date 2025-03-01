from django.shortcuts import render, redirect
from app.models import Test, Question, QuestionChoice, Examination, Answer
from app.views import crypturl


def get_exam(request, signed_testid):
    """試験画面を表示する

    Returns:
        テンプレートコンテキスト:
            model (Test): テストの基本情報
                - id: テストID
                - title: テストタイトル
            question_list (list[dict]): 問題と選択肢のリスト
                - question (Question): 問題情報（問題文、配点）
                - questionchoices (list[QuestionChoice]): 選択肢リスト
    """
    testid = crypturl.verify_exam_url(signed_testid)
    model = Test.objects.get(pk=testid)
    question_list = []
    
    for question in Question.objects.filter(testid=testid):
        questionchoices = QuestionChoice.objects.filter(questionid=question.id)
        question_list.append({
            'question': question,
            'questionchoices': list(questionchoices)
        })

    context = {
        'model': model,
        'question_list': question_list  # このキー名が重要
    }
    return render(request, 'app/exam/exam.html', context) 


def post_exam(request, testid):
    """試験の回答を保存する

    Expected POST data:
        guestname (str): 受験者名
            - input要素のname属性: "guestname"
        
        question_{id} (str): 各問題の回答
            - input要素のname属性: "question_1", "question_2", ...
              ({id}は問題のID)
            - input要素のtype属性: "radio"
            - input要素のvalue属性: 選択肢のID

    Form構造例:
        <input type="text" name="guestname" required>
        
        {% for question in question_list %}
            <input type="radio" 
                   name="question_{{ question.id }}" 
                   value="{{ choice.id }}"
                   required>
        {% endfor %}

    Returns:
        結果画面へのリダイレクト
    """
    if request.method == 'POST':
        testid = Test.objects.get(pk=testid)
        #まずはこのテストをExaminationに保存し、そのexaminationのidを取得
        examination = Examination.objects.create(
            testid=testid,
            guestname=request.POST.get('guestname')
        )

        # questionオブジェクトを直接取得
        for question in Question.objects.filter(testid=testid):
            # questionはオブジェクトなのでidにアクセス可能
            selected_sequence = request.POST.get(f'question_{question.id}')
            #   value="{{ questionchoice.id }}"   <=   question_1
            is_correct = False
            
            if selected_sequence:
                is_correct = int(selected_sequence) == question.correct_sequence
            
            Answer.objects.create(
                examinationid=examination,
                questionid=question,
                selected_sequence=selected_sequence,
                iscorrect=is_correct
            )

        return redirect('app:exam_result', signed_examinationid=crypturl.generate_exam_result_url(examination.id))


def exam_result(request, signed_examinationid):
    """試験結果画面を表示する

    Returns:
        テンプレートコンテキスト:
            model (Examination): 受験情報
                - id: 受験ID
                - guestname: 受験者名
            answer_list (list[dict]): 回答結果リスト
                - answer (Answer): 回答情報（選択肢、正誤）
                - question (Question): 問題情報
                - selected_choice_text (str): 選択された選択肢
                - correct_choice_text (str): 正解の選択肢
            correct_count (int): 正解数
            total_count (int): 問題総数
    """
    examinationid = crypturl.verify_exam_result_url(signed_examinationid)
    model = Examination.objects.get(pk=examinationid)
    answer_list = []
    for answer in Answer.objects.filter(examinationid=examinationid):
        question = answer.questionid
        selected_choice_text = QuestionChoice.objects.get(
            questionid=question,
            sequence=answer.selected_sequence
        )
        correct_choice_text = QuestionChoice.objects.get(
            questionid=question,
            sequence=question.correct_sequence
        )
        answer_list.append({
            'answer': answer,
            'question': question,
            'selected_choice_text': selected_choice_text,
            'correct_choice_text': correct_choice_text,
        })

    # 正解数を計算
    correct_count = len([answer for answer in answer_list if answer['answer'].iscorrect])
    total_count = len(answer_list)
    
    context = {
        'model': model,
        'answer_list': answer_list,
        'correct_count': correct_count,
        'total_count': total_count,
    }

    return render(request, 'app/exam/exam_result.html', context) 


def exam_result_for_admin(request, examinationid):
    """試験結果画面を表示する

    Returns:
        テンプレートコンテキスト:
            model (Examination): 受験情報
                - id: 受験ID
                - guestname: 受験者名
            answer_list (list[dict]): 回答結果リスト
                - answer (Answer): 回答情報（選択肢、正誤）
                - question (Question): 問題情報
                - selected_choice_text (str): 選択された選択肢
                - correct_choice_text (str): 正解の選択肢
            correct_count (int): 正解数
            total_count (int): 問題総数
    """
    model = Examination.objects.get(pk=examinationid)
    answer_list = []
    for answer in Answer.objects.filter(examinationid=examinationid):
        question = answer.questionid
        selected_choice_text = None
        correct_choice_text = None

        # 問題が削除されている場合のハンドリング
        if question is None:
            answer_list.append({
                'answer': answer,
                'question': {'text': '問題は削除されました'},
                'selected_choice_text': {'text': '問題が削除されたため表示できません'},
                'correct_choice_text': {'text': '問題が削除されたため表示できません'},
            })
            continue

        # 選択された回答の取得（存在しない場合はNone）
        if answer.selected_sequence:
            try:
                selected_choice_text = QuestionChoice.objects.get(
                    questionid=question,
                    sequence=answer.selected_sequence
                )
            except QuestionChoice.DoesNotExist:
                selected_choice_text = {'text': f'選択肢{answer.selected_sequence}は削除されました'}

        # 正解の選択肢の取得（存在しない場合はNone）
        try:
            correct_choice_text = QuestionChoice.objects.get(
                questionid=question,
                sequence=question.correct_sequence
            )
        except QuestionChoice.DoesNotExist:
            correct_choice_text = {'text': f'正解の選択肢（{question.correct_sequence}）は削除されました'}
        except AttributeError:  # correct_sequenceが設定されていない場合
            correct_choice_text = {'text': '正解が設定されていません'}

        answer_list.append({
            'answer': answer,
            'question': question,
            'selected_choice_text': selected_choice_text or {'text': '未回答'},
            'correct_choice_text': correct_choice_text or {'text': '正解が設定されていません'},
        })

    # 正解数を計算
    correct_count = len([answer for answer in answer_list if answer['answer'].iscorrect])
    total_count = len(answer_list)
    
    context = {
        'model': model,
        'answer_list': answer_list,
        'correct_count': correct_count,
        'total_count': total_count,
    }

    return render(request, 'app/exam/exam_result_for_admin.html', context) 


# リストは管理者画面のため、URLの暗号化は不要
def exam_result_list(request, testid):
    """特定のテストに紐づく試験結果一覧画面を表示する

    Returns:
        テンプレートコンテキスト:
            test (Test): テスト情報
            examination_list (QuerySet[Examination]): 受験情報一覧
    """
    test = Test.objects.get(pk=testid)
    examination_list = Examination.objects.filter(testid=testid)
    
    for examination in examination_list:
        examination.correct_count = examination.answer_set.filter(iscorrect=True).count()
        examination.total_count = examination.answer_set.count()
    
    context = {
        'test': test,
        'examination_list': examination_list,
    }
    
    return render(request, 'app/test/records.html', context)