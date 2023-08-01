import requests
from Estado import *
from Clima import *
from Pais import *

def api_estado():
    """funcion que convierte el api de estados a una lista de objetos con la infomacion y su nombre

    Returns:
        api_estado(): lista de objetos de la clase estado
    """
    estados = []
    datos_api = requests.get('https://raw.githubusercontent.com/Andresarl16/API-Retos/main/location-states-api.json')
    datos = datos_api.json()
    for d in datos:
        for s in d['location_states']:
            x = Estado(d['location_name'], s['state_name'],s['state_capital'],s['population'],s['area'])
            estados.append(x)
    return estados

def api_climas ():
    """funcion que convierte el api de clima a una lista de objetos con la infomacion y su nombre

    Returns:
        api_climas (): lista de objetos de la clase clima
    """
    climas = []
    datos_api = requests.get('https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-api.json')
    datos = datos_api.json()
    for d in datos:
        for s in d['location_measurements']:
            x = Clima(d['location_name'], s['temperature'],s['humidity'],s['wind_speed'],s['date'])
            climas.append(x)
    return climas

def api_paises(estados, climas):
    """funcion que convierte el api de paises a una lista de objetos con la infomacion, tambien une, la informacion del api de estados y clima

    Returns:
        api_paises(estados, climas): lista de objetos compuestos por la informacion del api y de la clase pais, tambien se puede acceder a clima y estado desde aca
    """
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
    """funcion para mostrar y enumerar la lista de paises

    Args:
        paises (lista): lista de objetos de la clase pais 
    """
    print('\nLista de paises en el sistema')
    for i, pais in enumerate(paises):
        print(f'\t{i+1} {pais.nombre}') 


def escogencia_paises(paises):
    """para escoger uno de los paises de la lista de mostrar_paises

    Args:
        paises (lista): lista de objetos de la clase pais 

    Raises:
        Exception: por si el usuario mete un numero invalido

    Returns:
        string: el pais que escogio el usuario como string ejemplo "Venezuela"
    """
    while True:
        try:
            mostrar_paises(paises)
            opc = int(input("Introduzca el número del país que quiera seleccionar: "))
            nombres_paises = [pais.nombre for pais in paises]
            if opc not in range(1,11):
                raise Exception("El número de opción debe ser un entero entre 1 y 10")
            pais_seleccionado = nombres_paises[opc - 1]
            return pais_seleccionado
        except:
            print('\nPor favor ingrese únicamente números enteros entre 1 y 10\n')
            
def idiomas(paises):
    """imprime los idiomas disponibles en el sistema y cuales paises lo hablan

    Args:
        paises (lista): lista de objetos de la clase pais 
    """
    lenguajes = {}
    for pais in paises:
        if pais.idioma not in lenguajes.keys():
            lenguajes.update({pais.idioma:[pais.nombre]})
        else:
            lenguajes[pais.idioma].append(pais.nombre)
    for k,v in lenguajes.items():
        print(f'\n\t{k.upper()}')
        for x in v:
            print(f'\t\t{x}')
            
            
def calcular_moda(lista):
        """ Args:
            lista (list): Una lista de números.

        Returns:
            float: La moda de la lista. Si hay varias modas, devuelve la primera que encuentre. Si la lista está vacía, devuelve None.
        """
        conteos = {}
        for x in lista:
            if x in conteos:
                conteos[x] += 1
            else:
                conteos[x] = 1
        moda = None
        max_conteo = 0
        for x in conteos:
            if conteos[x] > max_conteo:
                moda = x
                max_conteo = conteos[x]
        return moda
    
