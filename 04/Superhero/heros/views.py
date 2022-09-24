from pathlib import Path
from django.views.generic import TemplateView



class heroListView(TemplateView):
    template_name = 'heros.html'

    def get_context_data(self, **kwargs):
        return dict(heros=hero_list())


class heroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        heros = hero_list()
        p = heros[i]
        return dict(hero=p)

def hero_list():
    def hero_details(i, f):
        
        
        if   i == 0: caption = f'Itachi Uchiha ' 
        elif i == 1: caption = f'Jiraya the sage  ' 
        elif i == 2: caption = f'Kakashi Sense ' 
        elif i == 3: caption = f'Minato ' 
        elif i == 4: caption = f'Naruto Uzamaki ' 
        elif i == 5: caption = f'Sasuke Uchiha ' 
        else: None

        return dict(id=i, file=f, caption=caption)

    heros = Path('static/images').iterdir()
    heros = [hero_details(i, f) for i, f in enumerate(heros)]
    return heros