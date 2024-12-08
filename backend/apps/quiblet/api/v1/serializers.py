from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.quiblet.models import Quiblet


class QuibletSerializer(ModelSerializer):
    class Meta:
        model = Quiblet
        fields = '__all__'

    def validate_name(self, name):
        if Quiblet.objects.filter(name__iexact=name).exists():
            raise ValidationError(
                f"Quiblet with name {name} already exists (case-insensitive)."
            )

        return name
