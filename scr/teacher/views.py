from django.shortcuts import render, redirect
from .forms import TeachFoM
from .models import Teacher
# Create your views here.

def index(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
        }
    
    return render(request, "teacher/index.html", context)

def add(request):
    context={"title":"Ajouter un eleve"}

    if request.method == "POST":
        print(request.POST)
        form = TeachFoM(request.POST)
        context["form"] = form
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('teacher:index')
        else:
            return render(request,"teacher/add.html")
    
    # context={'teach_form': teach_form}
    form = TeachFoM()
    context["form"] = form

    return render(request,"teacher/add.html",context)

def update(request, id):
    teacher = Teacher.objects.get(id=id)

    context = {"title":"Modifier professeur"}

    if request.method == "POST":
        form = TeachFoM(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher:index')
        
    form = TeachFoM(instance = teacher)

    context["form"] = form
    
    return render(request,"teacher/add.html",context)

def delete(request, id):
    teacher = Teacher.objects.get(id = id)
    teacher.delete()
    return redirect('teacher:index')