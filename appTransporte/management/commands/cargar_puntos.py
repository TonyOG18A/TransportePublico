import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from appTransporte.models import puntosGPS

class Command(BaseCommand):
    ayuda = "Cargar datos desde archivo csv"

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / 'data' / 'Ruta2A.csv'
        keys = ('WKT', 'Nombre')

        records = []
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append({k: row[k] for k in keys})
               # records.append(row['WKT'])
                #print(row['WKT'])
        
        # extraer latitud y longitud del objeto punto
        for record in records:
            print(record['WKT'].split("(")[-1].split(")")[0].split())
    
            longitud, latitud = record['WKT'].split("(")[-1].split(")")[0].split()
            record['longitud'] = float(longitud)
            record['latitud'] = float(latitud)

            # añadir datos a la base de datos
            puntosGPS.objects.get_or_create(
                latitud = record['latitud'],
                longitud = record['longitud']
            )
