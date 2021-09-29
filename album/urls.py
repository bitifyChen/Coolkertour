from django.urls import path
from . import views as album

urlpatterns = [
    path('', album.album, name='album'),
    path('<int:album_id>/detail/', album.album_detail, name='album_detail'),
    path('<int:album_id>/upload/', album.album_upload, name='album_upload'),
    path('<int:album_id>/verify/', album.album_verify, name='album_verify'),
]
