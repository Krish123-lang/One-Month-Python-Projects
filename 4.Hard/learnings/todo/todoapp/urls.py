from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('create_todo', views.create_todo, name="create_todo"),
    path("todo_details/<int:pk>", views.todo_details, name="todo_details"),
    path("todo_update/<int:pk>", views.todo_update, name="todo_update"),
    path("todo_delete/<int:pk>", views.todo_delete, name="todo_delete"),
]
