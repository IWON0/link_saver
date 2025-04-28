from rest_framework import viewsets, permissions
from links.models import Link
from links.serializers import LinkSerializer
from links.utils import fetch_link_metadata

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        url = self.request.data.get('url')
        metadata = fetch_link_metadata(url)
        serializer.save(user=self.request.user, **metadata)
