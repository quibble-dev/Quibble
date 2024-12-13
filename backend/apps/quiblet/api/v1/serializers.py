from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from ...models import Quib, Quiblet


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


class QuibletSlimSerializer(ModelSerializer):
    class Meta:
        model = Quiblet
        fields = ('name', 'avatar')


class QuibSerializer(ModelSerializer):
    quiblet = QuibletSerializer(read_only=True)

    class Meta:
        model = Quib
        fields = '__all__'


class QuibSlimSerializer(ModelSerializer):
    quiblet = QuibletSlimSerializer(read_only=True)

    class Meta:
        model = Quib
        exclude = ('quibber',)
