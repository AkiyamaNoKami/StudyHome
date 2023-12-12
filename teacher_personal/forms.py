from django import forms

class GradeForm(forms.Form):
    homework_id = forms.IntegerField(widget=forms.HiddenInput())
    grade = forms.IntegerField(label='Выставить оценку', min_value=0, max_value=5)