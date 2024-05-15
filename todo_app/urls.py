from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addtodo', views.addtodo, name='addtodo'),
    path('delete/<int:todo_id>', views.delete_todo, name='delete_todo')
]