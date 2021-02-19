"""
2.- Realiza una función llamada area_circulo(radio) que devuelva el área de un
círculo a partir de un radio. Calcula el área de un círculo de 5 de radio.
"""
r = 5
pi = float(3.1416)

def a_circulo(radio, p):
     a = pi*r**2
     return a
print(f"pi = {pi} y el radio es = {r}, por lo tanto el area del circulo es: {a_circulo(r, pi)}")
