from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ('h','Homme'),
        ('f','Femme'),
     )
    CLASSE_CHOICES = (
        ('terminale','terminale'),
        ('premier','premier'),
        ('second','second'),
        ('troisieme','troisieme'),
        ('quatrieme','quatrieme'),
        ('cinquieme','cinquieme'),
     )
    nom = models.CharField(max_length=15)
    prenoms = models.CharField(max_length=255)
    genre = models.CharField(max_length=20)
    matricule= models.CharField(max_length=15)
    dateNaissance = models.DateField()
    classe= models.CharField(max_length=20,choices=CLASSE_CHOICES)
    telephone=models.CharField(max_length=30)   
    ville=models.CharField(max_length=30)