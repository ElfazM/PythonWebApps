from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'




class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'body': 'My name is Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }
        


class DragonView(TemplateView):
    template_name = 'hero.html'
 
    def get_context_data(self, **kwargs):
        return {
            'title': 'House of The Dragon',
            'id': 'Rhaenyra Targaryen',
            'image': '/static/images/HouseOfDragon.jpg'
        }   


class ThroneView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Game of Thrones',
            'id': 'Daenerys Targaryen',
            'image': '/static/images/GameOfThrones.jpg'
        }   