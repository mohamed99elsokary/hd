from django.db import models

# Create your models here.


class Categories(models.Model):
    category = models.CharField(max_length=150)
    icon = models.ImageField(
        upload_to="products/categories",
        height_field=None,
        width_field=None,
        max_length=100,
        null=True,
        blank=True,
    )

    products = models.ManyToManyField("Products")

    def __str__(self):
        return self.category


class Tools(models.Model):
    name = models.CharField(max_length=150)
    ar_name = models.CharField(max_length=150, null=True, blank=True)
    icon = models.ImageField(
        upload_to="tools", height_field=None, width_field=None, max_length=None
    )

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    ar_description = models.TextField(null=True, blank=True)
    photo = models.ImageField(
        upload_to="products/images", height_field=None, width_field=None, max_length=100
    )
    volt = models.CharField(max_length=150, null=True, blank=True, default=None)
    ampere = models.CharField(max_length=150, null=True, blank=True, default=None)
    watt = models.CharField(max_length=150, null=True, blank=True, default=None)
    digram = models.ImageField(
        upload_to="products/digram", height_field=None, width_field=None, max_length=100
    )
    digram_2 = models.ImageField(
        upload_to="products/digram",
        height_field=None,
        width_field=None,
        max_length=100,
        null=True,
        blank=True,
    )
    quick_start = models.FileField(
        upload_to="products/quick_start", max_length=100, null=True, blank=True
    )
    specification = models.FileField(
        upload_to="products/specification", max_length=100, null=True, blank=True
    )
    user_manual = models.FileField(
        upload_to="products/user_manual", max_length=100, null=True, blank=True
    )
    sell_link = models.URLField(max_length=200)
    is_rf = models.BooleanField(default=False)
    is_app_control = models.BooleanField(default=False)
    is_single_count_down_timing = models.BooleanField(default=False)
    is_share_control = models.BooleanField(default=False)
    is_smart_scene = models.BooleanField(default=False)
    is_sync_status = models.BooleanField(default=False)
    is_lan_control = models.BooleanField(default=False)
    video_link = models.URLField(max_length=200, null=True, blank=True)
    programing_video_1 = models.URLField(max_length=200, null=True, blank=True)
    programing_video_2 = models.URLField(max_length=200, null=True, blank=True)
    voice_command_options = models.CharField(
        max_length=150, null=True, blank=True, default=None
    )
    number_of_gangs = models.IntegerField(null=True, blank=True, default=None)
    load_per_gang = models.CharField(
        max_length=150, null=True, blank=True, default=None
    )
    total_load = models.CharField(max_length=150, null=True, blank=True, default=None)
    working_temp = models.CharField(max_length=150)
    resistance_code = models.IntegerField(null=True, blank=True, default=None)
    material = models.CharField(max_length=150)
    how_to_pair = models.TextField()
    ar_how_to_pair = models.TextField(null=True, blank=True)
    tools = models.ManyToManyField(Tools, blank=True)

    def __str__(self):
        return self.name


class Questions(models.Model):
    question = models.CharField(max_length=150, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    ar_question = models.CharField(max_length=150, null=True, blank=True)
    ar_answer = models.TextField(null=True, blank=True)
    products = models.ManyToManyField(Products)

    def __str__(self):
        return self.question
