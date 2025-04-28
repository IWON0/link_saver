from rest_framework import serializers
from links.models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ('user', 'title', 'description', 'image', 'link_type', 'created_at', 'updated_at')
