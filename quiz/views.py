from django.shortcuts import render
from .models import Quiz



def home(request):
    quizes = Quiz.objects.all()
    context = {
        "quiz" : quizes
    }
    return render(request , "home.html" , context)