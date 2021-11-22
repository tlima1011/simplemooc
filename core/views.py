from django.shortcuts import render, get_object_or_404
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


'''def details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {
        'course': course
    }
    template_name = 'details.html'
    return render(request, template_name, context)
'''


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    template_name = 'details.html'
    return render(request, template_name, context)



