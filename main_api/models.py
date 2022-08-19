from django.db import models

# Create your models here.
class User (models.Model):
    username = models.CharField (
        max_length=30,
        unique=True
    )

    password = models.CharField (
        max_length=60,
        editable=True
    )

    role = models.ForeignKey (
        to='Role',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['id']
        verbose_name = 'user'
        verbose_name_plural = 'users'
        app_label = 'main_api'


class Role (models.Model):
    rolename = models.CharField (
        max_length=30,
        unique=True
    )

    def __str__(self):
        return self.rolename

    class Meta:
        ordering = ['id']
        verbose_name = 'role'
        verbose_name_plural = 'roles'
        app_label = 'main_api'