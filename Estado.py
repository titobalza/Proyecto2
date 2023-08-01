class Estado:
    def __init__(self, nombre_pais,nombre,capital,poblacion,area):
        self.nombre_pais = nombre_pais
        self.nombre = nombre
        self.capital = capital
        self.poblacion = poblacion
        self.area = area
        
    def mostrar_info_estado(self):
        print(f'\nEstado: {self.nombre}\nCapital del estado: {self.capital}\nPoblación del estado: {self.poblacion}\nArea: {self.area}')