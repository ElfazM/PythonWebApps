from django.views.generic import TemplateView


class HulkView(TemplateView):
    template_name = 'hero.html'
 
    def get_context_data(self, **kwargs):
        return {
            'title': 'House of The Dragon',
            'id': 'Rhaenyra Targaryen',
            'image': '/static/images/HouseOfDragon.jpg'
        }   


class IronManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Game of Thrones',
            'id': 'Daenerys Targaryen',
            'image': '/static/images/GameOfThrones.jpg'
        }   