from django.shortcuts import render
from app.models import Question, QuestionChoice

# 問題削除
def question_delete(request):
    return render(request, 'app/test/modal/confirm_question_deletion.html')
