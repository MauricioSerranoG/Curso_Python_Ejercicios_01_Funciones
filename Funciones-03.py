"""
3. - Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo
siguiente (Quizá debas adelantarte un poco al uso de condiciones básicas):

● Si el primer número es mayor que el segundo, debe devolver 1.
● Si el primer número es menor que el segundo, debe devolver -1.
● Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.

"""
#Relacion de numeros 5 y 10
num1 = 5
num2 = 10

def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0

print(f"Numero A: {num1}, Numero B: {num2}, Relación es... ", relacion(num1, num2), end = "\n")

#Relacion de numeros 10 y 5
num1 = 10
num2 = 5

print(f"Numero A: {num1}, Numero B: {num2}, Relación es... ", relacion(num1, num2), end = "\n")

#Relacion de numeros 5 y 5
num1 = 5
num2 = 5

print(f"Numero A: {num1}, Numero B: {num2}, Relación es... ", relacion(num1, num2), end = "\n")
