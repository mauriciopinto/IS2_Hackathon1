from rest_framework import serializers
from main_api.models import User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'username', 'password']