print("📋 Formulario de Registro")

# Solicitar datos al usuario
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuál es tu altura en metros? (Ej: 1.65) "))
tiene_mascota = input("¿Tienes mascota? (sí/no): ").lower() == "sí"

# Mostrar resumen
print("\n🧾 Resumen del formulario:")
print(f"Nombre: {nombre} (tipo: {type(nombre).__name__})")
print(f"Edad: {edad} (tipo: {type(edad).__name__})")
print(f"Altura: {altura} m (tipo: {type(altura).__name__})")
print(f"Tiene mascota: {tiene_mascota} (tipo: {type(tiene_mascota).__name__})")
