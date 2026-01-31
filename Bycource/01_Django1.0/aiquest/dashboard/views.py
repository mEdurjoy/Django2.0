from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dashboard_view(request):
    return HttpResponse("Welcome to the Dashboard!")
def another_view(request):
    return HttpResponse("This is another view in the dashboard.")