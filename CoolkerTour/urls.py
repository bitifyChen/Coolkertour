from django.contrib import admin
from django.urls import path, include
from web import views as web

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('ckeditor', include('ckeditor_uploader.urls')),

    path('', web.index, name='index'),
    path('login/', web.login, name='login'),
    path('logout/', web.logout, name='logout'),
    path('member/', include('member.urls')),
    path('shop/', include('shop.urls')),
    path('tour/', include('tour.urls')),
    path('album/', include('album.urls')),
    path('work/', include('work.urls')),
]
