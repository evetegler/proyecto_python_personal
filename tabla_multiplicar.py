print("📊 Generador de Tabla de Multiplicar")

numero = int(input("Ingresa un número entero: "))

print(f"\nTabla del {numero}:")
for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
