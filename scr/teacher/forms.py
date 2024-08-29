from django import forms
from .models import Teacher

class TeachFoM(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
        widgets={
            'dateNaissance':forms.DateInput(attrs={'type':'date'}),
            'genre' :forms.RadioSelect(choices=Teacher.GENDER_CHOICES),
        }