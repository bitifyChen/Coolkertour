import datetime
from django.db import models


class Message(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '訊息'

    name = models.CharField('姓名', max_length=20)
    email = models.CharField('電子郵件', max_length=255)
    phone = models.CharField('電話', max_length=50, blank=True, null=True)
    subject = models.CharField('主旨', max_length=100)
    content = models.TextField('內容')
    timestamp = models.DateTimeField('時間戳', default=datetime.datetime.now)

    def __str__(self):
        return self.name
