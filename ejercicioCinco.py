#Ejercicio 5
 
def es_multiplo(numero, divisor):
    if divisor == 0:
        return False
    if numero % divisor == 0:
        return True
    else:
        return False
 
 
a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
 
print(a, "multiplo de", b, ":", es_multiplo(a, b))
print(b, "multiplo de", a, ":", es_multiplo(b, a))