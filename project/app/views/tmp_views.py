from django.shortcuts import render, redirect, get_object_or_404
from app.forms.test import TestForm
from app.models import User, Test, Question, QuestionChoice


# ホーム画面（テスト一覧）
def home(request):
    return render(request, 'app/test/index.html')


# テスト作成
def create(request):
    return render(request, 'app/test/create.html')


# テスト作成完了
def creation_successful(request):
    return render(request, 'app/test/creation_successful.html')


# ユーザー情報編集
def user_edit(request):
    return render(request, 'app/user/edit.html')

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
# テスト詳細
def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    questions = test.questions.all()
    context = {
        'test': test, 'questions':questions
    }
    return render(request, 'app/test/detail.html', context)
"""

# テスト詳細
def test_detail(request):
    return render(request, 'app/test/detail.html')


"""
# テスト作成
def test_create(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:creation_successful')
    else:
        form = TestForm()
    context = {
        'form': form,
    }
    return render(request, 'app/test/create.html', context)
"""

"""
# テスト作成完了
def creation_successful(request):
    return render(request, 'app/test/creation_successful.html')
"""

"""
# テスト編集
def test_update(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app/test.html')
    else:
        form = TestForm(instance=test)
    context = {
        'form': form, 'test': test
    }
    return render(request, 'app/test/update.html', context)
"""


# テスト編集
def test_update(request):
    return render(request, 'app/test/update.html')


# テスト削除
def test_delete(request):
    return render(request, 'app/test/modal/confirm_test_deletion.html')


# 回答履歴一覧
def test_records(request):
    return render(request, 'app/test/records.html')


# 問題削除
def question_delete(request):
    return render(request, 'app/test/modal/confirm_question_deletion.html')


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
