"""
1.- Realiza una función llamada area_rectangulo(base, altura) que devuelva el área
del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de
15 de base y 10 de altura.
"""

altura = 10
base = 15

def area_rectangulo(b, a):
    area = int(altura*base)
    return area

print(f"El triangulo cuya base es de {base} y altura es:{altura} tiene un area de: ", area_rectangulo(altura, base))
