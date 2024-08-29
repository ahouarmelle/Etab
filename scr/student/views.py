from django.shortcuts import render, redirect
from .forms import EleveFoM
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {
        'students':students
        
    }
    return render(request, "student/index.html", context)

def add(request):
    context={"title":"Ajouter Eleve"}

    if request.method == "POST":
        print(request.POST)
        form =EleveFoM(request.POST)
        context["form"] = form
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect('student:index')
        else:
            return render(request,"student/add.html")

    # context={'elev_form':elev_form}
    form = EleveFoM()
    context["form"] = form

    return render(request,"student/add.html",context)

def update(request, id ):
    student = Student.objects.get(id=id)

    context = {"title":"Modifier eleve"}


    if request.method == "POST":
        form = EleveFoM(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:index')
        
    form = EleveFoM(instance = student)

    context["form"] = form

    return render(request,"student/add.html",context)

def delete(request ,id):
    student = Student.objects.get(id = id)
    student.delete()
    return redirect('student:index')
