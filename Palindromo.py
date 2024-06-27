"""Comprobar si una palabra o frase es palindorma"""

def esPalindromo(palabra):
    #La ruta nos aporto otro paso natural
    #larutanosaportootropasonatural

    palabra = palabra.lower() # la ruta nos aporto otro paso natural
    palabra = palabra.replace (" ","")# larutanosaportootropasonatural
    palabra = palabra.replace("á","a")# larutanosaportootropasonatural
    palabra = palabra.replace ("é","e")# larutanosaportootropasonatural
    palabra = palabra.replace ("í","i")# larutanosaportootropasonatural
    palabra = palabra.replace ("ó","o")# larutanosaportootropasonatural 
    palabra = palabra.replace ("ú","u")# larutanosaportootropasonatural

    # larutanosaportootropasonatural
    #012....
    # n = largo de la frase - 1
    """Ejemplo
    # oso
    # o -> 0
    # s -> 1
    # o -> 2"""

    a = 0
    b = len(palabra) - 1

    for i in range(0, len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else:
            return False
    return True

palabra = input("Ingrese una palabra o una frase: ")

if esPalindromo(palabra):
    print("Es una palabra o frase palíndroma")

else:
    print("No es una palabra o frase palíndroma")