from django import forms
from .models import RegNewUser

class RegUserForm(forms.ModelForm):
    class Meta:
        model = RegNewUser
        fields = ('userName', 'userPass', )