def run():
    LIMITE = 1000

    contador = 0
    potenia_2 = 2**contador

    while potenia_2 < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a:" + str(potenia_2))
        contador = contador + 1
        potenia_2 = 2**contador


if __name__ == '__main__':
    run()