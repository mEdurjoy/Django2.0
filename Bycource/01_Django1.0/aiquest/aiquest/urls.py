from django.contrib import admin
from django.urls import path
from course import views as course_views
from dashboard import views as dashboard_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("course/", course_views.course),
    path("ds/", course_views.data_science),
    path("wd/", course_views.web_development),
    path("ml", course_views.machine_learning),
    path("about", course_views.about),
    path("dashboard/", dashboard_views.dashboard_view),
    path("another/", dashboard_views.another_view),
]