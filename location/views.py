from django.shortcuts import render
import requests
import folium
import json

def location(request):
    response = requests.get('https://urbe.me/administracao/api/lista-projetos/').json()
    coord = [-15.793889, -47.882772]
    map = folium.Map(location=coord, zoom_start = 5, height='100%')

    json_response = json.dumps(response, indent = 8)
    jsonformatted = json.loads(json_response)
    for i in jsonformatted:
        latitude = i['latitude']
        longitude = i['longitude']
        titulo = i['projeto']
        if latitude == None or longitude == None:
            latitude = 0
            longitude = 0
        position = [latitude, longitude]
        if position == [0,0]:
            titulo = titulo + '- Sem localização'
        folium.Marker(position, popup=titulo).add_to(map)
    map.save('map.html')
    context = {'my_map': map._repr_html_()}
    return render(request, 'location.html', context)
