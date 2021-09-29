import json
import logging

from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import render

from CoolkerTour.form_messages import push_form_errors
from .forms import PhotoForm
from .models import Album, Photo
logger = logging.getLogger('debug')


def album(request):
    albums = Album.objects.all().order_by('-travel_date')
    years = get_album_years()
    return render(request, "album.html", locals())


def get_album_years():
    years = {}
    for album_date in Album.objects.all().order_by('-travel_date__year').values_list('travel_date', flat=True):
        if album_date.year not in years:
            years[album_date.year] = 0
        years[album_date.year] += 1
    return years


def album_detail(request, album_id):
    query_album = Album.objects.filter(id=album_id)
    if query_album.exists():
        obj_album = query_album.get()
        photos = Photo.objects.filter(album=obj_album)
    return render(request, "album_detail.html", locals())


def album_upload(request, album_id):
    if request.user.is_authenticated:
        query_album = Album.objects.filter(id=album_id)
        if query_album.exists():
            obj_album = query_album.get()
            if request.method == 'POST':
                post_form = PhotoForm({'album': album_id}, request.FILES)
                if post_form.is_valid():
                    post_form.save()
                else:
                    push_form_errors(request, post_form, json.loads(post_form.errors.as_json()))
            else:
                post_form = PhotoForm()
        return render(request, "album_upload.html", locals())
    raise PermissionDenied


def album_verify(request, album_id):
    if request.method == 'GET':
        query_album = Album.objects.filter(id=album_id)
        if query_album.exists():
            user_input = request.GET.get('password')
            if user_input:
                if user_input == query_album.get().random_code:
                    return JsonResponse({'msg': 'success'})
                return JsonResponse({'msg': 'wrong'})
            return JsonResponse({'msg': 'empty'})
        else:
            return JsonResponse({'msg': 'album not exist'})
