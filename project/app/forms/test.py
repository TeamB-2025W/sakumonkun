from django import forms
from ..models import Test


class TestForm(forms.ModelForm):

    class Meta:
        model = Test # models.py から Testを継承
        fields = '__all__'