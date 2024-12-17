from rest_framework import exceptions, serializers

from ...models import Quiblet


class QuibletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiblet
        fields = '__all__'

    def validate_name(self, name):
        if Quiblet.objects.filter(name__iexact=name).exists():
            raise exceptions.ValidationError(
                f"Quiblet with name {name} already exists (case-insensitive)."
            )

        return name


class QuibletSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiblet
        fields = ('name', 'avatar')


class QuibletExistsSerializer(serializers.Serializer):
    exists = serializers.BooleanField()
    name = serializers.CharField()
