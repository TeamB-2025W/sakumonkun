from django.urls import path
from app.views import user, exam, test

app_name = 'app'

urlpatterns = [
    # テスト用のURL
    # path('', tmp_views.home, name='home'),
    # path('test/create/', tmp_views.create, name='test_create'),
    # path('test/create/tmp', tmp_views.creation_successful, name='creation_successful'),
    # path('user/edit', tmp_views.user_edit, name='user_edit'),

    # User-related URLs
    # path('user/', user_views.info, name='info'),
    # path('user/register/', user_views.register, name='register'),
    # path('user/login/', user_views.login, name='login'),
    # path('user/logout/', user_views.logout, name='logout'),
    # path('user/update/username/', user_views.username, name='username'),
    # path('user/update/password/', user_views.password, name='password'),

    # Test-related URLs
    path('', test.test_list, name='home'),
    path('test/detail/<int:test_id>/', test.test_detail, name='test_detail'),
    path('test/create/', test.test_create, name='test_create'),
    path('test/creation_successful/', test.creation_successful, name='creation_successful'),
    path('test/update/', test.test_update, name='test_update'),
    path('test/delete/', test.test_delete, name='test_delete'),
    path('test/record/<int:test_id>/', test.test_record, name='test_record'),

    # Question-related URLs
    path('question/', test.question, name='question'),
    path('question/detail/<int:question_id>/', test.question_detail, name='question_detail'),
    path('question/create/', test.question_create, name='question_create'),
    path('question/update/', test.question_update, name='question_update'),
    path('question/delete/', test.question_delete, name='question_delete'),

    # Choice-related URLs
    path('choice/', test.choice, name='choice'),
    path('choice/update/', test.choice_update, name='choice_update'),
    path('choice/delete/', test.choice_delete, name='choice_delete'),

    # Exam-related URLs
    path('exam/<int:testid>/', exam.GetExam, name='get_exam'),  # 受験ページ
    path('exam/<int:testid>/post/', exam.PostExam, name='post_exam'),  # 回答送信
    path('exam/result/<int:examinationid>/', exam.GetExamResult, name='exam_result'),  # 結果ページ

]