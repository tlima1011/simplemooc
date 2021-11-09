from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from appcourses.models import Course


def hello(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def courses(request):
    courses = Course.objects.all()
    template_name = 'courses.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

