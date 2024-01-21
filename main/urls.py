from django.urls import path
from main.apps import MainConfig
from django.views.decorators.cache import cache_page
from main.views import index, UserListView, UserDetailView, MassageListView, MassageDetailView, MassageCreateView, \
    MassageUpdateView, UserUpdateView, MassageDeleteView, SettingsReportListView, ClientListView, ClientDetailView, \
    ClientCreateView, ClientUpdateView, \
    ClientDeleteView, SettingsListView, SettingsDetailView, SettingsCreateView, SettingsUpdateView, SettingsDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(5*60)(index), name='index'),
    path('users_list/', cache_page(5*60)(UserListView.as_view()), name='users_list'),
    path('user/view/<int:pk>/', cache_page(5*60)(UserDetailView.as_view()), name='user_view'),
    path('user/edit/<int:pk>/', cache_page(5*60)(UserUpdateView.as_view()), name='user_update'),
    path('report/', cache_page(5*60)(SettingsReportListView.as_view()), name='report'),
    path('massages/', cache_page(5*60)(MassageListView.as_view()), name='massage_list'),
    path('massage/view/<int:pk>/', cache_page(5*60)(MassageDetailView.as_view()), name='massage_view'),
    path('massage/create/', cache_page(5*60)(MassageCreateView.as_view()), name='massage_create'),
    path('massage/edit/<int:pk>/', cache_page(5*60)(MassageUpdateView.as_view()), name='massage_update'),
    path('massage/delete/<int:pk>/', cache_page(5*60)(MassageDeleteView.as_view()), name='massage_delete'),
    path('clients/', cache_page(5*60)(ClientListView.as_view()), name='client_list'),
    path('client/view/<int:pk>/', cache_page(5*60)(ClientDetailView.as_view()), name='client_view'),
    path('client/create/', cache_page(5*60)(ClientCreateView.as_view()), name='client_create'),
    path('client/edit/<int:pk>/', cache_page(5*60)(ClientUpdateView.as_view()), name='client_update'),
    path('client/delete/<int:pk>/', cache_page(5*60)(ClientDeleteView.as_view()), name='client_delete'),
    path('settings/', cache_page(5*60)(SettingsListView.as_view()), name='settings_list'),
    path('settings/view/<int:pk>/', cache_page(5*60)(SettingsDetailView.as_view()), name='settings_view'),
    path('settings/create/', cache_page(5*60)(SettingsCreateView.as_view()), name='settings_create'),
    path('settings/edit/<int:pk>/', cache_page(5*60)(SettingsUpdateView.as_view()), name='settings_update'),
    path('settings/delete/<int:pk>/', cache_page(5*60)(SettingsDeleteView.as_view()), name='settings_delete')
]
