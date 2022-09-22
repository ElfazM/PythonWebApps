from pathlib import Path
from django.views.generic import TemplateView

from .models import HeroD


class heroListView(TemplateView):
    template_name = 'heros.html'

    def get_context_data(self, **kwargs):
        return {
            'object_list': HeroD.objects.all()
        }
        


class heroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'note': HeroD.objects.get(pk=kwargs['pk'])
        }

