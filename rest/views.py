from rest_framework import viewsets
from .models import Food, Owner, Pet
from .serializers import FoodSerializer, OwnerSerializer, PetSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAdminUser]


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
