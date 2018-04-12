from django.db import models
from datetime import datetime

# Create your models here.
class FileName(models.Model):
    file_name = models.CharField('ファイル名', max_length=50)
    upload_time = models.DateTimeField('アップロード日時', default = datetime.now)

    def __str__(self):
        return self.file_name
