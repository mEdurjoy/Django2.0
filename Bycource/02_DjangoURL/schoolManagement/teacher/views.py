from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def teacher_dashboard(request):
    return HttpResponse("Welcome to the teacher Dashboard")
def teacher_profile(request):
    return HttpResponse("This is the Teacher Profile Page")