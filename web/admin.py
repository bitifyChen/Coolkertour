from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Message._meta.fields]


admin.site.register(Message, MessageAdmin)
# Register your models here.
admin.AdminSite.site_header = '酷客旅遊 網站管理'
admin.AdminSite.site_title = '酷客旅遊'
