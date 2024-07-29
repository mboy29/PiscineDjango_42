from django import forms

class FormInput(forms.Form):
    field_input = forms.CharField(label='Your Input', max_length=100)