import random
from django import template
from album.models import Photo

register = template.Library()


@register.simple_tag
def get_album_cover_photo(obj_album):
    photo_ids = Photo.objects.filter(album=obj_album, cover_photo=True).values_list('id', flat=True)
    if photo_ids.exists():
        return Photo.objects.get(id=photo_ids[random.randint(0, len(photo_ids) - 1)]).square_banner.url
    return ''
