from django import forms


class TestForm(forms.ModelForm):
    answer_one = forms.BooleanField(required=False,
                                    widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkbox',
                                                                      'style': 'height: 20px; width: 20px'}))
    answer_two = forms.BooleanField(required=False,
                                    widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkbox',
                                                                      'style': 'height: 20px; width: 20px'}))
    answer_three = forms.BooleanField(required=False,
                                      widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkbox',
                                                                        'style': 'height: 20px; width: 20px'}))
    answer_four = forms.BooleanField(required=False,
                                     widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkbox',
                                                                       'style': 'height: 20px; width: 20px'}))
    answer_five = forms.BooleanField(required=False,
                                     widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkbox',
                                                                       'style': 'height: 20px; width: 20px'}))
    answer_six = forms.BooleanField(required=False,
                                    widget=forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkbox',
                                                                      'style': 'height: 20px; width: 20px'}))
