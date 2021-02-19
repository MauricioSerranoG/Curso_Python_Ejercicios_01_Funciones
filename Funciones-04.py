"""
4.- Realiza una función llamada intermedio(a, b) que a partir de dos números,
devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio
entre -12 y 24:
Pista: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
"""


n1 = 2
n2 = 8
inter = 0
def intermedio(a, b):
    inter = (n1 +n2)/2
    return inter


print(f"El numero intermedio de los numeros {n1} y {n2}, es: ", intermedio(n1, n2)) 