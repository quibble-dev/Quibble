from rest_framework import exceptions, serializers

from ...models import QuibletModel


class QuibletSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuibletModel
        fields = '__all__'

    def validate_name(self, name):
        if QuibletModel.objects.filter(name__iexact=name).exists():
            raise exceptions.ValidationError(
                f"Quiblet with name {name} already exists (case-insensitive)."
            )

        return name


class QuibletSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuibletModel
        fields = ('name', 'avatar')
