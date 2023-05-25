import requests

def get_directions_response(lat1, lon1, lat2, lon2, mode='drive'):
   url = "https://route-and-directions.p.rapidapi.com/v1/routing"
   key = "af5aa41a26msh74b47a47e88330cp111409jsndc7d574188df"
   host = "route-and-directions.p.rapidapi.com"
   headers = {"X-RapidAPI-Key": key, "X-RapidAPI-Host": host}
   querystring = {"waypoints":f"{str(lat1)},{str(lon1)}|{str(lat2)},{str(lon2)}","mode":mode}
   response = requests.request("GET", url, headers=headers, params=querystring)
   return response