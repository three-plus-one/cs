from django import forms


class UserForm(forms.Form):
    inputTel = forms.CharField(label='inputTel', max_length=12)
    inputPassword = forms.CharField(label='inputPassword', widget=forms.PasswordInput())