from django.shortcuts import render, redirect
from .forms import UserForm,UseFoM
from .models import User



# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }

    return render(request, "user/index.html",context)

def add(request):
    context={"title":"Ajouter utilisateur"}
     
    if request.method == "POST":
        print(request.POST)
        form = UseFoM(request.POST)
        context["form"] = form
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('user:index')
        else:
            return render(request,"user/add.html",context)
  
    form=UseFoM()
    context["form"] = form

    return render(request,"user/add.html",context)


def update(request, id):
    # user = get_object_or_404(User,id = id)
    user = User.objects.get(id=id)
 
    context = {
        "title":"Modifier utilisateur"
    }

    if request.method == "POST":
        form = UseFoM(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:index')
        
    form = UseFoM(instance = user)

    context["form"] = form

    return render(request,"user/add.html",context)

def delete(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('user:index')