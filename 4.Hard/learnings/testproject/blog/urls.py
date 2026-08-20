from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/create', views.create_post, name="create_post"),
    path('post/edit/<int:id>/', views.edit_post, name="edit_post"),
    path('post/delete/<int:id>/', views.delete_post, name="delete_post"),
]
