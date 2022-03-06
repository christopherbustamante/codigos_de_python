menu = """
Bienvenido al conversor de moneda 💰
1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Nicaraguenses

Elige una opcion: 
"""
opcion = input(menu)

def calcular(tipo_pesos, valor_dolar):
    pesos = input ("Cuantos Pesos" + tipo_pesos +" Tienes ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ "+ dolares + "Dolares")



if opcion == '1':
    calcular("Colombianos", 3875)
# --------------------------------------------------------------------
elif opcion == '2':
    calcular("Argentinos", 65)
# --------------------------------------------------------------------
elif opcion == '3':
    calcular("Nicaraguenses", 35)
# --------------------------------------------------------------------
else:
    print("Ingrese una opcion Correcta")
