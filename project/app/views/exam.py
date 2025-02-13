from django.shortcuts import render, redirect
from app.models import Test, Question, QuestionChoice, Examination, Answer
from app.forms.exam import AnswerForm


def GetExam(request, testid):
    model = Test.objects.get(pk=testid)
    question_list = []
    
    # 質問と選択肢を辞書型で整理
    for question in Question.objects.filter(testid=testid):
        choices = QuestionChoice.objects.filter(questionid=question.id)
        question_list.append({
            'question': question,
            'choices': list(choices)
        })

    context = {
        'model': model,
        'question_list': question_list
    }
    return render(request, 'app/test_view/exam.html', context) 


def PostExam(request, testid):
    if request.method == 'POST':
        test_id = Test.objects.get(pk=testid)
        #まずはこのテストをExamに保存し、そのexamのidを取得
        examination = Examination.objects.create(
            testid=test_id,
            guestname=request.POST.get('guestname')
        )
        questions = Question.objects.filter(testid=testid)
        
        for question in questions:
            # POSTデータから直接選択された選択肢IDを取得
            selected_choiceid = request.POST.get(f'question_{question.id}')
            
            if selected_choiceid:
                is_correct = (int(selected_choiceid) == question.correct_choiceid)
                
                Answer.objects.create(
                    examinationid=examination,  # ForeignKeyはオブジェクトを渡す
                    questionid=question,        # ForeignKeyはオブジェクトを渡す
                    selected_choiceid=selected_choiceid,
                    iscorrect=is_correct
                )

    return redirect('app:exam_result', examinationid=examination.id)


def GetExamResult(request, examinationid):
    model = Examination.objects.get(pk=examinationid)
    answer_list = []
    
    # 質問と選択肢を辞書型で整理
    for answer in Answer.objects.filter(examinationid=examinationid):
        question = Question.objects.get(id=answer.questionid)
        choices = QuestionChoice.objects.filter(questionid=question.id)
        answer_list.append({
            'question': question,
            'choices': list(choices),
            'is_correct': answer.iscorrect
        })

    context = {
        'model': model,
        'answer_list': answer_list
    }
    return render(request, 'app/test_view/exam_result.html', context) 