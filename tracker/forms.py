from django import forms

class EncodeForm(forms.Form):
    message = forms.CharField(label='Message')
