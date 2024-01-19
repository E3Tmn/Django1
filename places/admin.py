from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html

# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['preview_image']
    def preview_image(self, obj):
        url = obj.picture.url
        return format_html(f'<img src="{url}" height="200px" />')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
   

