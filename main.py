print("Que pasa chavales todo bien todo correcto y yo que me alegro. Bienvenidos al mejor Gestor de Tareas.")

tarea = input("Escribe una nueva tarea: ")
with open("tareas.txt", "a") as archivo:
    archivo.write(tarea + "\n")
    print("Tarea guardada.")