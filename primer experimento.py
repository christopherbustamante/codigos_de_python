def run():

    contador = 0

    limite = input("De un nombre")
    
    
    while contador < limite:
        if limite == 'o':
            break
        contador = contador + 1
        print(contador)
       

if __name__ == '__main__':
    run()