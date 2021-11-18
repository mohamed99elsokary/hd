from django.shortcuts import render
from . import models

# Create your views here.
def all_exams(request):
    exams = models.exams.objects.all()
    context = {"exams": exams, "title": "all exams"}
    return render(request, "exams.html", context)


def exam(request, exam_id):
    exam = models.exams.objects.get(id=exam_id)
    exam_questions = exam.questions.all()
    questions = {}

    for question in exam_questions:
        answers = question.answers.all()
        questions[question] = answers
    if request.method == "POST":
        total = exam_questions.count()
        grade = 0
        for question in questions.keys():
            answer = request.POST.get(question.question)
            if answer == question.right_answer.answer:
                grade += 1
            models.exam_solves.objects.create(
                exam=exam,
                answer=answer,
                question=question.question,
                right_answer=question.right_answer,
            )
        models.exam_grades.objects.create(exam=exam, grade=grade, total=total)
    context = {"exam": exam, "questions": questions, "title": exam}

    return render(request, "exam.html", context)


def all_courses(request):
    courses = models.Courses.objects.all()
    context = {"courses": courses, "title": "all courses"}
    return render(request, "all-courses.html", context)


def course_lectures(request, course_id):
    course = models.Courses.objects.get(id=course_id)
    course_lectures = models.Lectures.objects.filter(course=course)
    context = {"course_lectures": course_lectures}
    return render(request, "lecture.html", context)


def course_lecture(request, course_id, lecture_id):
    course = models.Courses.objects.get(id=course_id)
    course_lectures = models.Lectures.objects.filter(course=course)
    lecture = models.Lectures.objects.get(id=lecture_id)
    lecture_videos = models.Videos.objects.filter(lecture=lecture)
    lecture_files = models.Files.objects.filter(lecture=lecture)
    lecture_images = models.Images.objects.filter(lecture=lecture)
    lecture_questions = lecture.questions.all()
    questions = {}
    for question in lecture_questions:
        answers = question.answers.all()
        questions[question] = answers

    context = {
        "course_lectures": course_lectures,
        "lecture": lecture,
        "lecture_videos": lecture_videos,
        "lecture_files": lecture_files,
        "lecture_questions": questions,
        "lecture_images": lecture_images,
    }
    return render(request, "lecture.html", context)
