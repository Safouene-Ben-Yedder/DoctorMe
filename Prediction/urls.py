from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path("PredictCovid/", views.PredictCovid,name='PredictCovid'),
    path("Home_Covid/", views.Home_Covid,name='Home_Covid'),
    #path("ResultCovid/", views.ResultCovid,name='ResultCovid'),
    path("PredictCovid/result/", views.result),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)