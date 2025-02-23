from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages

from app.models import User


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'account/edit.html'
    success_url = reverse_lazy('accounts:edit')

    def get_object(self, queryset=None):
        return self.request.user


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # パスワード変更後もログイン状態を維持
            update_session_auth_hash(request, user)
            messages.success(request, 'パスワードが正常に変更されました。')
            return redirect('accounts:edit')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })