from django.shortcuts import render, redirect
from app.models import Test, Question, QuestionChoice, Examination, Answer
from app.forms.exam import AnswerForm


def GetExam(request, testid):
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
    return render(request, 'app/test_view/exam.html', context) 


def PostExam(request, testid):
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
        test_id = Test.objects.get(pk=testid)
        #まずはこのテストをExaminationに保存し、そのexaminationのidを取得
        examination = Examination.objects.create(
            testid=test_id,
            guestname=request.POST.get('guestname')
        )

        # questionオブジェクトを直接取得
        for question in Question.objects.filter(testid=testid):
            # questionはオブジェクトなのでidにアクセス可能
            selected_choiceid = request.POST.get(f'question_{question.id}')
            #   value="{{ questionchoice.id }}"   <=   question_1
            is_correct = False
            
            if selected_choiceid:
                is_correct = int(selected_choiceid) == question.correct_choiceid
            
            Answer.objects.create(
                examinationid=examination,
                questionid=question,
                selected_choiceid=selected_choiceid,
                iscorrect=is_correct
            )

        return redirect('app:exam_result', examinationid=examination.id)


def GetExamResult(request, examinationid):
    """試験結果画面を表示する

    Returns:
        テンプレートコンテキスト:
            model (Examination): 受験情報
                - id: 受験ID
                - guestname: 受験者名
            answer_list (list[dict]): 回答結果リスト
                - answer (Answer): 回答情報（選択肢、正誤）
                - question (Question): 問題情報
                - questionchoice_text (str): 選択された選択肢
                - correct_choice_text (str): 正解の選択肢
            correct_count (int): 正解数
            total_count (int): 問題総数
    """
    model = Examination.objects.get(pk=examinationid)
    answer_list = []
    for answer in Answer.objects.filter(examinationid=examinationid):
        question = answer.questionid
        questionchoice_text = QuestionChoice.objects.get(id=answer.selected_choiceid)
        correct_choice_text = QuestionChoice.objects.get(id=answer.questionid.correct_choiceid)
        answer_list.append({
            'answer': answer,
            'question': question,
            'questionchoice_text': questionchoice_text,
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

    return render(request, 'app/test_view/exam_result.html', context) 


def GetExamResultList(request, testid):
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
    
    return render(request, 'app/test_view/test_results.html', context)