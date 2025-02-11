from django.urls import path
from app.views import user_views
from app.views import tmp_views

app_name = 'app'

urlpatterns = [
    # User-related URLs
    path('user/', user_views.info, name='info'),
    path('user/register/', user_views.register, name='register'),
    path('user/login/', user_views.login, name='login'),
    path('user/logout/', user_views.logout, name='logout'),
    path('user/update/username/', user_views.username, name='username'),
    path('user/update/password/', user_views.password, name='password'),
    path('', tmp_views.home, name='home'),
    path('test/create/', tmp_views.create, name='test_create'),
    path('test/create/tmp', tmp_views.creation_successful, name='creation_successful'),
    path('user/edit', tmp_views.user_edit, name='user_edit'),

    # Test-related URLs

    # Question-related URLs

    # Choice-related URLs

    # Exam-related URLs
    # path('exam/<int:testid>/', user_views.exam, name='exam'), # 受験ページ
    # path('exam/submit/<int:testid>/', user_views.exam, name='submit'), # 回答送信


    # Answer-related URLs
    # path('answer/<int:sessionid>/', user_views.answer, name='answer'),
]
