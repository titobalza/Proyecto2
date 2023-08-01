class Clima:
    def __init__(self, nombre_pais,temperatura,humedad,viento,fecha):
        self.nombre_pais = nombre_pais
        self.temperatura = temperatura
        self.humedad = humedad    
        self.viento= viento
        self.fecha = fecha
        
    def mostrar_info_clima(self):
        print(f'\nTemperatura: {self.temperatura} °C \nHumedad: {round(self.humedad*100, 2)}%\nVelocidad del viento: {self.viento}Km/h\nFecha: {self.fecha}')