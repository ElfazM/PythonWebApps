
from django.urls import path
from heros.views import HeroListView, HeroView



urlpatterns = [
    path('<str:name>', HeroView.as_view()),
    path('', HeroListView.as_view()) 
]
