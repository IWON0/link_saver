from rest_framework import serializers
from collections_app.models import Collection
from links.serializers import LinkSerializer

class CollectionSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at')
