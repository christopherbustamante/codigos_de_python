import random


def generar_contrasena(num_carac):
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '(', ')',',', ':', '.', '>', '<', ';', '&', '$', '#', '"']

    caracteres = mayusculas + minusculas + numeros + simbolos #suma a todas las listas en un una lista única

    contrasena = [] #genera una lista vacía

    for i in range (num_carac):
        caracter_random = random.choice(caracteres) # genera un caracter aleatorio
        contrasena.append(caracter_random) #ingresa el caracter al final de lista

    contrasena = "".join(contrasena) #genera un string de la lista orginal
    return contrasena

def run():
    num_carac = int(input("ingrese la cantidad de caracteres que desea en la contraseña: "))
    contrasena = generar_contrasena(num_carac)
    print("Tu nueva contraseña es: " +  contrasena)


if __name__ == "__main__":
    run()