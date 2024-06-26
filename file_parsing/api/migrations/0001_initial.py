# Generated by Django 5.0.1 on 2024-03-29 07:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='csvFileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(6)])),
                ('upload_file', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
