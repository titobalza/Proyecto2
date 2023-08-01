import requests
from Estado import *
from Clima import *
from Pais import *

def api_estado():
    estados = []
    datos_api = requests.get('https://raw.githubusercontent.com/Andresarl16/API-Retos/main/location-states-api.json')
    datos = datos_api.json()
    for d in datos:
        for s in d['location_states']:
            x = Estado(d['location_name'], s['state_name'],s['state_capital'],s['population'],s['area'])
            estados.append(x)
    return estados

def api_climas ():
    climas = []
    datos_api = requests.get('https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-api.json')
    datos = datos_api.json()
    for d in datos:
        for s in d['location_measurements']:
            x = Clima(d['location_name'], s['temperature'],s['humidity'],s['wind_speed'],s['date'])
            climas.append(x)
    return climas

def api_paises(estados, climas):
    paises = []
    states=[]
    data=[]
    datos_api = requests.get('https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-data-api.json')
    datos = datos_api.json()   
    for pais in datos:
        for s in estados:
            if s.nombre_pais == pais['location_name']:
                states.append(s)
        for c in climas:
            if c.nombre_pais == pais['location_name']:
                data.append(c)
        x = Pais(pais['location_name'],pais['location_capital'], pais['population'], pais['area'],pais['currency'],pais['main_language'],states, data)        
        paises.append(x)
        states = []
        data= []
        
    return paises

def mostrar_paises(paises):
    print('Lista de paises en el sistema')
    for i, pais in enumerate(paises):
        print(i+1, pais.nombre) 
