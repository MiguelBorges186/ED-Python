meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

departamentos = ["Ropa", "Deportes", "Juguetería"]
ventas = [[0 for _ in range(len(departamentos))] for _ in range(12)]

def agregar_departamento():
    nuevo = input("Ingresa el nombre del nuevo departamento: ")
    departamentos.append(nuevo)
    for fila in ventas:
        fila.append(0)
    print(f" Departamento agregado: {nuevo}")

def pedir_mes():
    return int(input("Ingresa el número de mes (1-12): ")) - 1

def pedir_departamento():
    print("Departamentos:")
    for i, d in enumerate(departamentos):
        print(f"{i+1}. {d}")
    return int(input("Elige un departamento: ")) - 1

def insertar_venta():
    mes = pedir_mes()
    dep = pedir_departamento()
    ventas[mes][dep] = int(input("Ingresa la venta: "))
    print(" Venta registrada.")

def buscar_venta():
    mes = pedir_mes()
    dep = pedir_departamento()
    print(f"La venta es: {ventas[mes][dep]}")

def eliminar_venta():
    mes = pedir_mes()
    dep = pedir_departamento()
    ventas[mes][dep] = 0
    print(" Venta eliminada.")

def mostrar_ventas():
    print("\n--- Tabla de Ventas ---")
    print("Mes\t\t" + "\t".join(departamentos))
    for i in range(12):
        fila = [str(ventas[i][j]) for j in range(len(departamentos))]
        print(f"{meses[i]}\t" + "\t\t".join(fila))

while True:
    print("\n--- Menú ---")
    print("1. Insertar/Actualizar venta")
    print("2. Buscar venta")
    print("3. Eliminar venta")
    print("4. Mostrar tabla de ventas")
    print("5. Agregar nuevo departamento")
    print("6. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        insertar_venta()
    elif opcion == 2:
        buscar_venta()
    elif opcion == 3:
        eliminar_venta()
    elif opcion == 4:
        mostrar_ventas()
    elif opcion == 5:
        agregar_departamento()
    elif opcion == 6:
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")
