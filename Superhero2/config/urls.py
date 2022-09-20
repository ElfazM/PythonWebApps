
from django.urls import path
from heros.views import HeroView


urlpatterns = [
    path('', HeroView.as_view()),
]
