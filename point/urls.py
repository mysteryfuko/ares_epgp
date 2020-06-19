from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('epgp',views.epgp),
    path('epgplog',views.epgplog),
    path('epgplog1',views.epgplog1),
    path('dkp',views.dkp),
    path('dkplog',views.dkplog),
    path('dkplog1',views.dkplog1),
    path('PlayerDetail/',views.PlayerDetail),
    path('Playerepgplog/',views.Playerepgplog),
    path('Playerdkplog/',views.Playerdkplog),
    path('kill/',views.kill),
]