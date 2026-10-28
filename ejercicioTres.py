#Ejercicio 3
 
numero = int(input("Digite un numero (0 o negativo para terminar): "))
 
while numero > 0:
 
    # contar los digitos
    cantidad = 0
    aux = numero
    while aux > 0:
        aux = aux // 10
        cantidad = cantidad + 1
 
    # sumar cada digito elevado a la cantidad de digitos
    suma = 0
    texto = ""
    numero_texto = str(numero)
    for digito in numero_texto:
        suma = suma + int(digito) ** cantidad
        if texto == "":
            texto = digito + "^" + str(cantidad)
        else:
            texto = texto + " + " + digito + "^" + str(cantidad)
 
    if suma == numero:
        print(numero, "es narcisista (" + texto + " = " + str(suma) + ")")
    else:
        print(numero, "no es narcisista (" + texto + " = " + str(suma) + ")")
 
    numero = int(input("Digite un numero (0 o negativo para terminar): "))
 
print("Fin del programa")
 