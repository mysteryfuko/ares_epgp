from django.urls import path
from django.urls import include, path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('PlayerDetail/<str>/',views.PlayerDetail),
    path('kill/<id>/',views.kill),
    path('ajax/<str:action>/',views.ajax),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns