from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Company, Album, Photo


class CompanyAdmin(admin.ModelAdmin):
    pass


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'travel_date')
    ordering = ('-travel_date',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'square_photo', 'upload_date', 'shooting_date', 'cover_photo')
    list_editable = ('cover_photo', )
    list_filter = ('album', )
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


admin.site.register(Company, CompanyAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
