from pathlib import Path
from turtle import title
from django.views.generic import TemplateView

def hero_list():
    def hero_details(i, f):
        
        
        if   i == 0: caption = f'Itachi Uchiha ' , 'Weakness: Terminaly Sick'
        elif i == 1: caption = f'Jiraya the sage  ' , 'Weakness: Tsunade '
        elif i == 2: caption = f'Kakashi Sense ' , 'Weakness:  cant show his face '
        elif i == 3: caption = f'Minato ' , ' Weakness: None'
        elif i == 4: caption = f'Naruto Uzamaki '  , ' Weakness: like father like son'
        elif i == 5: caption = f'Sasuke Uchiha ' , 'Weakness: Can not get over his brother betraying him '
        else: None

        return dict(id=i, file=f, caption=caption)

    heros = Path('static/images').iterdir()
    heros = [hero_details(i, f) for i, f in enumerate(heros)]
    return heros

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
