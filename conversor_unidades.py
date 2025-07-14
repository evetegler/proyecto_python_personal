def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def pesos_a_dolares(pesos, tasa):
    return pesos / tasa

def dolares_a_pesos(dolares, tasa):
    return dolares * tasa

def metros_a_kilometros(m):
    return m / 1000

def kilometros_a_metros(km):
    return km * 1000

print("Bienvenido al conversor de unidades 🌐")
print("1. Temperatura")
print("2. Moneda")
print("3. Longitud")
opcion = input("Selecciona una opción (1-3): ")

if opcion == "1":
    print("\n-- Conversor de Temperatura --")
    sub_opcion = input("Escribe 'C' para Celsius a Fahrenheit o 'F' para Fahrenheit a Celsius: ").upper()
    valor = float(input("Ingresa el valor a convertir: "))
    if sub_opcion == "C":
        print(f"{valor}°C = {celsius_a_fahrenheit(valor):.2f}°F")
    elif sub_opcion == "F":
        print(f"{valor}°F = {fahrenheit_a_celsius(valor):.2f}°C")
    else:
        print("Opción no válida.")

elif opcion == "2":
    print("\n-- Conversor de Moneda --")
    tasa = float(input("Ingresa el valor del dólar en CLP (ej: 950): "))
    sub_opcion = input("Escribe 'P' para Pesos a Dólares o 'D' para Dólares a Pesos: ").upper()
    valor = float(input("Ingresa el valor a convertir: "))
    if sub_opcion == "P":
        print(f"{valor} CLP = ${pesos_a_dolares(valor, tasa):.2f} USD")
    elif sub_opcion == "D":
        print(f"${valor} USD = {dolares_a_pesos(valor, tasa):.2f} CLP")
    else:
        print("Opción no válida.")

elif opcion == "3":
    print("\n-- Conversor de Longitud --")
    sub_opcion = input("Escribe 'M' para Metros a Kilómetros o 'K' para Kilómetros a Metros: ").upper()
    valor = float(input("Ingresa el valor a convertir: "))
    if sub_opcion == "M":
        print(f"{valor} m = {metros_a_kilometros(valor):.3f} km")
    elif sub_opcion == "K":
        print(f"{valor} km = {kilometros_a_metros(valor):.2f} m")
    else:
        print("Opción no válida.")
else:
    print("Selección inválida. Intenta nuevamente.")
