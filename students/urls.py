# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentCreateView.as_view(), name='home'),
]
