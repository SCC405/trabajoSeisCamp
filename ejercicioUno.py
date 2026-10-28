#Ejercicio 1
 
while True:
 
    temperatura = float(input("Digite la temperatura del sitio de incubacion (°C): "))
 
    if temperatura < 26:
        print("❄️  T. baja")
    elif temperatura <= 34:
        print("✅ T. normal")
    else:
        print("🔥 T. alta")
 
    seguir = int(input("Desea ingresar otra temperatura? (1: si, 2: no) "))
    if seguir == 2:
        break
 
print("Gracias por usar el programa")