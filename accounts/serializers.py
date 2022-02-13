from rest_framework import serializers
from accounts.models import Client


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'created_at', 'updated_at',)