def analisis_estadistico(climas, pais_seleccionado):
    """convierte los parametros climaticos en listas, para hacer los analisis, luego imprime los resultados

    Args:
        climas (lista): lista de objetos de la clase clima
        pais_seleccionado (string): es el resultado de escogencia paises
    """
    temperatura = []
    humedades = []
    velocidades = []
    
    for ubicacion in climas:
        if ubicacion.nombre_pais.lower().strip() == pais_seleccionado.lower().strip():
            temperatura.append(ubicacion.temperatura)
            humedades.append(ubicacion.humedad)
            velocidades.append(ubicacion.viento)
            temperaturas = temperatura
            humedad = humedades
            velocidad_viento = velocidades
            moda_temperaturas = calcular_moda(temperaturas)
            moda_humedad = calcular_moda(humedad)
            moda_velocidad_viento=calcular_moda(velocidad_viento)
            
    print(f"\n----------Información meteorológica para {pais_seleccionado}:----------\n")
    print('\nTEMPERATURA')
    print('\tMaximo: ', max(temperatura),"°C")
    print('\tMinimo: ', min(temperatura),"°C")
    print('\tPromedio: ',round(sum(temperatura) / len(temperatura), 2),"°C")
    print('\tModa: ', moda_temperaturas, "°C\n")
    print('\nHUMEDAD')
    print('\tMaximo: ', max(humedades*100 ),"%")
    print('\tMinimo: ', min(humedades*100 ),"%")
    print('\tPromedio: ', round(sum(humedades*100 ) / len(humedades), 2),"%")
    print('\tModa: ', moda_humedad*100, "%\n")
    print('\nVELOCIDAD DE VIENTO')
    print('\tMaximo: ', max(velocidades ), "m/s")
    print('\tMinimo: ', min(velocidades ), "m/s")
    print('\tPromedio: ',round( sum(velocidades ) / len(velocidades), 2), "m/s")
    print('\tModa: ', moda_velocidad_viento, "m/s\n")
    

    
    
def filtro_superficie(paises):
    """filtra la lista de paises y su informacion dependiendo de los parametros del usuario para obtener estados con la extension indicada

    Args:
        paises (lista): lista de objetos de la clase pais 

    Raises:
        Exception: por si el usuario introduce un numero minimo mayor al maximo
    """
    country = escogencia_paises(paises) 
    states = []
    while True:
        try:
            mini = int(input('\nIngrese el menor valor del area de los estados que desee ver: '))
            maxi = int(input('Ingrese el mayor valor del area de los estados que desee ver: '))
            if (mini>maxi):
                raise Exception
            break
        except:
            print('\nPor favor ingrese unicamente numeros enteros y recuerde que el valor minimo no puede ser mayor al valor maximo')
    
    for pais in paises:
        if pais.nombre == country:
            for estado in pais.estado:
                if estado.area in range(mini,maxi+1):
                    states.append(estado)
    
    if len(states) > 0:
        print(f'Estados de {country} con un area entre {mini} y {maxi} kilometros cuadrados')
        for s in states:
            print(f' - {s.nombre}\n\t{s.area} kilometros cuadrados\n')
    else:
        print(f'No existen estados en {country} con un area entre {mini} y {maxi} kilometros cuadrados')
        
def filtro_poblacion(paises):
    """filtra la lista de paises y su informacion dependiendo de los parametros del usuario para conseguir estados con un minimo de poblacion

    Args:
        paises (lista): lista de objetos de la clase pais 
    """
    country = escogencia_paises(paises) 
    states = []
    while True:
        try:
            num = int(input('\nIngrese el menor valor de poblacion de los estados que desee ver: '))
            break
        except:
            print('\nPor favor ingrese unicamente numeros enteros')
    
    for pais in paises:
        if pais.nombre == country:
            for estado in pais.estado:
                if estado.poblacion > num:
                    states.append(estado)
    
    if len(states) > 0:
        print(f'Estados de {country} con una poblacion mayor a {num} habitantes')
        for s in states:
            print(f' - {s.nombre}\n\t{s.poblacion} habitantes\n')
    else:
        print(f'No existen estados en {country} con una poblacion mayor a {num} habitantes')
        
        
        
