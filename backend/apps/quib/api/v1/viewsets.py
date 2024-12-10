from rest_framework import viewsets

from apps.quib.models import Quib

from .serializers import QuibSerializer


class QuibViewSet(viewsets.ModelViewSet):
    queryset = Quib.objects.all()
    serializer_class = QuibSerializer
