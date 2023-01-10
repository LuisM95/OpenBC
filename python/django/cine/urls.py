from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('films/', views.film_saved,name = 'films')
]