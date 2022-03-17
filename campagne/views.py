from django.shortcuts import render
from django.http import HttpResponse
from .models import Team

def index(request):
    return HttpResponse("Campagne live")


def chart(request):
    return render(request, "chart.html", {"equipe1":Team.objects.filter(color="equipe1").get().score,
                                          "equipe2":Team.objects.filter(color="equipe2").get().score,
                                          "equipe3":Team.objects.filter(color="equipe3").get().score,
                                          "equipe4":Team.objects.filter(color="equipe4").get().score,
                                          "equipe5":Team.objects.filter(color="equipe5").get().score,
                                          "equipe6":Team.objects.filter(color="equipe6").get().score,
                                          "equipe7":Team.objects.filter(color="equipe7").get().score,
                                          "equipe8":Team.objects.filter(color="equipe8").get().score,
                                          "equipe9":Team.objects.filter(color="equipe9").get().score,
                                          "equipe10":Team.objects.filter(color="equipe10").get().score})
