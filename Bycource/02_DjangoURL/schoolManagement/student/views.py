from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_dashboard(request):
    return HttpResponse("Welcome to the Student Dashboard")
def student_profile(request):
    return HttpResponse("This is the Student Profile Page")