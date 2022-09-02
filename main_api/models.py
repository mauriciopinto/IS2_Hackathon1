from operator import truediv
from sqlite3 import Timestamp
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

    role = models.IntegerField (
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


class Store (models.Model):
    store_name = models.CharField (
        max_length=60,
        blank=False
    )

    description = models.TextField (
        max_length=200,
        blank=True
    )

    address = models.CharField (
        max_length=80,
        blank=False
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'store'
        verbose_name_plural = 'stores'
        app_label = 'main_api'


class Product (models.Model):
    store_id = models.ForeignKey (
        to='Store',
        on_delete=models.CASCADE
    )
    
    product_name = models.CharField (
        max_length=30,
        blank=False
    )

    description = models.TextField (
        max_length=200,
        blank=True
    )

    stock = models.IntegerField ()


class Purchase(models.Model):
    user_id = models.ForeignKey (
        to='User',
        on_delete=models.CASCADE
    )

    product_id = models.ForeignKey (
        to='Product',
        on_delete=models.CASCADE
    )

    timestamp = models.DateTimeField (
        
    )

