from django.urls import path
from . import views

# отслеживание адресов
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('chat', views.flex, name='chat')
]