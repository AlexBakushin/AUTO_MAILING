from django import forms
from main.models import Massage, Client, Settings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# class MassageForm(StyleFormMixin, forms.ModelForm):  # Форма под создание екземпляра продукта
#
#     class Meta:
#         model = Massage
#         # fields = '__all__' можно так (выбрать все поля)
#         fields = ('head', 'body',)
#         # exclude = ('is_active', ...,...)  + это (исключить)
#
#
# class ClientForm(StyleFormMixin, forms.ModelForm):  # Форма под создание екземпляра продукта
#
#     class Meta:
#         model = Client
#         # fields = '__all__' можно так (выбрать все поля)
#         fields = ('first_name', 'last_name', 'sur_name', 'mail', 'description')
#         # exclude = ('is_active', ...,...)  + это (исключить)
#
#
# class ModeratorClientForm(StyleFormMixin, forms.ModelForm):
#     class Meta:
#         model = Client
#         fields = ('is_active',)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#         self.fields["is_active"].widget.attrs['class'] = 'form-check-input'
#
#         def get_form_class(self):
#             if self.request.user == self.object.user:
#                 return ClientForm
#             elif self.request.user.groups.filter(name='manager').exists():
#                 return ModeratorClientForm
#             else:
#                 return ClientForm
#
#
# class SettingsForm(StyleFormMixin, forms.ModelForm):  # Форма под создание екземпляра продукта
#
#     class Meta:
#         model = Settings
#         # fields = '__all__' можно так (выбрать все поля)
#         fields = ('time', 'frequency', 'client', 'massage')
#         # exclude = ('is_active', ...,...)  + это (исключить)
