from django.db import models
from products import models as products_models

# Create your models here.
class Client(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    classification = models.CharField(max_length=50)

    def __str__(self):
        return str(self.full_name)


class Phone_numbers(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return str(self.phone_number)


class Apartments(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)

    def __str__(self):
        return str(f"{self.client} {self.name}")


class Survey(models.Model):
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    survey = models.FileField(upload_to="client/survey/", max_length=100)
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(f"{self.apartment} {self.date}")


class offer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    offer = models.FileField(upload_to="client/offer", max_length=100)
    is_accepted = models.BooleanField(default=False)
    date = models.DateField(auto_now=True, auto_now_add=False)


class order(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    order = models.FileField(upload_to="client/order", max_length=100)
    date = models.DateField(auto_now=True, auto_now_add=False)


class Rooms(models.Model):
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class products_in_rooms(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    product = models.ForeignKey(products_models.Products, on_delete=models.CASCADE)
    before = models.ImageField(
        upload_to="client/before",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )
    after = models.ImageField(
        upload_to="client/after",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.product)
