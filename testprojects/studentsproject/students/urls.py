from django.urls import path
from .views import (WelcomeView, HomeView, StudentHomeRedirectView, StudentListView,
                    StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView, StudentSearchView)

urlpatterns = [
    path("welcome/", WelcomeView.as_view(), name="welcome"),
    path("home/", HomeView.as_view(), name="home"),
    path("", StudentHomeRedirectView.as_view(), name="student-home"),

    path('students/', StudentListView.as_view(), name="student-list"),
    path('students/create/', StudentCreateView.as_view(), name="student-create"),
    path('students/<int:pk>/', StudentDetailView.as_view(), name="student-detail"),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name="student-update"),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name="student-delete"),
    
    path('search/', StudentSearchView.as_view(), name="student-search"),
]
