from rest_framework import serializers
from main_api.models import Role, User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'username', 'password']


class RoleSerializer (serializers.ModelSerializer):
    class Meta:
        model=Role
        fields = ['id', 'rolename']