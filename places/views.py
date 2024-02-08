from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place


def place_page(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    response = {
        "title": place.title,
        "imgs": [image.picture.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.long,
            "lat": place.lat
        }
    }

    return JsonResponse(
        response,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )


def index_page(request):
    db_places = Place.objects.all()
    places = {
        "type": "FeatureCollection",
        "features":
        [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.long, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(
                        place_page,
                        kwargs={'place_id': place.id}
                    )
                }
            } for place in db_places
        ]
    }

    data = {'places': places}
    return render(request, 'index.html', context=data)
