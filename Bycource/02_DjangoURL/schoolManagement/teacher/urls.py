from django.urls import path
from . import views
urlpatterns = [
    path("td/", views.teacher_dashboard),
    path("tp/", views.teacher_profile),
]
