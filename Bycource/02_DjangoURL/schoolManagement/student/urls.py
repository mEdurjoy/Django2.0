from django.urls import path
from . import views
urlpatterns = [
    path("sd/", views.student_dashboard),
    path("sp/", views.student_profile),
]
