from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)