from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def presentation(request):
    return render(request, "presentation.html")

def interne(request):
    return HttpResponse("Activité interne")

def externe(request):
    return HttpResponse("Activité externe")
