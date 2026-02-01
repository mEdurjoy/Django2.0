from django.urls import path
from . import views
urlpatterns = [
    path("", views.student_dashboard),
    path("profile/", views.student_profile),
]
