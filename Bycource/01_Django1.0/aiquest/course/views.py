from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course(request):
    return HttpResponse("Welcome to the Course Page")

def data_science(request):
    return HttpResponse("Welcome to the Data Science Course")

def web_development(request):
    return HttpResponse("Welcome to the Web Development Course")

def machine_learning(request):
    return HttpResponse("Welcome to the Machine Learning Course")

def about(request):
    return HttpResponse("This is the About Page of the Course App")