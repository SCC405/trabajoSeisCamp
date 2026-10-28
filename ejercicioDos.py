#Ejercicio 2
 
numero = int(input("Digite un numero (negativo para terminar): "))
 
while numero >= 0:
 
    if numero <= 2:
        print("El numero debe ser mayor que dos")
    else:
        suma = 0
        d = 1
        while d < numero:
            if numero % d == 0:
                suma = suma + d
            d = d + 1
 
        if suma == numero:
            print(numero, "es un numero perfecto")
        else:
            print(numero, "no es un numero perfecto")
 
    numero = int(input("Digite un numero (negativo para terminar): "))
 
print("Fin del programa")
 