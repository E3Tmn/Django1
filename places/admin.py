from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminBase, SortableStackedInline

from .models import Place, Image
# Register your models here.


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['preview_image']
    ordering = ("serial_number",)
    def preview_image(self, obj):
        url = obj.picture.url
        return format_html(f'<img src="{url}" height="200px" />')

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
   

