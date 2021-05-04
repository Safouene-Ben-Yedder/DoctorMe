from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
#from .views import UserEditView

urlpatterns = [
    path('', views.indexView, name='home'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('register/', views.registerView, name='register_url'),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name='logout'),
    path('edit_profile/', views.editView, name='edit_profile'),

]