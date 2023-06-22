from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from minio import Minio


# Create your views here.

class FileUploadView(View):
    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')  # Получаем загруженный файл

        # Подключаемся к Minio серверу
        minio_client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=False  # Измените на True, если используете HTTPS
        )

        # Загружаем файл в Minio
        minio_client.put_object(
            bucket_name=settings.MINIO_BUCKET_NAME,
            object_name=file_obj.name,
            data=file_obj
        )

        return JsonResponse({'message': 'Файл успешно загружен'})

    def get(self, request, *args, **kwargs):
        filename = kwargs['filename']  # Получаем имя файла из URL
        # Подключаемся к Minio серверу
        minio_client = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=False  # Измените на True, если используете HTTPS
        )

        # Получаем URL для доступа к файлу
        file_url = minio_client.presigned_get_object(
            bucket_name=settings.MINIO_BUCKET_NAME,
            object_name=filename
        )

        return JsonResponse({'file_url': file_url})
