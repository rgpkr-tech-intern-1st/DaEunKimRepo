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
            current_time = timezone.localtime()
            orderable_time = current_time + timezone.timedelta(hours=1)
            qs = self.model.objects.filter(
                open_time__lte=current_time.strftime('%H:%M:%S'),
                close_time__gt=orderable_time.strftime('%H:%M:%S'),
                address__startswith=self.kwargs['region'],
                postal_code=self.kwargs['postal_code'],
            )
        except Exception as err:
            raise err
        else:
            return qs
