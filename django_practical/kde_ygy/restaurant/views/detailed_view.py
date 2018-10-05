from django.views.generic.detail import DetailView

from ..models import Restaurant


class DetailedView(DetailView):
    model = Restaurant
    template_name = 'restaurant/detail.html'
    context_object_name = 'restaurant'

