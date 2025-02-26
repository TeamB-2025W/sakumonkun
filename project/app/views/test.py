from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.http import JsonResponse
from django.utils import timezone
from app.forms.test import TestForm
from app.models import Test, Question, QuestionChoice
import json

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
    # テストIDに基づいてTestオブジェクトを取得
    test = get_object_or_404(Test, id=testid)
    
    # テストに関連する質問と選択肢を取得
    questions = test.questions.prefetch_related('choices').all()

    # **リクエストメソッドに基づいて処理を分岐**
    if request.method == 'POST':
        try:
            if 'update_question' in request.POST:  # 質問更新フォームの送信
                question_id = request.POST.get('question_id')
                question = get_object_or_404(Question, id=int(question_id))

                # 質問のテキストを更新
                question.text = request.POST.get('text', question.text)
                question.updated_at = timezone.now()

                # 正解の選択肢を更新
                correct_choice_id = request.POST.get('correct_choice')
                if correct_choice_id:
                    correct_choice = get_object_or_404(QuestionChoice, id=correct_choice_id)
                    question.correct_choice = correct_choice

                question.save()

                # 選択肢の更新
                for key, value in request.POST.items():
                    if key.startswith('choice_'):
                        choice_id = key.split('_')[1]
                        choice = get_object_or_404(QuestionChoice, id=choice_id)
                        choice.text = value
                        choice.updated_at = timezone.now()
                        choice.save()

                # Testのupdated_atを更新
                test.updated_at = timezone.now()
                test.save()

                return redirect('app:test_detail', testid=testid)
            
            # 質問削除フォームの送信かどうかを確認
            elif 'delete_question' in request.POST:
                question_id = request.POST.get('question_id')
                question = get_object_or_404(Question, id=question_id)
                
                # 関連するQuestionChoiceを削除
                question.choices.all().delete()

                # Question を削除
                question.delete()

                # Testのupdated_atを更新
                test.updated_at = timezone.now()
                test.save()
                
                # 削除成功のレスポンスを返す
                return JsonResponse({'status': 'success', 'message': '削除が完了しました。'})

        
        # 例外が発生した場合
        except Exception as e:
            # エラーメッセージを返す
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    # テンプレートに渡すコンテキスト
    context = {
        'test': test,
        'questions': questions,
    }
    
    # 'app/test/detail.html'テンプレートをレンダリングして返す
    return render(request, 'app/test/detail.html', context)


# テスト削除
def test_delete(request, testid):
    if request.method == 'POST':
        testid = request.POST.get('testid')
        if testid:
            test = Test.objects.get(id=testid)
            test.delete()
            return redirect('app:home')
        
    return render(request, 'app/test/modal/confirm_test_deletion.html')


def test_delete_confirm(request):
    return render(request, 'app/test/modal/confirm_test_deletion.html')
