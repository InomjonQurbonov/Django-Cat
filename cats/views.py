from rest_framework import viewsets
from cats.models import Cats
from cats.serializers import CatsSerializer, GetCatsSerializer
from config.permissions import OnlyUserPermissions
from cats.filters import CatsFilter


class CatsViewSet(viewsets.ModelViewSet):
    queryset = Cats.objects.all()
    permission_classes = [OnlyUserPermissions]
    filterset_class = CatsFilter

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return GetCatsSerializer
        return CatsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
