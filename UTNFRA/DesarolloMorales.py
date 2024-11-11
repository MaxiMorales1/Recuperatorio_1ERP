
#Morales Máximo - Turno Mañana - Div. 114

#1ER PARCIAL - Recuperatorio 

#Programa UTNFRA (Votos de Presidente o Partido) - Desarrollo

import random
listas_politicas = 5
listas_turnos = ["MAÑANA" , "TARDE" , "NOCHE"]

def entradas_menu (mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    """_summary_
    Args:
        mensaje (str): _description_
        mensaje_error (str): _description_
        minimo (int): _description_
        maximo (int): _description_
    Returns:
        int: _description_
    """
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje_error))

    return numero

# Función para cargar los votos secuencialmente.
def cargar_votos():
    matriz = []
    for i in range(listas_politicas):
        print(f"\nIngresos para Politico Nº{i + 1}")
        # Validación de número de lista.
        while True:
            nro_lista = int(input("Número de lista: "))
            if 99 <= nro_lista <= 999:
                break
            print("Error, (debe ser positivo y de tres cifras).")
        # Sección para ingresar los votos por turno.
        votos = []
        for turno in listas_turnos:
            while True:
                voto = int(input(f"Ingreso votos turno {turno}: "))
                if voto >= 0:
                    votos.append(voto)
                    break
                print("Error, deben ser positivos.")
        
        matriz.append([nro_lista] + votos)
    return matriz

# Función para calcular el porcentaje de votos de cada lista.
def calcular_porcentajes(matriz):
    total_votos = sum(sum(lista[1:]) for lista in matriz)
    porcentajes = []
    for lista in matriz:
        votos_lista = sum(lista[1:])
        porcentaje = (votos_lista / total_votos * 100) if total_votos > 0 else 0
        porcentajes.append(porcentaje)
    return porcentajes

# Función para mostrar los votos.
def mostrar_votos(matriz):
    porcentajes = calcular_porcentajes(matriz)
    print("\nNro Lista | Mañana | Tarde | Noche | Porcentaje Total \n")
    for i in range(len(matriz)):
        lista = matriz[i]
        print(f"{lista[0]:<10} {lista[1]:<8} {lista[2]:<7} {lista[3]:<6} {porcentajes[i]:.2f}% \n")

# Función para ordenar la matriz según los votos del turno mañana
def ordenar_votos_mañana(matriz: list, indice: int) -> list:
    for i in range(len(matriz) - 1):
        for j in range(i + 1, len(matriz)):
            if matriz[i][indice] < matriz[j][indice]:
                # Intercambia las filas si el elemento en la columna `indice` de `j` es mayor
                aux = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = aux
    return matriz

# Función para mostrar las listas con menos del 5% de los votos totales
def listas_5_porciento(matriz):
    porcentajes = calcular_porcentajes(matriz)
    print("\nListas con pocos votos: \n")
    for i in range(len(porcentajes)):
        porcentaje = porcentajes[i]
        if porcentaje < 5:
            print(f"Lista {matriz[i][0]} con {porcentaje:.2f}% del total de votos \n")

# Función para mostrar el turno con más votos
def turnos_mas_votados(matriz):
    total_votos_turno = [sum(lista[i + 1] for lista in matriz) for i in range(len(listas_turnos))]
    max_votos = max(total_votos_turno)
    turnos_mas_votados = []
    
    for i in range(len(total_votos_turno)):
        if total_votos_turno[i] == max_votos:
            turnos_mas_votados.append(listas_turnos[i])
    
    print("\nTurno(s) con más votos:")
    for turno in turnos_mas_votados:
        print(turno)

# Función para verificar si hay ballotage
def verificar_ballotage(matriz):
    porcentajes = calcular_porcentajes(matriz)
    return not any(porcentaje > 50 for porcentaje in porcentajes)

# Función para realizar la segunda vuelta

