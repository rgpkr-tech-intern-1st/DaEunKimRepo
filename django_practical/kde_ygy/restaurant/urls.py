from django.urls import path

from .views import DefaultListView, CategorizedListView, DetailedView

app_name = 'restaurant'
urlpatterns = [
    path('<postal_code>/', DefaultListView.as_view(), name='default_list'),
    path('<postal_code>/<category>/', CategorizedListView.as_view(), name='categorized_list'),
    path('<int:pk>/', DetailedView.as_view(), name='detail'),
]
