from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from app.forms.test import TestForm
from app.models import User, Test, Question, QuestionChoice

"""
NOTE: 使用しなくなった関数(レンダリング専用)はコメントアウト
"""


"""
# テスト一覧
def test_list(request):
    tests = Test.objects.all()
    context = {
        'test': tests
    }
    return render(request, 'app/test/index.html', context)
"""


"""
# テスト編集
def test_update(request):
    return render(request, 'app/test/update.html')
"""


"""
# 回答履歴一覧
def test_records(request):
    return render(request, 'app/test/records.html')
"""


"""
# 問題
def question(request):
    return render(request, 'app/test_detail.html')


# 問題詳細
def question_detail(request):
    return render(request, 'app/question_detail.html')


# 問題作成
def question_create(request):
    return render(request, 'app/test/create.html')


# 問題編集
def question_update(request):
    return render(request, 'app/test/update.html')
"""


"""
# 選択肢
def choice(request):
    return render(request)


# 選択肢編集
def choice_update(request):
    return render(request)


# 選択肢削除
def choice_delete(request):
    return render(request)
"""
