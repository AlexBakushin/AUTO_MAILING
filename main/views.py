from django.shortcuts import render
from main.models import Massage, Client
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'main/index.html', context)


class MassageReportListView(LoginRequiredMixin, ListView):
    model = Massage
    template_name = 'main/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отчет по рассылкам'
        return context


class MassageListView(LoginRequiredMixin, ListView):
    model = Massage
    template_name = 'main/massage_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список сообщений'
        return context


class MassageDetailView(LoginRequiredMixin, DetailView):
    model = Massage
    template_name = 'main/massage_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.head
        return context


class MassageCreateView(LoginRequiredMixin, CreateView):
    model = Massage
    fields = ('head', 'body', 'settings', 'logs', 'client',)
    success_url = reverse_lazy('main:massage_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание сообщения'
        return context


class MassageUpdateView(LoginRequiredMixin, UpdateView):
    model = Massage
    fields = ('head', 'body', 'settings', 'logs' 'client',)

    def get_success_url(self):
        return reverse('main:massage_view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Изменение "{self.object.head}"'
        return context_data


class MassageDeleteView(LoginRequiredMixin, DeleteView):
    model = Massage
    success_url = reverse_lazy('main:massage_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление "{self.object.head}"'
        return context


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'main/client_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список клиентов'
        return context


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'main/client_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.mail
        return context


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('first_name', 'last_name', 'sur_name', 'mail', 'description',)
    success_url = reverse_lazy('main:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запись клиента'
        return context


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('first_name', 'last_name', 'sur_name', 'description',)

    def get_success_url(self):
        return reverse('main:client_view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Изменение "{self.object.mail}"'
        return context_data


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('main:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление "{self.object.mail}"'
        return context
