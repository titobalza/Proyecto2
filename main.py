from Funciones import * 

def main():
    estados = api_estado()
    climas = api_climas()
    
    paises = api_paises(estados,climas)
    
    for pais in paises:
        if pais.nombre == 'Venezuela':
            pais.mostrar_info()
            
    mostrar_paises(paises)
    
    
    
main()