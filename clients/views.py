from django.shortcuts import render
from . import models
from products import models as product_models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def all_clients(request):
    if request.method == "POST":
        client = models.Client.objects.create(
            full_name=request.POST.get("name"),
            email=request.POST.get("email"),
            classification=request.POST.get("classification"),
        )
        phone_number = models.Phone_numbers.objects.create(
            client=client, phone_number=request.POST.get("phone_number")
        )
    all_clients = models.Client.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(all_clients, 10)
    try:
        all_clients = paginator.page(page)
    except PageNotAnInteger:
        all_clients = paginator.page(1)
    except EmptyPage:
        all_clients = paginator.page(paginator.num_pages)
    context = {"all_clients": all_clients, "title": "all clients"}
    return render(request, "all_clients.html", context)


def client(request, id):
    client = models.Client.objects.get(id=id)
    if request.method == "POST":
        if request.POST.get("action") == "add_apartment":
            models.Apartments.objects.create(
                client=client,
                name=request.POST.get("address"),
                address=request.POST.get("address"),
            )

    client_phones = models.Phone_numbers.objects.filter(client=client)
    client_apartments = models.Apartments.objects.filter(client=client)
    context = {
        "title": "client details",
        "client": client,
        "client_phones": client_phones,
        "client_apartments": client_apartments,
    }
    return render(request, "client.html", context)


def apartment(request, id):

    if request.method == "POST":
        if request.POST.get("action") == "delete_product":
            models.products_in_rooms.objects.get(
                id=request.POST.get("product_id")
            ).delete()

        if request.POST.get("action") == "add_room":
            apartment = models.Apartments.objects.get(
                id=request.POST.get("apartment_id")
            )
            if request.POST.get("name") != None:
                if request.POST.get("name") != "":

                    room = models.Rooms.objects.create(
                        apartment=apartment, name=request.POST.get("name")
                    )

        if request.POST.get("action") == "add_survey":
            if request.FILES.get("uploadedFile") != None:
                uploadedFile = request.FILES["uploadedFile"]
                apartment = models.Apartments.objects.get(
                    id=request.POST.get("apartment_id")
                )
                room = models.Survey(apartment=apartment, survey=uploadedFile)
                room.save()

        if request.POST.get("action") == "add_product":

            if request.POST.get("product_id") != None:
                if request.POST.get("product_id") != "":
                    if request.POST.get("room_id") != None:
                        if request.POST.get("room_id") != "":
                            product = product_models.Products.objects.get(
                                id=request.POST.get("product_id")
                            )
                            room = models.Rooms.objects.get(
                                id=request.POST.get("room_id")
                            )
                            room = models.products_in_rooms.objects.create(
                                room=room, product=product
                            )

    apartment = models.Apartments.objects.get(id=id)
    surveys = models.Survey.objects.filter(apartment=apartment)
    client_rooms = models.Rooms.objects.filter(apartment=apartment)
    products = product_models.Products.objects.order_by("name")
    room_products = {}
    for room in client_rooms:
        room_product = models.products_in_rooms.objects.filter(room=room)
        room_products[room.name] = room_product

    context = {
        "title": "client details",
        "client_rooms": client_rooms,
        "apartment": apartment,
        "surveys": surveys,
        "room_products": room_products,
        "products": products,
    }
    return render(request, "apartment.html", context)


def survey(request, id):
    survey = models.Survey.objects.get(id=id)
    if request.method == "POST":
        if request.POST.get("action") == "delete_order":
            models.order.objects.get(id=request.POST.get("order_id")).delete()
        if request.POST.get("action") == "delete_offer":
            models.offer.objects.get(id=request.POST.get("offer_id")).delete()
        if request.POST.get("action") == "add_order":
            if request.FILES.get("uploadedFile") != None:
                uploadedFile = request.FILES["uploadedFile"]
                order = models.order(survey=survey, order=uploadedFile)
                order.save()
        if request.POST.get("action") == "add_offer":
            if request.FILES.get("uploadedFile") != None:
                uploadedFile = request.FILES["uploadedFile"]
                offer = models.offer(survey=survey, offer=uploadedFile)
                offer.save()
    offers = models.offer.objects.filter(survey=survey)
    try:
        order = models.order.objects.get(survey=survey)
    except:
        order = []
        pass
    context = {
        "title": "client details",
        "offers": offers,
        "order": order,
        "survey": survey,
    }
    return render(request, "surveys.html", context)
