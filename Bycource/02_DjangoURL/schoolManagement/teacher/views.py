from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def teacher_dashboard(request):
    return render(request, 'dashboard.html')
def teacher_profile(request):
    return render(request, 'profile.html')