from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.Main, name='Main'),
    url('Contact/', views.Contact, name='Contact'),
    url('About/', views.About, name='About'),
    path('accounts/', include('accounts.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)