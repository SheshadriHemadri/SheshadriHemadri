from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
