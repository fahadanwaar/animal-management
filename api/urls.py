from django.urls import path
from .views import AnimalListAPIView, AnimalRemoveAPIView

urlpatterns = [
    path('animals/', AnimalListAPIView.as_view(), name='animal-list'),
    path('animals/<int:pk>/', AnimalRemoveAPIView.as_view(), name='animal-remove')
]

