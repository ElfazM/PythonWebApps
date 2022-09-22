from email.mime import image
from pathlib import Path
from unicodedata import name
from django.views.generic import TemplateView


class HeroView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        name = kwargs['name']
        image = f'/static/images/{name}'
        return {'hero': image}




class HeroListView(TemplateView):
    template_name = 'heros.html'

    def get_context_data(self, **kwargs):
        heros = Path('static/images').iterdir()
        heros = [ f for f in heros]
        return dict(heros=heros) 

