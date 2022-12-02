from django.views.generic import RedirectView
from django.urls import path
from django.contrib import admin
from heroes.views import heroDetailView, heroListView


urlpatterns = [

    #admin
    path('admin/', admin.site.urls),
    
    # Home
    path('', RedirectView.as_view(url='hero/')),

    # heros
    path('hero/', heroListView.as_view()),
    path('hero/<int:id>', heroDetailView.as_view()),
]