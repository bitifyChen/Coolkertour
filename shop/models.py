from django.db import models
from image_cropping import ImageRatioField


class TourComponent(models.Model):
    title = models.CharField('標題', max_length=100)
    description = models.TextField('敘述')
    photo = models.ImageField('圖片')
    crop_photo = ImageRatioField('photo', '320x180', verbose_name='剪裁圖片')

    class Meta:
        verbose_name = verbose_name_plural = '行程組件'

    def __str__(self):
        return self.title
