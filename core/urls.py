from django.contrib import admin
from django.urls import path, include

import core
from core import views, urls

urlpatterns = [
    path('home/', core.views.hello, name='home'),
    path('', core.views.hello, name='home'),
    path('contato/', core.views.contact, name='contact')
]
