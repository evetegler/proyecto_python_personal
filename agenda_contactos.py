print("📞 Agenda de Contactos")

agenda = {}  # Diccionario vacío

while True:
    print("\nMenú:")
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar contacto")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ").capitalize()
        telefono = input("Número de teléfono: ")
        agenda[nombre] = telefono
        print(f"✅ Contacto '{nombre}' agregado.")
    
    elif opcion == "2":
        if agenda:
            print("\n📇 Lista de contactos:")
            for nombre, telefono in agenda.items():
                print(f"- {nombre}: {telefono}")
        else:
            print("📭 No hay contactos registrados.")
    
    elif opcion == "3":
        buscar = input("Ingresa el nombre del contacto a buscar: ").capitalize()
        if buscar in agenda:
            print(f"📌 {buscar}: {agenda[buscar]}")
        else:
            print("❌ Contacto no encontrado.")
    
    elif opcion == "4":
        print("👋 Cerrando agenda...")
        break
    else:
        print("⚠️ Opción no válida.")
