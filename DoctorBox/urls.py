from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
     path("DoctorBox/", views.DoctorBox,name='DoctorBox'),
     path("DoctorBox/resultDB/", views.resultDB),
     path("DoctorBox/resultDB1/", views.resultDB1),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)