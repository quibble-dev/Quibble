from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import User, Profile


class CustomUserAdminForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:  # pyright: ignore [reportIncompatibleVariableOverride]
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class ProfileAdminForm(ModelForm):
    class Meta:  # pyright: ignore [reportIncompatibleVariableOverride]
        model = Profile
        fields = '__all__'

    def clean(self):  # pyright: ignore [reportIncompatibleVariableOverride]
        user = self.cleaned_data.get('user')

        if self.instance.pk is None and user and user.profiles.count() >= 5:
            self.add_error(None, _('A user cannot have more than 5 profiles.'))

        return self.cleaned_data
