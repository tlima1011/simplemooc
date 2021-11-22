from django.shortcuts import render, get_object_or_404

# Create your views here.
from appcourses.models import Course


def courses(request):
    template_name = 'appcourses/courses.html'
    return render(request, template_name)


def details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {
        'course': course
    }
    template_name = 'core.templates.details.html'
    return render(request, template_name, context)