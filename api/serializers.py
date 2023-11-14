from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name']

    def create(self, validated_data):
        validated_data['name'] = validated_data['name'].lower()
        instance = Animal.objects.using("memory").create(**validated_data)
        return instance

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete(using="memory")
        return Response(status=status.HTTP_204_NO_CONTENT)
