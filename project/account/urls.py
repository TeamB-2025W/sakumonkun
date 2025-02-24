from django.urls import path
from allauth.account.views import LoginView, SignupView, LogoutView
from .views import UserProfileUpdateView, change_password

app_name = 'accounts'  # 名前空間を復活

urlpatterns = [
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('signup/', SignupView.as_view(), name='account_signup'),
    path('edit/', UserProfileUpdateView.as_view(), name='edit'),
    path('change-password/', change_password, name='change_password'),
]