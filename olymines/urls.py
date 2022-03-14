from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('interne', views.interne, name="activite interne"),
    path('externe', views.externe, name="activite externe"),
    path('presentation', views.presentation, name="presentation")
]
