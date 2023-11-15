from rest_framework import serializers
from rest_framework.response import Response
from django.db import IntegrityError
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name']

    def create(self, validated_data):
        validated_data['name'] = validated_data['name'].lower()
        try:
            instance = Animal.objects.using("memory").create(**validated_data)
            return instance
        except IntegrityError:
            raise serializers.ValidationError({"error": f"Animal named as {validated_data['name']} already exist"}, code='invalid')

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete(using="memory")
        return Response(status=status.HTTP_204_NO_CONTENT)
