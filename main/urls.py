from django.urls import path
from main.apps import MainConfig
from main.views import index, UserListView, UserDetailView, MassageListView, MassageDetailView, MassageCreateView, \
    MassageUpdateView, UserUpdateView, MassageDeleteView, SettingsReportListView, ClientListView, ClientDetailView, \
    ClientCreateView, ClientUpdateView, \
    ClientDeleteView, SettingsListView, SettingsDetailView, SettingsCreateView, SettingsUpdateView, SettingsDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('users_list/', UserListView.as_view(), name='users_list'),
    path('user/view/<int:pk>/', UserDetailView.as_view(), name='user_view'),
    path('user/edit/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('report/', SettingsReportListView.as_view(), name='report'),
    path('massages/', MassageListView.as_view(), name='massage_list'),
    path('massage/view/<int:pk>/', MassageDetailView.as_view(), name='massage_view'),
    path('massage/create/', MassageCreateView.as_view(), name='massage_create'),
    path('massage/edit/<int:pk>/', MassageUpdateView.as_view(), name='massage_update'),
    path('massage/delete/<int:pk>/', MassageDeleteView.as_view(), name='massage_delete'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client/view/<int:pk>/', ClientDetailView.as_view(), name='client_view'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('settings/', SettingsListView.as_view(), name='settings_list'),
    path('settings/view/<int:pk>/', SettingsDetailView.as_view(), name='settings_view'),
    path('settings/create/', SettingsCreateView.as_view(), name='settings_create'),
    path('settings/edit/<int:pk>/', SettingsUpdateView.as_view(), name='settings_update'),
    path('settings/delete/<int:pk>/', SettingsDeleteView.as_view(), name='settings_delete')
]
