from rest_framework import serializers, generics

from main.models import FrameworkModel


class FrameworkModelSerializer(serializers.ModelSerializer):
    """Сериализатор модели FrameworkModel"""
    class Meta:
        model = FrameworkModel
        fields = '__all__'

