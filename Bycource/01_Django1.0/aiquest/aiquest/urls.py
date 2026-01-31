from django.contrib import admin
from django.urls import path
from course import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("course/", views.course),
    path("ds/", views.data_science),
    path("wd/", views.web_development),
    path("ml", views.machine_learning),
    path("about", views.about),
]