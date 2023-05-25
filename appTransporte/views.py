from django.shortcuts import render
import folium
from .models import puntosGPS
from .funtions import get_directions_response
import requests
# Create your views here.

def index(request):
    return render(request, 'index.html')
    #ip = request.META.get('REMOTE_ADDR')
    # respuesta = requests.get('https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyB1yKimI7f2QEmIh8C8H3k3eHTWh0sl92s')
    # print(respuesta)
    # if respuesta.status_code == 200:
    #     datos = respuesta.json()
    #     latitud = datos['location']['lat']
    #     longitud = datos['location']['lng']
    #     print([latitud, longitud])
    #     return render(request, 'index.html')
    # else:
    #     print("No se pudo obtener la ubicación")
    #     return render(request, 'index.html')
    
    """puntos = puntosGPS.objects.all()

    # crear un mapa con folium
    m = folium.Map(location=[25.4278684, -101.0046573], zoom_start=12)

    #
    responses = []
    for i in range(len(puntos) - 1):
        lat1, lon1, lat2, lon2 = puntos[i].latitud, puntos[i].longitud, puntos[i + 1].latitud, puntos[i + 1].longitud
        response = get_directions_response(lat1, lon1, lat2, lon2, mode='drive')
        responses.append(response)

    for response in responses:
        mls = response.json()['features'][0]['geometry']['coordinates']
        points = [(i[1], i[0]) for i in mls[0]]
        folium.PolyLine(points, weight=5, opacity=1).add_to(m)
    # añadir un marcador al mapa por cada punto
    for punto in puntos:
        coordenadas = (punto.latitud, punto.longitud)
        folium.Marker(coordenadas).add_to(m)

    context = {'map': m._repr_html_()}
    return render(request, 'index.html', context)"""
    
def Ruta2A(request):
    return render(request, 'mapasRutas\Ruta2A.html')