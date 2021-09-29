from django.shortcuts import render


def shop_index(request):
    return render(request, "shopIndex.html", locals())

def shop_detail(request):
    return render(request, "shopDetail.html", locals())

def shop_list(request):
    return render(request, "shopList.html", locals())

def shop_submit(request):
    return render(request, "shopSubmit.html", locals())
