from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def interne(request):
    return HttpResponse("Activité interne")

def externe(request):
    return HttpResponse("Activité externe")

def boutique(request):
    return HttpResponse("Boutique")

def calendrier(request):
    return render(request, 'calendar.html')
