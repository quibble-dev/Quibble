from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserAdminForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:  # pyright: ignore [reportIncompatibleVariableOverride]
        model = CustomUser
        fields = '__all__'

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
