from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Student

class StudentCreateView(CreateView):
    model = Student
    fields = ['title', 'author', 'publication_date']
    template_name = 'Student_form.html'  # Optional: specify custom template
    success_url = reverse_lazy('Student_list')  # URL to redirect to after successful form submission

class StudentListView(ListView):
    model = Student
    context_object_name = 'books'  # Optional: specify the context variable name in templates
    template_name = 'Student_list.html'  # Optional: specify custom template

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['title', 'author', 'publication_date']
    template_name = 'Student_form.html'  # Optional: specify custom template
    success_url = reverse_lazy('Student_list')  # URL to redirect to after successful form submission

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'Student_confirm_delete.html'  # Optional: specify custom template
    success_url = reverse_lazy('Student_list')  # URL to redirect to after successful deletion


# Create your views here.
