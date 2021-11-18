from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_clients),
    path("<int:id>", views.client),
    path("ap/<int:id>", views.apartment),
    path("survey/<int:id>", views.survey),
]
