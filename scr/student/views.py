from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def index(request):
    context = {
        'nom':'Kouakou',
        'prenom':'Ahou',
    }
    return render(request, "student/index.html", context)

def add(request):
    form = StudentForm()
    context ={'form': form}

    return render(request,"student/add.html", context)

def edit(request):
    context = {
        'nom':'Kouakou',
        'prenom':'Ahou',
        'age':'23',
        'ville':'Dabou',
    }
    return render(request,"student/edit.html",context)
