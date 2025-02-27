from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from app.forms.test import TestForm
from app.models import User, Test, Question, QuestionChoice


# ホーム画面（テスト一覧）
def home(request):
    test = Test.objects.all().annotate(question_count=Count('questions'))
    context = {
        'test': test
    }
    return render(request, 'app/test/index.html', context)


# テスト作成
def create(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        print(form)

        # デバッグ中のみ
        # ログインしている場合はuseridを設定
        if request.user.is_authenticated:
            form.user = request.user
        # ログインしていない場合はNone
        else:
            form.user = None
        

        if form.is_valid():

            # デバッグ中のみ
            # ***
            # ユーザーログインしてなくてもOK
            form.user = None
            # ***

            # Testを保存
            test = form.save()

            question_count = 1  # 最初の問題番号
            while True:

                # Questionの保存
                question_text = request.POST.get(f'question_text_{question_count}')
                print('question_text', question_count, question_text, request)
                if not question_text:
                    break
                correct_choice = request.POST.get(f'correct_{question_count}')
                explanation = request.POST.get(f'commentary_{question_count}')
                print('question_text', 'correct_choice', 'explanation')

                # Questionの作成
                question = Question(
                    testid=test,
                    text=question_text,
                    correct_choiceid=int(correct_choice),
                    explanation=explanation,
                )
                question.save()

                # 選択肢の保存
                for choice_number in range(1, 5):
                    choice_text = request.POST.get(f'choice_{question_count}_{choice_number}')
                    if choice_text:
                        choice = QuestionChoice(
                            questionid=question,
                            text=choice_text
                        )
                        choice.save()

                question_count += 1

            return redirect('app:creation_successful', testid=test.id)
        questions = [{}] 
    else:
        form = TestForm()
        questions = [{}]
    context = {
        'form': form,
        'questions': questions,
    }
    return render(request, 'app/test/create.html', context)


# テスト作成完了
def creation_successful(request, testid):
    test = get_object_or_404(Test, id=testid)
    print(test.id)
    context = {
        'test': test,
    }
    return render(request, 'app/test/creation_successful.html', context)


# テスト詳細
def test_detail(request, testid):
    test = get_object_or_404(Test, id=testid)
    context = {
        'test': test
    }
    return render(request, 'app/test/detail.html', context)


# テスト編集
def test_update(request, testid=None):
    test = get_object_or_404(Test, pk=testid)

    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            return redirect('app:home')
    else:
        form = TestForm(instance=test)

    context = {
        'form': form,
        'testid': testid
    }
    
    return render(request, 'app/test/update.html', context)


# テスト削除
def test_delete(request, testid):
    if request.method == 'POST':
        # testid = request.POST.get('testid')
        if testid:
            test = Test.objects.get(id=testid)
            test.delete()
            return redirect('app:home')
        
    return render(request, 'app/test/modal/confirm_test_deletion.html')


def test_delete_confirm(request):
    return render(request, 'app/test/modal/confirm_test_deletion.html')
