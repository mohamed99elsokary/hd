from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_categories),
    path("category/<str:category>", views.all_products),
    path("<int:id>/", views.product_details),
    path("add_product", views.add_product),
]
