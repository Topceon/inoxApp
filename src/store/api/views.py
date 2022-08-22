from rest_framework.viewsets import ModelViewSet

from store.api.serializers import StorageSerializer
from store.models import Storage


class StorageViewSet(ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
