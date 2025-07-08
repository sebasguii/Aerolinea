from django.shortcuts import render, redirect
from .models import Avion
from .forms import AvionForm, RegistroUsuariosForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import AvionSerializer

class AvionViewSet(viewsets.ModelViewSet):
    queryset = Avion.objects.all()
    serializer_class = AvionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()