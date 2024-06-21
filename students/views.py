# views.py
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Students

class StudentCreateView(View):
    def get(self, request):
        return render(request, 'home.html')
    
    def post(self, request):
        name = request.POST.get('Name')
        age = request.POST.get('Age')
        student = Students.objects.create(name=name, age=age)

        return render(request, 'home.html')
