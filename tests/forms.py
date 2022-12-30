from django import forms

from questions.models import Question


class TestForm(forms.Form):
    answer_one = forms.BooleanField(required=False,
                                    widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input',
                                                                      'style': 'height: 20px; width: 20px'}))
    answer_two = forms.BooleanField(required=False,
                                    widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input',
                                                                      'style': 'height: 20px; width: 20px'}))
    answer_three = forms.BooleanField(required=False,
                                      widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input',
                                                                        'style': 'height: 20px; width: 20px'}))
    answer_four = forms.BooleanField(required=False,
                                     widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input',
                                                                       'style': 'height: 20px; width: 20px'}))
    answer_five = forms.BooleanField(required=False,
                                     widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input',
                                                                       'style': 'height: 20px; width: 20px'}))
    answer_six = forms.BooleanField(required=False,
                                    widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input',
                                                                      'style': 'height: 20px; width: 20px'}))
