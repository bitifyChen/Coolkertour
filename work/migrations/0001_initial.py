# Generated by Django 2.2.13 on 2020-08-24 14:44

from django.db import migrations, models
import django.db.models.deletion
import work.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='標題')),
                ('sub_title', models.CharField(max_length=100, verbose_name='副標題')),
                ('description', models.TextField(blank=True, verbose_name='描述')),
                ('icon', models.CharField(max_length=30, verbose_name='圖示')),
            ],
            options={
                'verbose_name': '相簿',
                'verbose_name_plural': '相簿',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=work.models.upload_to_work_album, verbose_name='照片')),
                ('upload_date', models.DateTimeField(blank=True, verbose_name='上傳日期')),
                ('shooting_date', models.DateTimeField(blank=True, null=True, verbose_name='拍攝日期')),
                ('cover_photo', models.BooleanField(default=False, verbose_name='相簿封面')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='work.Album', verbose_name='相簿')),
            ],
            options={
                'verbose_name': '照片',
                'verbose_name_plural': '照片',
            },
        ),
    ]