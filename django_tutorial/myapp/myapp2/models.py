from django.db import models

# Create your models here.
class Songs(models.Model):
    title = models.CharField('タイトル', max_length=255)
    artist = models.CharField('アーティスト', max_length=255)
    price = models.IntegerField('値段', default=0)
    genre = models.CharField('ジャンル', blank=True, max_length=255)

    def __str__(self):
        return self.title
