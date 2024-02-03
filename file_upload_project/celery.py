from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем переменную окружения для настройки Django перед использованием Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_upload_project.settings')

# Создаем экземпляр Celery и настраиваем его используя файл настроек Django
celery_app = Celery('file_upload_project')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузка задач из всех файлов tasks.py в приложениях Django
celery_app.autodiscover_tasks()
