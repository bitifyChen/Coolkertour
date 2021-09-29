from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import TourComponent


class TourComponentAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(TourComponent, TourComponentAdmin)
