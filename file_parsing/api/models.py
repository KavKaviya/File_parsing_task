from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator,MinLengthValidator
from django.utils import timezone
import pytz

class csvFileUpload(models.Model):
    file_id=models.IntegerField()
    upload_file=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)

