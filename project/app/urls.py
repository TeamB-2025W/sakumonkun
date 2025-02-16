from django.urls import path
from app.views import user, exam, tmp_views, user_views

app_name = 'app'

urlpatterns = [
    # テスト用のURL
    path('', tmp_views.home, name='home'),
    path('test/create/', tmp_views.create, name='test_create'),
    path('test/create/tmp', tmp_views.creation_successful, name='creation_successful'),
    path('user/edit', tmp_views.user_edit, name='user_edit'),


    # User-related URLs
    # path('user/', user_views.info, name='info'),
    # path('user/register/', user_views.register, name='register'),
    # path('user/login/', user_views.login, name='login'),
    path('user/logout/', user_views.logout, name='logout'),
    # path('user/update/username/', user_views.username, name='username'),
    # path('user/update/password/', user_views.password, name='password'),


    # Test-related URLs
    # path('', tmp_views.home, name='home'),
    # path('test/detail/<int:test_id>/', tmp_views.test_detail, name='test_detail'),
    path('test/detail/', tmp_views.test_detail, name='test_detail'),
    # path('test/create/', tmp_views.create, name='test_create'),
    # path('test/creation_successful/', tmp_views.creation_successful, name='creation_successful'),
    path('test/update/', tmp_views.test_update, name='test_update'),
    # path('test/records/<int:test_id>/', tmp_views.test_records, name='test_records'),
    path('test/records/', tmp_views.test_records, name='test_records'),
    path('test/modal/confirm_test_deletion/', tmp_views.test_delete, name='test_delete'),
    path('test/modal/confirm_ques_deletion/', tmp_views.question_delete, name='question_delete'),
    path('test/<int:testid>/results', exam.ExamResultList, name='exam_result_list'),


    # Question-related URLs
    # path('question/', tmp_views.question, name='question'),
    # path('question/detail/<int:question_id>/', tmp_views.question_detail, name='question_detail'),
    # path('question/create/', tmp_views.question_create, name='question_create'),
    # path('question/update/', tmp_views.question_update, name='question_update'),
    # path('question/delete/', tmp_views.question_delete, name='question_delete'),


    # Choice-related URLs
    # path('choice/', tmp_views.choice, name='choice'),
    # path('choice/update/', tmp_views.choice_update, name='choice_update'),
    # path('choice/delete/', tmp_views.choice_delete, name='choice_delete'),


    # Exam-related URLs
    path('exam/<int:testid>/', exam.GetExam, name='get_exam'),  # 受験ページ
    path('exam/<int:testid>/post/', exam.PostExam, name='post_exam'),  # 回答送信
    path('exam/result/<int:examinationid>/', exam.ExamResult, name='exam_result'),  # 結果ページ


]
