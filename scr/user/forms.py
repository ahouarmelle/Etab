from django import forms
from .models import User
class UserForm(forms.Form):
   
    Pseudo = forms.CharField(max_length=15)
    MotDePasse = forms.CharField(max_length=50,widget=forms.PasswordInput)
   
class UseFoM(forms.ModelForm):
    class Meta:
        model = User
        fields = ["pseudo","password"]

