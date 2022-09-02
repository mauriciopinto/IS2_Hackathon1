from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from main_api.serializers import UserSerializer, RoleSerializer
from main_api.models import User, Role

# Create your views here.
class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['id']
    search_fields = ['username']
    