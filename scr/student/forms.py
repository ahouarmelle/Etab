from django import forms
from .models import Student

class EleveFoM(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets={
            'dateNaissance':forms.DateInput(attrs={'type':'date'}),
            'genre' :forms.RadioSelect(choices=Student.GENDER_CHOICES),
        }