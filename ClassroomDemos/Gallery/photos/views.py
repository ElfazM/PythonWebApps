from decimal import getcontext
from django.views.generic import TemplateView

class PhotoView(TemplateView): 
    template_name = 'photo.html'

    def get_context_data(self, **kwargs): # key word argumets 
        name = kwargs['name']             # gets name from url
        image = f'\static\images\{name}'  # string that has url which will output whatever name the user asks from the image file
        return {'photo' : image}          # communicate with template to inject a variable that will point image which  wil have the name.

