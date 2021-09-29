# Generated by Django 2.2.13 on 2020-06-08 17:25

from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_tour_viewpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='crop_photo1',
            field=image_cropping.fields.ImageRatioField('photo1', '320x180', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='剪裁圖片1'),
        ),
        migrations.AddField(
            model_name='tour',
            name='crop_photo2',
            field=image_cropping.fields.ImageRatioField('photo2', '320x180', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='剪裁圖片2'),
        ),
        migrations.AddField(
            model_name='tour',
            name='page_views',
            field=models.IntegerField(default=0, verbose_name='瀏覽量'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.Area', verbose_name='地區'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='days',
            field=models.IntegerField(default=1, verbose_name='天數'),
        ),
        migrations.CreateModel(
            name='SeasonTour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=50, verbose_name='子標題')),
                ('button_text', models.CharField(default='觀看更多', max_length=50, verbose_name='按鈕文字')),
                ('banner', models.ImageField(blank=True, upload_to='img/season_tour/banner', verbose_name='橫幅')),
                ('crop_banner', image_cropping.fields.ImageRatioField('banner', '1920x1080', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='剪裁橫幅')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.Tour', verbose_name='行程')),
            ],
            options={
                'verbose_name': '季節行程',
                'verbose_name_plural': '季節行程',
            },
        ),
    ]