from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView, TemplateView, RedirectView, ListView, UpdateView, DetailView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from students.forms import StudentForm
from students.models import Student
from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
# Create your views here.


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Welcome to Student Management System")


class HomeView(TemplateView):
    template_name = "students/home.html"


class StudentHomeRedirectView(RedirectView):
    pattern_name = "student-list"
    permanent = False


class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q", "").strip()
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = "students/student_detail.html"
    context_object_name = "student"


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student-list")
    # login_url = "/accounts/login/"

    def form_valid(self, form):
        messages.success(self.request, "Student Created Successfully!")
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student-list")
    login_url = "/accounts/login/"


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Student
    template_name = "students/student_confirm_delete.html"
    success_url = reverse_lazy("student-list")
    permission_required = "students.delete_student"
    login_url = "/accounts/login/"


class StudentSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)


class StudentSearchView(FormView):
    template_name = "students/student_search.html"
    form_class = StudentSearchForm

    def form_valid(self, form):
        query = form.cleaned_data["query"]
        messages.success(self.request, f"Search Submitted: {query}")
        # return super().form_valid(form)
        return redirect(f"{reverse('student-list')}?q={query}")

    def get_success_url(self):
        return reverse_lazy("student-list")


class ProtectedStudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student-list")
    login_url = "/accounts/login/"


class StaffOnlyView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "students/home.html"

    def test_func(self):
        return self.request.user.is_staff
