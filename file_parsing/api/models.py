from django.db import models

class csvFileUpload(models.Model):
    file_id=models.IntegerField()
    upload_file=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)

