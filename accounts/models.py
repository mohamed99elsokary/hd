from django.db import models
from django.contrib.auth.models import User

from courses import models as courses_models


class categories(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return str(self.category)


class accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    profile_picture = models.ImageField(
        upload_to="profile_pics",
        height_field=None,
        width_field=None,
        max_length=100,
        null=True,
        blank=True,
        default=None,
    )

    category = models.ForeignKey(categories, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Grades(models.Model):
    course = models.ForeignKey(courses_models.Courses, on_delete=models.CASCADE)
    account = models.ForeignKey(accounts, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)

    def __str__(self):
        return str(self.course)
