from django import forms

class TeacherForm(forms.Form):
   
    GENDER_CHOICES = (
        ('h','Homme'),
        ('f','Femme'),
    )
    MATIERE_CHOICES = (
        ('MATH','MATH'),
        ('PHYSIQUE','PHYSIQUE'),
        ('SVT','SVT'),
        ('FRANCAIS','FRANCAIS'),
        
    )
    Nom = forms.CharField(max_length=15)
    Prenoms = forms.CharField(max_length=50)
    Genre = forms.ChoiceField( choices=GENDER_CHOICES,widget= forms.RadioSelect)
    Date_Naissance = forms.DateField(widget=forms.DateInput)
    Matiere= forms.ChoiceField(choices=MATIERE_CHOICES)
    Telephone=forms.CharField(max_length=30)
   
