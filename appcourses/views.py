from django.shortcuts import render

# Create your views here.


def courses(request):
    template_name = 'appcourses/courses.html'
    return render(request, template_name)