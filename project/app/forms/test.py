from django import forms
from ..models import Test, Question, QuestionChoice


class TestForm(forms.ModelForm):

    class Meta:
        model = Test # models.py から Testを継承
        fields = ['title']

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # ログインユーザーを設定（もしログインしていれば）
        if hasattr(self, 'user') and self.user is not None:
            instance.userid = self.user
        else:
            instance.userid = None  # ログインしていない場合はNoneを設定

        if commit:
            instance.save()
        return instance

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question # models.py から Testを継承
        fields = ['text', 'explanation', 'correct_sequence']


class QuestionChoiceForm(forms.ModelForm):
    class Meta:
        model = QuestionChoice
        fields = ['text']