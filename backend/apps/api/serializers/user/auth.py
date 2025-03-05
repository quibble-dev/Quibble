from dj_rest_auth.registration.serializers import (
    RegisterSerializer as RestAuthRegisterSerializer,
)
from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from apps.user.models import User

from .profile import ProfileBasicSerializer


class LoginSerializer(RestAuthLoginSerializer):
    """Custom LoginSerializer making email field required and removing username field"""

    username = None
    email = serializers.EmailField(required=True)


class RegisterSerializer(RestAuthRegisterSerializer):
    """Custom RegisterSerializer removing username field"""

    username = None


class UserDetailsSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'date_joined', 'profile')

    @extend_schema_field(ProfileBasicSerializer)
    def get_profile(self, obj):
        request = self.context.get('request')
        user_profile = getattr(request, 'user_profile', None)

        if user_profile:
            return ProfileBasicSerializer(user_profile, context={'request': request}).data
        return None
