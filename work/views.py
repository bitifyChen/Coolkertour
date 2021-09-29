from django.shortcuts import render
from .models import Album, Photo


def work(request, work_album_id):
    album, created = Album.objects.get_or_create(id=work_album_id)
    photos = Photo.objects.filter(album=album)
    return render(request, "work.html", locals())
