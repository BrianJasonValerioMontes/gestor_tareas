print("Que pasa chavales todo bien todo correcto y yo que me alegro. Bienvenidos al mejor Gestor de Tareas.")

print("\nTus tareas:")
with open("tareas.txt", "r") as archivo:
    print(archivo.read())