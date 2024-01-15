from django.urls import path
from main.apps import MainConfig
from main.views import index, MassageListView, MassageDetailView, MassageCreateView, MassageUpdateView, \
    MassageDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('massages/', MassageListView.as_view(), name='massage_list'),
    path('view/<int:pk>/', MassageDetailView.as_view(), name='massage_view'),
    path('create/', MassageCreateView.as_view(), name='massage_create'),
    path('edit/<int:pk>/', MassageUpdateView.as_view(), name='massage_update'),
    path('delete/<int:pk>/', MassageDeleteView.as_view(), name='massage_delete')
]
