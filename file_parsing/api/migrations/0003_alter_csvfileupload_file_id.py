# Generated by Django 5.0.1 on 2024-03-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_csvfileupload_file_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfileupload',
            name='file_id',
            field=models.IntegerField(),
        ),
    ]
