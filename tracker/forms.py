from django import forms

class EncodeForm(forms.Form):
    message = forms.CharField(label='Message')

class PurchaseForm(forms.Form):
    type = forms.CharField(label='Type', max_length=20)
    price = forms.IntegerField(label='Price')
