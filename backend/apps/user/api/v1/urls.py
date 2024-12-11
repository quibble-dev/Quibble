from django.urls import include, path

# from .views import LoginAPIView, LogoutAPIView, MeAPIView, RegisterAPIView

urlpatterns = [
    # auth endpoints
    # path(
    #     'auth/',
    #     include(
    #         [
    #             path('login/', LoginAPIView.as_view(), name='login'),
    #             path('logout/', LogoutAPIView.as_view(), name='logout'),
    #             path('register/', RegisterAPIView.as_view(), name='register'),
    #         ]
    #     ),
    # ),
    # # user view of requested user
    # path('me/', MeAPIView.as_view(), name='me'),
]
