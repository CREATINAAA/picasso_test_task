# file_upload_app/views.py
from rest_framework import generics
from .models import File
from .serializers import FileSerializer
from .tasks import process_file

class FileListCreateView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        process_file.delay(instance.id)

