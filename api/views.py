from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from .models import Animal
from .serializers import AnimalSerializer
from .pagination import CustomPagination
from rest_framework.views import APIView
from rest_framework.response import Response

class AnimalListAPIView(generics.ListCreateAPIView):
    queryset = Animal.objects.using('memory').all()
    serializer_class = AnimalSerializer
    pagination_class = CustomPagination

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AnimalSerializer(queryset, many=True)
        return Response(serializer.data)


class AnimalRemove(generics.DestroyAPIView):
    queryset = Animal.objects.using('memory').all()
    serializer_class = AnimalSerializer