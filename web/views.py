import json
import requests
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import auth, messages

from CoolkerTour.form_messages import push_form_errors
from CoolkerTour.settings import RECAPTCHA_SECRET_KEY
from tour.models import Tour, SeasonTour
from album.models import Album
from .forms import LoginForm, ContactForm
from work import models as work
import logging
logger = logging.getLogger('debug')


def index(request):
    season_tours = SeasonTour.objects.exclude(hide=True).order_by('-id')
    season_tour_tour_ids = [query.get('tour') for query in season_tours.values('tour')]
    tours = Tour.objects.exclude(category__name='隱藏').exclude(id__in=season_tour_tour_ids).exclude(hide=True).order_by('-id')[:4]
    albums = Album.objects.all()[:12]
    work_albums = [
        work.Album.objects.get_or_create(title='員工/獎勵旅遊', icon='icon-et-briefcase')[0],
        work.Album.objects.get_or_create(title='家庭日/大型活動', icon='icon-et-flag')[0],
        work.Album.objects.get_or_create(title='會議假期/員工訓練', icon='icon-et-presentation')[0],
        work.Album.objects.get_or_create(title='春酒/尾牙', icon='icon-et-hotairballoon')[0],
    ]
    if request.method == 'GET':
        post_form = ContactForm()
    elif request.method == 'POST':
        post_form = ContactForm(request.POST)
        if post_form.is_valid():
            g_recaptcha_response = request.POST.get("g-recaptcha-response")
            r = requests.post("https://www.google.com/recaptcha/api/siteverify",
                              data={"secret": RECAPTCHA_SECRET_KEY, "response": g_recaptcha_response}, timeout=2)

            res = r.json()
            if 'success' in res and 'score' in res and 'action' in res:
                if not all((res["success"], res["score"] > 0.5, res["action"] == "contact")):
                    logger.debug('注意聯繫單(' + get_client_ip(request) + ') ' + str(res["score"]))
            post_form.save()
            messages.success(request, '送出成功')
        else:
            push_form_errors(request, post_form, json.loads(post_form.errors.as_json()))
    return render(request, "index.html", locals())


def login(request):
    if request.method == 'GET':
        post_form = LoginForm()
    elif request.method == "POST":
        post_form = LoginForm(request.POST)
        if post_form.is_valid():
            username = post_form.cleaned_data['username']
            password = post_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, '登入成功')
                return redirect('album')
            else:
                messages.error(request, '登入失敗！請確認帳號密碼是否錯誤!')
        else:
            push_form_errors(request, post_form, json.loads(post_form.errors.as_json()))
    return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('login')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

