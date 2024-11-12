from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class PasswordlessAuthBackend(ModelBackend):
    def authenticate(  # pyright: ignore [reportIncompatibleMethodOverride]
        self, request, email: str | None = None, **kwargs
    ):
        try:
            user = UserModel.objects.get(email=email)
            return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id: int):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
