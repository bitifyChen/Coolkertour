from easy_thumbnails.files import get_thumbnailer
from django.shortcuts import render
from shop.models import TourComponent


def shop_index(request):
    return render(request, "shop_index.html", locals())

def shop_detail(request):
    return render(request, "shop_detail.html", locals())

def shop_list(request):
    return render(request, "shop_list.html", locals())

def shop_submit(request):
    return render(request, "shop_submit.html", locals())

def shop_cms(request):
    return render(request, "cms/index.html", locals())

def shop_cms_add(request):
    tourComponentList = []
    for c in TourComponent.objects.all():
        thumbnail_url = get_thumbnailer(c.photo).get_thumbnail({'size': (320, 180),'box': c.crop_photo,'crop': True,'detail': True,}).url
        tourComponentList.append({'id': c.id, 'text': c.title,'description':c.description,'banner':thumbnail_url})
    return render(request, "cms/add.html", locals())