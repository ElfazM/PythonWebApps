from pathlib import Path
from django.views.generic import TemplateView


def hero_list():
    def hero_details(i, f):
        caption = f'Caption for hero {i}' if i == 1 else None
        return dict(id=i, file=f, caption=caption)

    heroes = Path('static/images').iterdir()
    heroes = [hero_details(i, f) for i, f in enumerate(heroes)]
    return heroes


class heroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        return dict(heroes=hero_list())


class heroDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        heroes = hero_list()
        p = heroes[i]
        return dict(hero=p)
