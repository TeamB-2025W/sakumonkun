from django import forms
from app.models.user_model import User


class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User # models.py から Userを参照し、継承する。
        fields = '__all__' # ('')