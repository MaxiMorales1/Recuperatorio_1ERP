
#Morales Máximo - Turno Mañana - Div. 114

#1ER PARCIAL - Recuperatorio 

#Programa UTNFRA (Votos de Presidente o Partido) - Main - Menu Sistema

from DesarolloMorales import *

def menu():
    
    matriz = []

    while True:
        print ("+------Bienvenido al programa de votos UTNFRA------+")
        print ("\n 1: CARGAR VOTOS \n 2: MOSTRAR VOTOS \n 3: ORDENAR VOTOS TM \n 4: VOTOS MINIMOS \n 5: TURNO MAS VOTADO \n 6: BALLOTAGE \n 7: SEGUNDA VUELTA \n 8: SALIR \n")
        opcion = entradas_menu ("Su opción: ","Error, ingrese opción válida.\nSu opción:",1,8)

        if opcion == 1:
            matriz = cargar_votos()
        elif opcion == 2:
            mostrar_votos(matriz)
        elif opcion == 3:
            print("\nPendiente para programar orden turno mañana.\n")
        elif opcion == 4:
            listas_5_porciento(matriz)
        elif opcion == 5:
            turnos_mas_votados(matriz)
        elif opcion == 6:
            if verificar_ballotage(matriz):
                print("\nHabrá segunda vuelta.\n")
            else:
                print("\nNo se necesita segunda vuelta.\n")
        elif opcion == 7:
            print("\nPendiente para programar la segunda vuelta.\n")
        elif opcion == 8:
            print("\n¡¡¡Gracias por participar!!!\n ")
            break

menu()
