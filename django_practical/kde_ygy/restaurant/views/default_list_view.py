from django.db.models import F
from django.views.generic.list import ListView
from django.utils import timezone

from ..models import Restaurant


class DefaultListView(ListView):
    model = Restaurant
    template_name = 'restaurant/list.html'
    context_object_name = 'restaurants'

    # TODO : internal server error 예외처리 개선
    def get_queryset(self):
        try:
            present_time = timezone.localtime().strftime('%H:%M:%S')
            qs = self.model.objects.filter(
                open_time__lte=present_time,
                close_time__gt=present_time,
                postal_code=self.kwargs['postal_code'],
            )
        except Exception as err:
            raise err
        else:
            return qs
