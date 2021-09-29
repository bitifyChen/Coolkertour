from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Album, Photo


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'sub_title', 'description')
    readonly_fields = ('title',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'square_photo', 'upload_date', 'shooting_date', 'cover_photo')
    list_editable = ('cover_photo',)
    list_filter = ('album',)
    readonly_fields = ('upload_date',)

    def square_photo(self, obj):
        if obj.square_banner:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.square_banner.url,
                width=75,
                height=75,
            )
            )
        return ''

    square_photo.short_description = '縮圖'


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
