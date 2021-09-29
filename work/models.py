import os
import uuid
import datetime
import exifread
from imagekit.models import ImageSpecField
from imagekit.processors import Transpose
from pilkit.processors import ResizeToFill
from django.db import models


class Album(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '相簿'

    title = models.CharField('標題', max_length=100)
    sub_title = models.CharField('副標題', max_length=100, blank=True)
    description = models.TextField('描述', blank=True)
    icon = models.CharField('圖示', max_length=30)

    def __str__(self):
        return self.title


def upload_to_work_album(instance, filename):
    ext = filename.split('.')[-1]
    filename = uuid.uuid4()
    return os.path.join('img/work/album/' + str(instance.album.id) + '/{0}.{1}'.format(filename, ext))


class Photo(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '照片'

    photo = models.ImageField('照片', upload_to=upload_to_work_album, blank=True, null=True)
    square_banner = ImageSpecField(source="photo", processors=[Transpose(), ResizeToFill(600, 600)],
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
