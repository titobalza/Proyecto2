from Funciones import * 
def menu():
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

def main():
    while True:
        opcion= menu()
        if opcion == 1:
            while True:
                try:
                        print('\n-----------------------------------')
                        print("Por favor, seleccione una opción:")
                        print("1. Mostrar países")
                        print("2. Mostrar información para un país")
                        print("3. Mostrar estados de un país")
                        print("4. Mostrar datos meteorológicos de un país")
                        print("5. Volver")
                        opc=int(input('\nSeleccione una opción: '))
                        estados=api_estado()
                        climas=api_climas()
                        paises=api_paises(estados,climas)
                        

                        if opc == 1:
                            mostrar_paises(paises)
                            
                        elif opc == 2:
                            opc= ''
                            while True:
                                try:
                                    mostrar_paises(paises)
                                    opc=int(input("\nIntroduzca el número del país que quiera seleccionar: "))
                                    if opc == 1:
                                        opc="Argentina"
                                    elif opc == 2:
                                        opc="Bolivia"
                                    elif opc == 3:
                                        opc="Brazil"
                                    elif opc == 4:
                                        opc="Canada"
                                    elif opc == 5:
                                        opc="Chile"
                                    elif opc == 6:
                                        opc='Colombia'
                                    elif opc == 7:
                                        opc="Mexico"
                                    elif opc == 8:
                                        opc="Peru"
                                    elif opc == 9:
                                        opc="United States"
                                    elif opc == 10:
                                        opc="Venezuela"
                                    
                                    else:
                                        raise Exception
                                    
                                    break
                                except:
                                    print('Por favor ingrese únicamente números enteros entre 1 y 10')
                            for pais in paises:
                                if pais.nombre == opc:
                                    pais.mostrar_info()
                        elif opc == 3:
                            opc= ''
                            while True:
                                try:
                                    mostrar_paises(paises)
                                    opc=int(input("introduzca el número del país que quiera seleccionar "))
                                    if opc == 1:
                                        opc="Argentina"
                                    elif opc == 2:
                                        opc="Bolivia"
                                    elif opc == 3:
                                        opc="Brazil"
                                    elif opc == 4:
                                        opc="Canada"
                                    elif opc == 5:
                                        opc="Chile"
                                    elif opc == 6:
                                        opc='Colombia'
                                    elif opc == 7:
                                        opc="Mexico"
                                    elif opc == 8:
                                        opc="Peru"
                                    elif opc == 9:
                                        opc="United States"
                                    elif opc == 10:
                                        opc="Venezuela"
                                    
                                    else:
                                        raise Exception
                                    
                                    break
                                except:
                                    print('\nPor favor ingrese únicamente números enteros entre 1 y 10\n')
                            print(f'\n--------INFORMACIÓN DE LOS ESTADOS DE {opc.upper()}--------')
                            for estado in estados:
                                if estado.nombre_pais == opc:
                                    
                                    estado.mostrar_info_estado()
                        elif opc == 4:
                            opc= ''
                            while True:
                                try:
                                    mostrar_paises(paises)
                                    opc=int(input("\nIntroduzca el número del país que quiera seleccionar: "))
                                    if opc == 1:
                                        opc="Argentina"
                                    elif opc == 2:
                                        opc="Bolivia"
                                    elif opc == 3:
                                        opc="Brazil"
                                    elif opc == 4:
                                        opc="Canada"
                                    elif opc == 5:
                                        opc="Chile"
                                    elif opc == 6:
                                        opc='Colombia'
                                    elif opc == 7:
                                        opc="Mexico"
                                    elif opc == 8:
                                        opc="Peru"
                                    elif opc == 9:
                                        opc="United States"
                                    elif opc == 10:
                                        opc="Venezuela"
                                    
                                    else:
                                        raise Exception
                                    
                                    break
                                except:
                                    print('\nPor favor ingrese únicamente números enteros entre 1 y 10: ')
                            print(f'\n--------INFORMACIÓN CLIMÁTICA PARA {opc.upper()}--------')
                            for clima in climas:
                                if clima.nombre_pais== opc:
                                    clima.mostrar_info_clima()
                        elif opc == 5:
                            break
                        else:
                            raise Exception
                        
                except:
                    print('\nPor favor seleccione un número entero entre 1 y 5')
                    
        elif opcion == 5:
            print('\nHasta pronto!\n\n')
            break
                
main()