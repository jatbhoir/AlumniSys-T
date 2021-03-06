# Generated by Django 3.0.5 on 2021-05-20 16:17

import Accounts.models
import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('bio', models.TextField(blank=True, default='', max_length=300, null=True)),
                ('website', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', max_length=128, null=True, region=None)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('avatar', models.ImageField(default='avatar.png', upload_to=Accounts.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('grno', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('is_private', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
