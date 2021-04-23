from django.urls import path
from forum.views import frontpage,post_detail
from .views import AddPostView
from . import views

urlpatterns = [
    #path('', views.page, name='page'),
    path('add_post/',AddPostView.as_view(),name='add_post')
]