from django.forms import ModelForm
from .models import CustomUser

class CustomUserAdminForm(ModelForm):
    class Meta: # pyright: ignore [reportIncompatibleVariableOverride]
        model = CustomUser
        fields = ('email', 'is_active', 'is_staff')
