from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminBase, SortableStackedInline

from .models import Place, Image


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['get_preview_image']
    ordering = ("serial_number",)

    def get_preview_image(self, obj):
        url = obj.picture.url
        picture_height = 200
        return format_html('<img src="{}" max-height="{}px" />', url, picture_height)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place']