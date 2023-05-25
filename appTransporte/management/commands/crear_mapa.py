import folium
from appTransporte.models import puntosGPS
from django.core.management.base import BaseCommand
import requests
#from appTransporte.funtions import get_directions_response
# Create your views here.

def get_directions_response(lat1, lon1, lat2, lon2, mode='drive'):
        url = "https://route-and-directions.p.rapidapi.com/v1/routing"
        key = "af5aa41a26msh74b47a47e88330cp111409jsndc7d574188df"
        host = "route-and-directions.p.rapidapi.com"
        headers = {"X-RapidAPI-Key": key, "X-RapidAPI-Host": host}
        querystring = {"waypoints":f"{str(lat1)},{str(lon1)}|{str(lat2)},{str(lon2)}","mode":mode}
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        puntos = puntosGPS.objects.all()

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

        m.save('appTransporte\\templates\mapasRutas\Ruta2A2.html')
    