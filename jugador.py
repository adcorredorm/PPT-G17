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

def modificar_baraja(baraja:list, valor:str) -> bool:
    for i in range(len(baraja)):
        if baraja[i] == valor:
            baraja[i] = ' '
            return True
    return False

def leer_jugada(baraja:list) -> str:
    eleccion = 0
    opcion = 0
    a = 0

    while a == 0:
        a = 1
        print("Esta es la baraja que tiene: ", baraja)
        print("Elija la opccion:")
        print("1. ",PIEDRA)
        print("2. ",PAPEL)
        print("3. ",TIJERA)
        opcion = int(input())
    
        if opcion == 1 and modificar_baraja(baraja, PIEDRA):
            eleccion = PIEDRA
        elif opcion == 2 and modificar_baraja(baraja, PAPEL):
            eleccion = PAPEL
        elif opcion == 3 and modificar_baraja(baraja, TIJERA):
            eleccion = TIJERA
        elif 1 <= opcion <= 3:
            print("Usted no posee una carta con el valor seleccionado, porfavor elija de nuevo")
            a = 0
        else:
            print("La opcion introducida no es valida, vuelva a ingresar: ")
            a = 0
    return eleccion

if __name__ == "__main__":
    baraja = [PAPEL, PAPEL, PAPEL, PIEDRA, TIJERA]
    print(baraja)
    modificar_baraja(baraja, PAPEL)
    print(baraja)
