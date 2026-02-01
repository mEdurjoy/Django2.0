from django.urls import path
from . import views
urlpatterns = [
    path("", views.teacher_dashboard),
    path("profile/", views.teacher_profile),
]
