
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
            ordenar_votos_mañana(matriz)
            print("\nVotos ordenados por turno mañana.")
        elif opcion == 4:
            listas_5_porciento(matriz)
        elif opcion == 5:
            turnos_mas_votados(matriz)
        elif opcion == 6:
            if verificar_ballotage(matriz):
                print("\nHabrá segunda vuelta.")
            else:
                print("\nNo se necesita segunda vuelta.")
        elif opcion == 7:
            print("Pendiente para programar la segunda vuelta")
        elif opcion == 8:
            print("¡¡¡Gracias por participar!!! \n ")
            break

menu()
