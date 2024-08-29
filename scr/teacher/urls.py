from django.urls import path
from .views import index
from .views import add
from .views import update
from .views import delete

app_name="teacher"
urlpatterns = [
    path('', index,name="index"),
    path('add',add,name="add"),
    path('update/<int:id>',update,name="update-teacher"),
    path('delete/<int:id>',delete,name="delete-teacher"),
]