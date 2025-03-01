from django import forms
from ..models import Examination, Answer

class AnswerForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['examinationid'].widget = forms.HiddenInput()
        self.fields['questionid'].widget = forms.HiddenInput()
        self.fields['selected_sequence'].widget = forms.HiddenInput()

    class Meta:
        model = Answer
        fields = ['examinationid', 'questionid', 'selected_sequence']

class ExaminationForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = ['guestname']


class ResultForm(forms.Form):
    class Meta:
        model = Answer
        fields = ['iscorrect']


