from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=50)


class DataEntrySerializer(serializers.Serializer):
    fields = serializers.JSONField()
