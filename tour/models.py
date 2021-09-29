import string
import random
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from image_cropping import ImageRatioField


def generate_random_code():
    while True:
        code = ''.join(random.sample(string.ascii_uppercase + string.digits, 4))
        if not Area.objects.filter(filter=code).exists():
            return code


class Area(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '行程地區'

    name = models.CharField('地區名稱', max_length=20)
    foreign = models.BooleanField('國外', default=False)
    filter = models.CharField('過濾器', max_length=20, unique=True, default=generate_random_code)
    sort_index = models.IntegerField('排序(整數)', default=0)

    def __str__(self):
        return self.name


digit_dict = {
    0: '', 1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九', 10: '十'
}


class Tour(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '行程'

    name = models.CharField('名稱', max_length=100)
    category = models.ForeignKey(Area, verbose_name='地區', on_delete=models.CASCADE, related_name='area')
    viewpoint = models.CharField('景點', max_length=50, blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True, verbose_name="內容")
    photo1 = models.ImageField('圖片1', blank=True, null=True)
    crop_photo1 = ImageRatioField('photo1', '320x180', verbose_name='剪裁圖片1')
    photo2 = models.ImageField('圖片2', blank=True, null=True)
    crop_photo2 = ImageRatioField('photo2', '320x180', verbose_name='剪裁圖片2')
    days = models.IntegerField('天數', default=1)
    hide = models.BooleanField('隱藏', default=False)
    page_views = models.IntegerField('瀏覽量', default=0)

    def day_ct(self):
        days_str = ''
        if self.days > 9:
            days_str += '十'
        days_str += digit_dict[self.days % 10]
        return days_str

    def __str__(self):
        return self.name


class SeasonTour(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '季節行程'
    tour = models.ForeignKey(Tour, verbose_name='行程', on_delete=models.CASCADE)
    sub_title = models.CharField('子標題', max_length=50)
    button_text = models.CharField('按鈕文字', max_length=50, default='觀看更多')
    banner = models.ImageField('橫幅', upload_to='img/season_tour/banner', blank=True)
    crop_banner = ImageRatioField('banner', '1920x1080', verbose_name='剪裁橫幅')
    hide = models.BooleanField('隱藏', default=False)

    def __str__(self):
        return self.tour.name
