from django.http import HttpResponse
from django.shortcuts import render
from places.models import Place, Image


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
            "detailsUrl": "../static/places/moscow_legends.json"
          }
        })

    data = {'places': places}
    return render(request, 'index.html', context=data)