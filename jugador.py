from jugadas import PIEDRA, PAPEL, TIJERA

def leer_baraja(tamano:int) -> list:
    contador = 0
    baraja = []
    while contador < tamano:
        print("1. PIEDRA",PIEDRA)
        print("2. PAPEL:",PAPEL)
        print("3. TIJERA",TIJERA)
        eleccion = int(input("Elija su baraja, coloque el número que corresponda a la opción que desea: "))
        if eleccion == 1:
            baraja.append(PIEDRA)
            contador += 1
        elif eleccion == 2:
            baraja.append(PAPEL)
            contador += 1
        elif eleccion == 3:
            baraja.append(TIJERA)
            contador += 1
        else: 
            print("Digite un valor válido")
    return baraja

def leer_jugada(baraja:list) -> str:
    pass