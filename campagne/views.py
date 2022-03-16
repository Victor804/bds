from django.shortcuts import render
from django.http import HttpResponse
from .models import Team

def index(request):
    return HttpResponse("Campagne live")


def chart(request):
    return render(request, "chart.html", {"bleu":Team.objects.filter(color="bleu").get().score,
                                          "jaune":Team.objects.filter(color="jaune").get().score,
                                          "violet":Team.objects.filter(color="violet").get().score,
                                          "vert":Team.objects.filter(color="verte").get().score,
                                          "rouge":Team.objects.filter(color="rouge").get().score})
