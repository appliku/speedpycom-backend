from rest_framework import serializers


class LogoutSerializer(serializers.Serializer):
    status = serializers.CharField(readonly=True)
