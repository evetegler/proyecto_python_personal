print("🧮 Calculadora de Factorial")

numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("❌ El factorial no está definido para números negativos.")
elif numero == 0:
    print("0! = 1")
else:
    resultado = 1
    contador = 1
    while contador <= numero:
        resultado *= contador
        contador += 1
    print(f"{numero}! = {resultado}")