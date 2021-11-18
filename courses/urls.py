from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_courses),
    path("exams/", views.all_exams),
    path("exams/<int:exam_id>/", views.exam),
    path("<int:course_id>/", views.course_lectures),
    path("<int:course_id>/<int:lecture_id>", views.course_lecture),
]
