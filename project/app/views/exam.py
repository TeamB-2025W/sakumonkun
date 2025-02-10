from django.shortcuts import render
from app.models import Test, Question, QuestionChoice

def GetExam(request, test_id):
    model = Test.objects.get(pk=test_id)
    question_list = []
    
    # 質問と選択肢を辞書型で整理
    for question in Question.objects.filter(test_id=test_id):
        choices = QuestionChoice.objects.filter(question_id=question.id)
        question_list.append({
            'question': question,
            'choices': list(choices)
        })

    context = {
        'model': model,
        'question_list': question_list
    }
    return render(request, 'app/exam.html', context) 