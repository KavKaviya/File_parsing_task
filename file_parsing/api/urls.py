from django.urls import path, include
from . import views


urlpatterns=[
    path("upload-retrieve-csv-file", views.csvFileUploadView.as_view()),
    path("retrieve_a_file_detail", views.retrieve_a_fileDetails.as_view({"get":"retrieve"}))
]