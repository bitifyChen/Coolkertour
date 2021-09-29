import os
import uuid
import string
import random
import datetime
import exifread
from imagekit.models import ImageSpecField
from imagekit.processors import Transpose
from pilkit.processors import ResizeToFill
from django.db import models
from django.utils.timezone import now
import logging
logger = logging.getLogger('debug')


class Company(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '公司'

    name = models.CharField('名稱', max_length=100)

    def __str__(self):
        return self.name


def generate_random_code():
    while True:
        code = ''.join(random.sample(string.ascii_uppercase + string.digits, 4))
        if not Album.objects.filter(random_code=code).exists():
            return code


class Album(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '相簿'

    name = models.CharField('名稱', max_length=100)
    company = models.ForeignKey(Company, verbose_name='公司', on_delete=models.CASCADE, related_name='company')
    travel_date = models.DateField('出團日期', default=now)
    description = models.TextField('描述', blank=True)
    random_code = models.CharField('隨機碼', max_length=10, unique=True, default=generate_random_code)

    def __str__(self):
        return self.name


def upload_to_album(instance, filename):
    ext = filename.split('.')[-1]
    filename = uuid.uuid4()
    return os.path.join('img/album/'+str(instance.album.id)+'/{0}.{1}'.format(filename, ext))


class Photo(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '照片'

    photo = models.ImageField('照片', upload_to=upload_to_album, blank=True, null=True)
    square_banner = ImageSpecField(source="photo", processors=[Transpose(),ResizeToFill(600, 600)],
                                   format='JPEG', options={'quality': 95})
    album = models.ForeignKey(Album, verbose_name='相簿', on_delete=models.CASCADE, related_name='album')
    upload_date = models.DateTimeField('上傳日期', blank=True)
    shooting_date = models.DateTimeField('拍攝日期', blank=True, null=True)
    cover_photo = models.BooleanField('相簿封面', default=False)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.upload_date = datetime.datetime.now()
        super().save(*args, **kwargs)
        f = open(self.photo.path, 'rb')
        tags = exifread.process_file(f)
        if 'EXIF DateTimeOriginal' in tags:
            self.shooting_date = datetime.datetime.strptime(str(tags['EXIF DateTimeOriginal']), '%Y:%m:%d %H:%M:%S')
            super().save(*args, **kwargs)
