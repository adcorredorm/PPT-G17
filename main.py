PIEDRA = '🪨'
PAPEL = '🍃'
TIJERA = '✀'

def instrucciones(rondas:int):
    pass

def leer_baraja(tamano:int) -> list:
    pass

def baraja_oponente(tamano:int) -> list:
    pass

def leer_jugada(baraja:list) -> str:
    pass

def jugada_oponente(baraja:list) -> str:
    pass

def jugar(j1:str, j2:str) -> int:
    """Esta funcion retorna
    - 0 si es empate
    - 1 si gano el jugador 1
    - 2 si gano el jugador 2
    """
    pass

def imprimir_ganador(j1:int, j2:int):
    pass


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
        
        i += 1

    imprimir_ganador(contador1, contador2)

main()