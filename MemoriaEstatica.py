# Programa en Python equivalente al de Java (MemoriaEstatica)

# Declarar una lista vacía para almacenar 5 calificaciones
calificaciones = []

# Ciclo para pedir las 5 calificaciones
for i in range(5):
    # Pedir dato al usuario y convertir a entero
    calificacion = int(input(f"Captura la calificación {i+1}: "))
    calificaciones.append(calificacion)

# Mostrar las calificaciones capturadas
print("\nLas calificaciones capturadas son:")
for i, cal in enumerate(calificaciones, start=1):
    print(f"Calificación {i}: {cal}")
