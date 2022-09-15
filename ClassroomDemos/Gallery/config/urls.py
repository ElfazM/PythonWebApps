from django.urls import path
from photos.views import PhotoView 

urlpatterns = [
    path('<str:name>', PhotoView.as_view()), # gets code from photoview  and runs as.view function on it  <str:name what file the user is asking for
    #    <str:name> gets url you are asking for 
    # and passes it through the views directory as the name KEY work - kwargs
]