def mayor_y_menor_superficie_poblacion(paises):
    """consigue los paises con mayor y menor poblacion y superficie,  tambien saca un promedio de estos dos

    Args:
        paises (lista): lista de objetos de la clase pais 
    """
    poblacion = []
    superficie = []
    nombre_pais = []
    for pais in paises:
        superficie.append(pais.area)
        poblacion.append(pais.poblacion)
        nombre_pais.append(pais.nombre)
        
    max_poblacion = max(poblacion)
    min_poblacion = min(poblacion)
    max_superficie = max(superficie)
    min_superficie = min(superficie)
    
    pais_max_poblacion = nombre_pais[poblacion.index(max_poblacion)]
    pais_min_poblacion = nombre_pais[poblacion.index(min_poblacion)]
    pais_max_superficie = nombre_pais[superficie.index(max_superficie)]
    pais_min_superficie = nombre_pais[superficie.index(min_superficie)]
    
    promedio_poblacion = sum(poblacion) / len(poblacion)
    promedio_superficie = sum(superficie) / len(superficie)
    
    print(f"\nPaís con la mayor población: {pais_max_poblacion} ({max_poblacion} habitantes)")
    print(f"\nPaís con la menor población: {pais_min_poblacion} ({min_poblacion} habitantes)")
    print(f"\nPaís con la mayor superficie: {pais_max_superficie} ({max_superficie} km²)")
    print(f"\nPaís con la menor superficie: {pais_min_superficie} ({min_superficie} km²)")
    print(f"\nPromedio de población total: {round(promedio_poblacion, 2)} habitantes")
    print(f"\nPromedio de superficie total: {round(promedio_superficie, 2)} km²")

def estado_mayor_y_menor_superficie_poblacion(estados, estado_seleccionado):
    """saca informacion de los estados de un pais que escoja el usuario

    Args:
        estados (lista): lista de objetos de la clase estado
        estado_seleccionado: son los estados dentro del pais seleccionado por el usuario
    """
    
    poblacion = []
    superficie = []
    nombre_estado = []

    for estado in estados:
        if estado.nombre_pais == estado_seleccionado.nombre_pais:
            superficie.append(estado.area)
            poblacion.append(estado.poblacion)
            nombre_estado.append(estado.nombre)
    
    if len(nombre_estado) == 0:
        print(f"No se encontraron estados para el país {estado_seleccionado.nombre_pais}")
    else:
        max_poblacion = max(poblacion)
        min_poblacion = min(poblacion)
        max_superficie = max(superficie)
        min_superficie = min(superficie)

        estado_max_poblacion = nombre_estado[poblacion.index(max_poblacion)]
        estado_min_poblacion = nombre_estado[poblacion.index(min_poblacion)]
        estado_max_superficie = nombre_estado[superficie.index(max_superficie)]
        estado_min_superficie = nombre_estado[superficie.index(min_superficie)]

        promedio_poblacion = sum(poblacion) / len(poblacion)
        promedio_superficie = sum(superficie) / len(superficie)

        print(f"\nEstado con la menor población: {estado_min_poblacion} ({min_poblacion} habitantes)")
        print(f"\nEstado con la mayor población: {estado_max_poblacion} ({max_poblacion} habitantes)")
        print(f"\nEstado con la mayor superficie: {estado_max_superficie} ({max_superficie} km²)")
        print(f"\nEstado con la menor superficie: {estado_min_superficie} ({min_superficie} km²)")
        print(f"\nPromedio de población total: {round(promedio_poblacion, 2)} habitantes")
        print(f"\nPromedio de superficie total: {round(promedio_superficie, 2)} km²")

def menu():
    """menu para que el usuario elija a que modulo quiere acceder

    Raises:
        Exception: por si no pone un numero entre 1 y 5

    Returns:
        variable: opcion es la variable para luego saber a que modulo se esta accediendo
    """
    print('\nBienvenido al sistema de datos meteorologicos!\n')
    while True:
        try:
            print('\n-----------------------------------')
            print("Por favor, seleccione un módulo:")
            print("1. Módulo de información")
            print("2. Módulo de análisis de datos")
            print("3. Módulo de filtrado de datos")
            print("4. Módulo de busqueda y consulta de datos")
            print("5. Salir")
            opcion = int(input("\nIngrese el número de la opción que desea: "))
            if opcion not in range(1,6):
                raise Exception 
            break   
        except:
            print("Por favor ingrese unicamente numeros enteros entre 1 y 5")
    return opcion 
