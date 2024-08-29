from django.db import models

# Create your models here.
class Teacher(models.Model):
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
    nom = models.CharField(max_length=15)
    prenoms = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    dateNaissance = models.DateField()
    matiere= models.CharField(max_length=20,choices=MATIERE_CHOICES)
    telephone=models.CharField(max_length=30)


    def __str__(self) :
        return self.nom   #super().__str__()
    