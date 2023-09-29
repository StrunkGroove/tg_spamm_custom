from django import forms
from .models import RequiredUserModel, UsernameModel

class RequiredUserForm(forms.ModelForm):
    class Meta:
        model = RequiredUserModel
        fields = ['name']

class UsernameForm(forms.ModelForm):
    class Meta:
        model = UsernameModel
        fields = ['phone', 'password']
