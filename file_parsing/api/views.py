import datetime
import mimetypes
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import *
from .models import *
import random
import pandas
from rest_framework import status
from rest_framework import viewsets
from django.urls import reverse

class csvFileUploadView(APIView):
    
    def post(self, request):
            parser_classes=[MultiPartParser,FormParser]
            file=request.FILES.get('upload_file')
            if not file:
                return Response({"Message":"Please upload a file.","Status":status.HTTP_400_BAD_REQUEST})
            elif file.content_type!="text/csv":
               return Response({"Message":"Please upload a CSV file.","Status":status.HTTP_400_BAD_REQUEST})
            unique_id=random.randint(100000,999999)
            print(unique_id, type(unique_id))
            request.data["file_id"]=unique_id
            serializer=csvFileUploadSerializer(data=request.data)
            if serializer.is_valid():
                 serializer.save()
                 print(serializer.data)
                 return Response({"Message":"Successfully uploaded your CSV file.", "Status":status.HTTP_200_OK, "File Id":serializer.data['file_id']})
            return Response(serializer.errors)
            
    
    def get(self, request):
        try:
             file_ids=request.data['file_ids']
             if file_ids:
                  datas=[]
                  serializer_data=[]
                  for id in file_ids:
                    obj=csvFileUpload.objects.get(file_id=id)
                    datas.append(obj)
                  serializer=csvFileUploadSerializer(datas, many=True)
                  for data in serializer.data:
                      file_id=data['file_id']
                      file=data['upload_file'].split("/")[2]
                      print(data['upload_file'].split("/"))
                      serializer_data.append({
                          "File id":file_id,
                          "File":file
                      })
                  print(serializer_data)
                  return Response(serializer_data)
             return Response({"Message":"Please enter file ids.","Status":status.HTTP_400_BAD_REQUEST})
        except csvFileUpload.DoesNotExist:
            return Response({"Message":"Please enter valid file ids.", "Status":status.HTTP_404_NOT_FOUND})


class retrieve_a_fileDetails(viewsets.ModelViewSet):
    serializer_class=csvFileUploadSerializer
    def retrieve(self,request):
        try:
         file_id=request.data['file_id'] 
         if not file_id:
              return Response({"Message":"Please enter valid file id", "Status":status.HTTP_400_BAD_REQUEST})
         file_id=int(file_id)
         csvFileUploadModel=csvFileUpload.objects.get(file_id=file_id)
         uploaded_file=csvFileUploadModel.upload_file
         file_name=uploaded_file.name
         file_size=uploaded_file.size
         change_b_kb_size="{} byte".format(file_size)
         file_extension = uploaded_file.name.split('.')[-1]
         file_type, _ = mimetypes.guess_type(f"file.{file_extension}")
         data_frame=pandas.read_csv(uploaded_file)
         rows,col=data_frame.shape
         serializer=self.get_serializer(csvFileUploadModel)
         res={
              "File Name":file_name,
              "File Size":change_b_kb_size,
              "File Type":file_type,
              "File Extention":file_extension,
              "File created date and time":serializer.data['created_at'],
              "Number of rows in the file":rows,
              "Number of columns in the file":col,
              "Download link":serializer.data['upload_file']
         }
         return Response({"Data":res, "Status":status.HTTP_200_OK})
        except csvFileUpload.DoesNotExist:
         return Response({"Message":"File not found, please enter valid file id.", "Status":status.HTTP_404_NOT_FOUND})
