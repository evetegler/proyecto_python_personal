import math

def area_cuadrado(lado):
    return lado * lado

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * radio ** 2

print("📏 Calculadora de Áreas")

while True:
    print("\nFiguras disponibles:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        lado = float(input("Ingresa el lado del cuadrado: "))
        print(f"Área del cuadrado: {area_cuadrado(lado):.2f} unidades²")

    elif opcion == "2":
        base = float(input("Base del rectángulo: "))
        altura = float(input("Altura del rectángulo: "))
        print(f"Área del rectángulo: {area_rectangulo(base, altura):.2f} unidades²")

    elif opcion == "3":
        base = float(input("Base del triángulo: "))
        altura = float(input("Altura del triángulo: "))
        print(f"Área del triángulo: {area_triangulo(base, altura):.2f} unidades²")

    elif opcion == "4":
        radio = float(input("Radio del círculo: "))
        print(f"Área del círculo: {area_circulo(radio):.2f} unidades²")

    elif opcion == "5":
        print("👋 Cerrando calculadora...")
        break
    else:
        print("⚠️ Opción no válida.")
