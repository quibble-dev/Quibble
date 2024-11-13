from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'date_joined')
        read_only_fields = ('date_joined',)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label=_("Email"),
        write_only=True,
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True,
    )

    def validate(self, attrs):
        email = attrs.get('email')

        if email:
            user = authenticate(
                request=self.context.get('request'),
                email=email,
            )

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include an "email"')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
