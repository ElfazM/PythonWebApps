from django.urls import path
from hero.views import HulkView, BlackWidow, IndexView, IronManView, DragonView, ThroneView


urlpatterns = [
    path('', IndexView.as_view()),
    path('hulk', HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('blackwidow', BlackWidow.as_view()),
    path('houseofthedragon',DragonView.as_view()),
    path('gameofthrones',ThroneView.as_view()),
    
]
