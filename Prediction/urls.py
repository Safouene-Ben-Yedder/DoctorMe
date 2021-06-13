from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path("Home_Covid/", views.Home_Covid,name='Home_Covid'),

     path("DoctorBox/", views.DoctorBox,name='DoctorBox'),
     path("DoctorBox/resultDB/", views.resultDB),
    #path("ResultCovid/", views.ResultCovid,name='ResultCovid'),

    path("PredictCovid/", views.PredictCovid,name='PredictCovid'),
    path("PredictCovid/result/", views.result),
   
    path("PredictDiabetes/", views.PredictDiabetes,name='PredictDiabetes'),
    path("PredictDiabetes/resultD/", views.resultD),
    
    path("PredictHeart/", views.PredictHeart,name='PredictHeart'),
    path("PredictHeart/resultH/", views.resultH),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)