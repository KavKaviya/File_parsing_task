# Generated by Django 5.0.1 on 2024-04-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_csvfileupload_upload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfileupload',
            name='upload_file',
            field=models.FileField(upload_to=''),
        ),
    ]
