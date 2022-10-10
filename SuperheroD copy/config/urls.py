from django.views.generic import RedirectView
from django.urls import path

from heroes.views import heroDetailView, heroListView


urlpatterns = [

    # Home
    path('', RedirectView.as_view(url='hero/')),

    # heros
    path('hero/', heroListView.as_view()),
    path('hero/<int:id>', heroDetailView.as_view()),
]
