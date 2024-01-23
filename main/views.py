from django.shortcuts import render
from main.models import Massage, Client, Settings
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog
from users.models import User
from django.conf import settings
from django.core.cache import cache


@login_required
def index(request):
    if settings.CACHE_ENABLED:
        key = f'blog_list'
        blog_list = cache.get(key)
        if blog_list is None:
            blog_list = Blog.objects.all()[:3]
            cache.set(key, blog_list)
        else:
            blog_list = Blog.objects.all()[:3]

    all_massage = Massage.objects.count()
    active_massage = Settings.objects.filter(status='start')
    all_client = Client.objects.count()
    context = {
        'title': 'Главная',
        'all_massage': all_massage,
        'active_massage': active_massage.count(),
        'all_client': all_client,
        'blog': blog_list,
    }

    return render(request, 'main/index.html', context)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'main/users_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи'

        return context


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'main/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.email}'

        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('is_active',)

    def get_success_url(self):
        return reverse('main:user_view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Изменение "{self.object.email}"'

        return context_data


class SettingsReportListView(LoginRequiredMixin, ListView):
    model = Settings
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
    fields = ('head', 'body',)
    success_url = reverse_lazy('main:massage_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание сообщения'

        return context

    def form_valid(self, form):
        """
        Для автоматического выставления хозяина при регистрации нового пользователя
        :param form:
        :return:
        """
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class MassageUpdateView(LoginRequiredMixin, UpdateView):
    model = Massage
    fields = ('head', 'body',)

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

    def form_valid(self, form):
        """
        Для автоматического выставления хозяина при регистрации нового пользователя
        :param form:
        :return:
        """
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('first_name', 'last_name', 'sur_name', 'description',)

    def get_success_url(self):
        """
        Перенаправления после сохранения
        :return:
        """
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


class SettingsListView(LoginRequiredMixin, ListView):
    model = Settings
    template_name = 'main/settings_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список настроек'

        return context


class SettingsDetailView(LoginRequiredMixin, DetailView):
    model = Settings
    template_name = 'main/settings_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.time

        return context


class SettingsCreateView(LoginRequiredMixin, CreateView):
    model = Settings
    fields = ('time', 'frequency', 'client', 'massage')
    success_url = reverse_lazy('main:settings_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание настройки'

        return context

    def form_valid(self, form):
        """
        Для автоматического выставления хозяина при регистрации нового пользователя
        :param form:
        :return:
        """
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_form(self, form_class=None):
        """
        Было пипец как сложно до этого дойти, но у меня получилось
        эта функция фильтрует выборку клиентов и сообщения, на те, чей создатель - текущий пользователь
        + проверка на админа
        """
        form = super(SettingsCreateView, self).get_form(form_class)

        if not self.request.user.is_superuser:
            form.fields['client'].queryset = Client.objects.filter(user=self.request.user)
            form.fields['massage'].queryset = Massage.objects.filter(user=self.request.user)
            return form
        else:
            return form


class SettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Settings
    fields = ('time', 'frequency', 'client', 'massage')

    def get_success_url(self):
        return reverse('main:settings_view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Изменение настройки'

        return context_data

    def get_form(self, form_class=None):
        """
        Было пипец как сложно до этого дойти, но у меня получилось
        эта функция фильтрует выборку клиентов и сообщения, на те, чей создатель - текущий пользователь
        + проверка на админа
        """
        form = super(SettingsUpdateView, self).get_form(form_class)

        if not self.request.user.is_superuser:
            form.fields['client'].queryset = Client.objects.filter(user=self.request.user)
            form.fields['massage'].queryset = Massage.objects.filter(user=self.request.user)
            return form
        else:
            return form


class SettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = Settings
    success_url = reverse_lazy('main:settings_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление настройки'

        return context
