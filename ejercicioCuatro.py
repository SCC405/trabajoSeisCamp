#Ejercicio 4
 
inicio = int(input("Rango inicial: "))
fin = int(input("Rango final: "))
 
lista = ""
x = inicio
while x <= fin:
 
    suma = 0
    d = 1
    while d < x:
        if x % d == 0:
            suma = suma + d
        d = d + 1
 
    if suma > x:
        if lista == "":
            lista = str(x)
        else:
            lista = lista + ", " + str(x)
 
    x = x + 1
 
if lista == "":
    print("No hay numeros abundantes entre", inicio, "y", fin)
else:
    print("Los numeros abundantes entre [" + str(inicio) + " y " + str(fin) + "] son:", lista)