from django.urls import path
from app.views import exam, tmp_views, test, question

app_name = 'app'

urlpatterns = [
    # テスト用のURL
    path('', test.home, name='home'),

    # User-related URLs
    # AllAuthの標準クラスを使用
    # 認証関連は全てaccount/urls.pyに記載

    # Test-related URLs
    path('test/create/', test.create, name='test_create'),
    path('test/creation_successful/<int:testid>/', test.creation_successful, name='creation_successful'),
    path('test/detail/<int:testid>/', test.test_detail, name='test_detail'),
    path('test/update/<int:testid>/', test.test_update, name='test_update'),
    path('test/modal/confirm_test_deletion/', test.test_delete, name='test_delete'),
    path('test/<int:testid>/results', exam.exam_result_list, name='exam_result_list'),


    # Question-related URLs
    path('question/delete/', question.question_delete, name='question_delete'),
    # path('question/update/', tmp_views.question_update, name='question_update'),


    # Choice-related URLs
    # path('choice/update/', tmp_views.choice_update, name='choice_update'),
    # path('choice/delete/', tmp_views.choice_delete, name='choice_delete'),


    # Exam-related URLs
    path('exam/<int:testid>/', exam.get_exam, name='get_exam'),  # 受験ページ
    path('exam/<int:testid>/post/', exam.post_exam, name='post_exam'),  # 回答送信
    path('exam/result/<int:examinationid>/', exam.exam_result, name='exam_result'),  # 結果ページ


]
