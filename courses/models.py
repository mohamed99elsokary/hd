from django.db import models
from django.db.models.base import Model

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.ImageField(
        upload_to="courses/cover",
        height_field=None,
        width_field=None,
        max_length=100,
    )

    def __str__(self):
        return str(self.name)


class Lectures(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, related_name="course_lectures"
    )
    description = models.TextField()
    questions = models.ManyToManyField("Questions")

    def __str__(self):
        return str(self.name)


class Videos(models.Model):
    lecture = models.ForeignKey(Lectures, on_delete=models.CASCADE)
    video = models.FileField(upload_to="courses/videos", max_length=100)
    description_before = models.TextField()
    description_after = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return str(self.lecture)


class Files(models.Model):
    lecture = models.ForeignKey(Lectures, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to="courses/files", max_length=100)
    description_before = models.TextField()
    description_after = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return str(self.file)


class Images(models.Model):
    lecture = models.ForeignKey(Lectures, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to="courses/course_images",
        height_field=None,
        width_field=None,
        max_length=None,
    )
    description_before = models.TextField()
    description_after = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return str(self.name)


class Questions(models.Model):
    answers = models.ManyToManyField("Answers", related_name="question_answers")
    right_answer = models.ForeignKey(
        "Answers",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        related_name="right_answer",
    )
    question = models.CharField(max_length=50)

    def __str__(self):
        return str(self.question)


class Answers(models.Model):
    answer = models.CharField(max_length=50)

    def __str__(self):
        return str(self.answer)


class exams(models.Model):
    questions = models.ManyToManyField(Questions)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class exam_solves(models.Model):
    exam = models.ForeignKey(exams, on_delete=models.CASCADE)
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    right_answer = models.CharField(max_length=50)

    def __str__(self):
        return str(self.exam)


class exam_grades(models.Model):
    exam = models.ForeignKey(exams, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)
    total = models.CharField(max_length=50)

    def __str__(self):
        return str(self.exam)
