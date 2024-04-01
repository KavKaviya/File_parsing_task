# Generated by Django 5.0.1 on 2024-03-29 08:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfileupload',
            name='file_id',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(6), django.core.validators.MinLengthValidator(6)]),
        ),
    ]
