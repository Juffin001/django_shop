from .models import *


menu = [
    {'title': "_", "url_name": "_"},
    {'title': "_", "url_name": "_"},
    {'title': "_", "url_name": "_"},
    {'title': "_", "url_name": "_"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        boxes = box.objects.all()
        context['menu'] = menu
        context['boxes'] = boxes
        return context