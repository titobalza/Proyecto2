class Pais: 
    def __init__(self,nombre ,capital ,poblacion ,area ,moneda,idioma ,estado, clima):
        self.nombre = nombre
        self.capital = capital
        self.poblacion = poblacion
        self.area = area
        self.moneda = moneda
        self.idioma = idioma
        self.estado = estado    
        self.clima = clima
        
    def mostrar_info(self):
        print(f'---------- INFORMACION DE {self.nombre.upper()}---------\n\nCapital: {self.capital}\nPoblacion: {self.poblacion}\nArea: {self.area}\nMoneda: {self.moneda}\nIdioma: {self.idioma}')
        
    