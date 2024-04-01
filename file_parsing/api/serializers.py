from .models import *
from rest_framework import serializers
import datetime


class csvFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=csvFileUpload
        fields=["file_id","upload_file","created_at"]
        

