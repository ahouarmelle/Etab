from django.shortcuts import render
from .forms import UserForm,UseFoM
# Create your views here.
def index(request):
    context = {
        'nom':'Kouakou',
        'prenom':'Ahou',
    }
    return render(request, "user/index.html", context)

def add(request):
    if request.method == "POST":
        print(request.POST)
        user_form = UseFoM(request.POST)
        if user_form.is_valid:
            print(user_form.cleaned_data)
            user_form.save()
  
    form=UserForm()
    context={'form':form}

    return render(request,"user/add.html",context)

def edit(request):
    context = {
        'nom':'Kouakou',
        'prenom':'Ahou',
       
    }
    return render(request,"user/edit.html",context)