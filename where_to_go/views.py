from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from places.models import Place, Image
from django.urls import reverse


def place_page(request, place_id):
  place = get_object_or_404(Place, id=place_id)
  images = Image.objects.filter(place=place)
  json_response = {
    "title": place.title,
    "imgs": [],
    "description_short": place.description_short,
    "description_long": place.description_long,
    "coordinates": {
        "lng": place.long,
        "lat": place.lat
    }
  }
  for image in images:
    json_response['imgs'].append(image.picture.url)

  return JsonResponse(json_response, json_dumps_params={'ensure_ascii': False, 'indent': 2})


def index_page(request):
    db_places = Place.objects.all()
    places = {
      "type": "FeatureCollection",
      "features": []
    }
    for place in db_places:
      places['features'].append({
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.long, place.lat]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse(place_page, kwargs={'place_id': place.id})
          }
        })

    data = {'places': places}
    return render(request, 'index.html', context=data)