from django.urls import path
from app.views import user, exam
app_name = 'app'

urlpatterns = [
    # User-related URLs
    # path('user/', user_views.info, name='info'),
    # path('user/register/', user_views.register, name='register'),
    # path('user/login/', user_views.login, name='login'),
    # path('user/logout/', user_views.logout, name='logout'),
    # path('user/update/username/', user_views.username, name='username'),
    # path('user/update/password/', user_views.password, name='password'),

    # Test-related URLs

    # Question-related URLs

    # Choice-related URLs

    # Exam-related URLs
    path('exam/<int:testid>/', exam.GetExam, name='get_exam'),  # 受験ページ
    path('exam/<int:testid>/post/', exam.PostExam, name='post_exam'),  # 回答送信
    path('exam/result/<int:examinationid>/', exam.GetExamResult, name='exam_result'),  # 結果ページ

]