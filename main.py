from jugadas import PIEDRA, PAPEL, TIJERA
from jugador import *
from oponente import *

def instrucciones(rondas:int):
    print("Aca irian las instrucciones del juego")
    print()
    print()

def jerarquia(j1:str, j2:str) -> bool:
    """ retorna si el jugador 1 es el ganador """
    return (j1 == PIEDRA and j2 == TIJERA) or (j1 == PAPEL and j2 == PIEDRA) or (j1 == TIJERA and j2 == PAPEL)

def jugar(j1:str, j2:str) -> int:
    """Esta funcion retorna
    - 0 si es empate
    - 1 si gano el jugador 1
    - 2 si gano el jugador 2
    """
    print("Usted jugó", j1)
    print("Su oponente jugó", j2)

    if j1 == j2:
        return 0
    elif jerarquia(j1, j2):
        return 1
    elif jerarquia(j2, j1):
        return 2
    else:
        print ("Error, verifique sus jugadas.")

def imprimir_ganador(contador1:int, contador2:int):
    if contador1 < contador2:
        return print("¡Ha ganado el jugador 2!")
    elif contador1 > contador2:
        return print("¡Ha ganado el jugador 1!")
    elif contador1 == contador2:
        return print("¡Empate!")


def main():
    num_rondas = 5
    contador1 = 0
    contador2 = 0

    instrucciones(num_rondas)

    b_jugador:list = leer_baraja(num_rondas)
    b_oponente:list = baraja_oponente(num_rondas)

    i = 1
    while i <= num_rondas:
        print("Inicia la ronda", i)

        jugada1:str = leer_jugada(b_jugador)
        jugada2:str = jugada_oponente(b_oponente)

        resultado:int = jugar(jugada1, jugada2)

        if resultado == 1:
            contador1 += 1
        elif resultado == 2:
            contador2 += 1
        
        print("El jugador 1 tiene", contador1, "puntos")
        print("El jugador 2 tiene", contador2, "puntos")

        i += 1

    imprimir_ganador(contador1, contador2)

main()
