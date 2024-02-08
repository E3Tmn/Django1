from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

import requests

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает информацию о компаниях в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('link', help='Вставьте ссылку на json файл')

    
    def handle(self, *args, **options):
        response = requests.get(options['link'])
        response_json = response.json()
        Place.objects.get_or_create(
                title=response_json['title'],
                description_long=response_json['description_long'],
                description_short = response_json['description_short'],
                long = response_json['coordinates']['lng'],
                lat = response_json['coordinates']['lat']
            )
        place_imgs = response_json['imgs']
        place = get_object_or_404(Place, title=response_json['title'])
        for num, image_link in enumerate(place_imgs):
            image = Image.objects.get_or_create(place=place, serial_number=num)
            image[0].picture.save(
                        f'{num}.jpg', 
                        ContentFile(requests.get(image_link).content),
                        save=True
                    )
