from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,  name='home'),
    path('about', views.about, name='about'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
    path('contacts/', views.contacts, name='contacts'),
]