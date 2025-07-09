from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentModel  
from .forms import StudentForm
from django.template import loader
#display & save form data   
def insert_Student(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = StudentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_Student.html", context)

# Create your views here.
def Add(request):
    temp=loader.get_template('Add.html')
    return HttpResponse(temp.render())
