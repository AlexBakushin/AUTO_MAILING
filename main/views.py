from django.shortcuts import render
from main.models import Massage
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
    fields = ('head', 'body', 'settings', 'logs')
    success_url = reverse_lazy('main:massage_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание сообщения'
        return context


class MassageUpdateView(LoginRequiredMixin, UpdateView):
    model = Massage
    fields = ('head', 'body', 'settings', 'logs')

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
