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
        tourComponentList.append({'id': c.id, 'text': c.title})
    return render(request, "cms/add.html", locals())