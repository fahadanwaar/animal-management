from django.urls import path
from .views import AnimalListAPIView, AnimalRemove

print("Inner URLS")
urlpatterns = [
    path('animals/', AnimalListAPIView.as_view(), name='animal-list'),
    path('animals/<int:pk>/', AnimalRemove.as_view(), name='animal-remove')
]

