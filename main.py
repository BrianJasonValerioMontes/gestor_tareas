print("Que pasa chavales todo bien todo correcto y yo que me alegro. Bienvenidos al mejor Gestor de Tareas.")

def guardar_tarea():
    tarea = input("Escribe una nueva tarea: ")
    with open("tareas.txt", "a") as archivo:
        archivo.write(tarea + "\n")
    print("Tarea guardada.")

def ver_tareas():
    print("\nTus tareas:")
    try:
        with open("tareas.txt", "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("Aún no hay tareas.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            guardar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

menu()