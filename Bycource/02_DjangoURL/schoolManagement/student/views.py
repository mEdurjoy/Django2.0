from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_dashboard(request):
    return render(request, 'dashboard.html')
def student_profile(request):
    return render(request, 'profile.html')