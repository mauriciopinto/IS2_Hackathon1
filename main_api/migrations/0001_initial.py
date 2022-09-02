# Generated by Django 4.1 on 2022-08-26 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'role',
                'verbose_name_plural': 'roles',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=60)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_api.role')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ['id'],
            },
        ),
    ]
