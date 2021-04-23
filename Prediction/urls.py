from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path("PredictCovid/", views.PredictCovid,name='PredictCovid'),
    path("Home_Covid/", views.Home_Covid,name='Home_Covid'),
    #path("ResultCovid/", views.ResultCovid,name='ResultCovid'),
    path("PredictCovid/result/", views.result),
]