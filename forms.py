from django import forms
from .models import Userregistration


class UserRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Userregistration
        fields = ['username', 'email', 'password', 'repassword']
