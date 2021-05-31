from random import randint
from jugadas import PIEDRA, PAPEL, TIJERA

opciones = [PIEDRA, PAPEL, TIJERA]

def baraja_oponente(tamano:int) -> list:
    baraja = []
    for _ in range(tamano):
        elegida = randint(0, len(opciones) - 1)
        baraja.append(opciones[elegida])
    return baraja

def jugada_oponente(baraja:list) -> str:
    posicion = randint(0, len(baraja) - 1)
    jugada = baraja[posicion]
    baraja.remove(jugada)
    return jugada

if __name__ == "__main__":
    tamano = 5
    baraja = baraja_oponente(tamano)

    for _ in range(tamano):
        print(baraja)
        print(jugada_oponente(baraja))
