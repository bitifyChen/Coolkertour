from django.contrib import admin
from .models import Area, Tour, SeasonTour
from image_cropping import ImageCroppingMixin


class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'foreign', 'sort_index')
    list_filter = ('foreign',)
    list_editable = ('sort_index',)
    ordering = ('sort_index',)

    fields = ('name', 'foreign', 'sort_index')


class TourAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'category', 'foreign', 'page_views')
    list_filter = ('category__foreign',)

    fields = ('name', ('category', 'viewpoint'), 'content', 'photo1', 'crop_photo1', 'photo2', 'crop_photo2', 'days',
              'page_views')
    readonly_fields = ('page_views',)

    def foreign(self, obj):
        return obj.category.foreign
    foreign.short_description = '國外'
    foreign.boolean = True


class SeasonTourAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('tour', 'sub_title')


admin.site.register(Area, AreaAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(SeasonTour, SeasonTourAdmin)
