from Funciones import * 

def main():
    estados=api_estado()
    climas=api_climas()
    paises=api_paises(estados,climas)
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
                        if opc not in range (1,6):
                            raise Exception
                        

                        if opc == 1:
                            mostrar_paises(paises)
                            
                        elif opc == 2:
                            while True:
                                try:
                                    opc = escogencia_paises(paises) 
                                    break
                                except:
                                    print('\nPor favor ingrese únicamente números enteros entre 1 y 10\n')
                            
                            for pais in paises:
                                if pais.nombre == opc:
                                    pais.mostrar_info()
                        elif opc == 3:
                            while True:
                                try:
                                    opc = escogencia_paises(paises) 
                                    break
                                except:
                                    print('\nPor favor ingrese únicamente números enteros entre 1 y 10\n')
                            print(f'\n--------INFORMACIÓN DE LOS ESTADOS DE {opc.upper()}--------')
                            for estado in estados:
                                if estado.nombre_pais == opc:
                                    
                                    estado.mostrar_info_estado()
                        elif opc == 4:
                            while True:
                                try:
                                    opc = escogencia_paises(paises) 
                                    break
                                except:
                                    print('\nPor favor ingrese únicamente números enteros entre 1 y 10\n')
                            print(f'\n--------INFORMACIÓN CLIMÁTICA PARA {opc.upper()}--------')
                            for clima in climas:
                                if clima.nombre_pais== opc:
                                    clima.mostrar_info_clima()
                        elif opc == 5:
                            break
                       
                        
                except:
                    print('\nPor favor seleccione un número entero entre 1 y 5')
        elif opcion == 2:
            while True:
                try:
                        print('\n-----------------------------------')
                        print("Por favor, seleccione una opción:")
                        print("1. Análisis de superficie y población de los países")
                        print("2. Análisis de superficie y población de los estados")
                        print("3. Análisis de idiomas")
                        print("4. Análisis estadístico de datos meteorológicos")
                        print("5. Volver")
                        opc=int(input('\nSeleccione una opción: '))
                        
                        if opc == 1:
                            mayor_y_menor_superficie_poblacion(paises)
                        elif opc == 2:
                            while True:
                                try:
                                    pais_seleccionado = escogencia_paises(paises)
                                    break
                                except:
                                    print('\nPor favor ingrese únicamente números enteros entre 1 y 10\n')
                                    
                            estado_seleccionado = None
                            for estado in estados:
                                if estado.nombre_pais == pais_seleccionado:
                                    estado_seleccionado = estado
                                    break
                            if estado_seleccionado is None:
                                print(f"No se encontraron estados para el país {pais_seleccionado}")
                            else:
                                estado_mayor_y_menor_superficie_poblacion(estados, estado_seleccionado)
                        elif opc == 3:
                            print(f'\n\t-----------LISTA DE IDIOMAS EN EL SISTEMA-------------')
                            idiomas(paises)
                        elif opc == 4:
                            while True:
                                try:
                                    pais_seleccionado=escogencia_paises(paises)
                                    break
                                except:
                                    print('\nPor favor ingrese únicamente números enteros entre 1 y 10\n')
                            analisis_estadistico(climas, pais_seleccionado)
                        elif opc == 5:
                            break
                        else:
                            raise Exception
                        
                except:
                    print('\nPor favor seleccione un número entero entre 1 y 5')
                    
        elif opcion == 3:
            while True:
                try:
                    opc = int(input('Presione 0 para filtrar por poblacion o 1 para filtrar por area: '))
                    if opc not in range(0,2):
                        raise Exception
                    break
                except:
                    print('\nPor favor ingrese una opcion valida')
            if opc == 0:
                filtro_poblacion(paises)
            elif opc == 1:
                filtro_superficie(paises)
        
        elif opcion == 4:
            print ("modulo4")
            
            
        elif opcion == 5:
            print('\nHasta pronto!\n\n')
            break
                
main()