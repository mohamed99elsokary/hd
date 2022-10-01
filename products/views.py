from django.shortcuts import render
from . import models
from . import forms

# Create your views here.
def all_categories(request):
    categories = models.Categories.objects.all()
    context = {"data": categories, "title": "all categories"}
    return render(request, "all_categories.html", context)


def all_products(request, category):
    cat = models.Categories.objects.get(category=category).products.all()
    context = {"data": cat, "title": "all product"}
    return render(request, "all_products.html", context)


def product_details(request, id):
    lang = "ar" if request.GET.get("lang") == "ar" else "en"
    product = models.Products.objects.get(id=id)
    questions = models.Questions.objects.filter(products=product)
    product_tools = product.tools.all()
    context = {
        "data": product,
        "questions": questions,
        "title": "product details",
        "product_tools": product_tools,
        "lang": lang,
    }
    return render(request, "product_details.html", context)


def add_product(request):
    form = forms.NameForm(request.POST)
    context = {"form": form, "title": "add product"}
    return render(request, "add_product.html", context)
