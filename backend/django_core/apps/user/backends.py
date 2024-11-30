from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()


class EmailAuthBackend(ModelBackend):
    """
    Custom Auth backend with email instead username
    """

    def authenticate(  # pyright: ignore [reportIncompatibleMethodOverride]
        self, request, email=None, password=None, **kwargs
    ):
        try:
            user = UserModel.objects.get(email=email)
            if password and user.check_password(password):
                return user
            return None
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id: int):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
