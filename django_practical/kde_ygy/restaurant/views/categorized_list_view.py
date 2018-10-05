from django.views.generic.list import ListView

from ..models import Restaurant


class CategorizedListView(ListView):
    model = Restaurant
    template_name = 'restaurant/list.html'
    context_object_name = 'restaurants'

