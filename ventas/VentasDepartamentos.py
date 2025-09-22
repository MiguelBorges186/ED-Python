class VentasDepartamentos:
    def __init__(self):
        self.meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                      "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.departamentos = ["Ropa", "Deportes", "Juguetería"]
        self.ventas = [[0 for _ in range(len(self.departamentos))] for _ in range(12)]

    def insertar_venta(self, mes, dep, valor):
        self.ventas[mes][dep] = valor

    def buscar_venta(self, mes, dep):
        return self.ventas[mes][dep]

    def eliminar_venta(self, mes, dep):
        self.ventas[mes][dep] = 0

    def mostrar_ventas(self):
        print("\n--- Tabla de Ventas ---")
        print("Mes\t\t" + "\t".join(self.departamentos))
        for i in range(12):
            fila = [str(self.ventas[i][j]) for j in range(len(self.departamentos))]
            print(f"{self.meses[i]}\t" + "\t\t".join(fila))

    def agregar_departamento(self, nombre):
        nombre = nombre.strip()
        if not nombre:
            print(" Nombre inválido.")
            return
        if nombre in self.departamentos:
            print(" Ya existe el departamento:", nombre)
            return
        self.departamentos.append(nombre)
        for fila in self.ventas:
            fila.append(0)
        print(f" Departamento agregado: {nombre}")


def pedir_entero(rango_min, rango_max, prompt=""):
    while True:
        try:
            valor = int(input(prompt))
            if rango_min <= valor <= rango_max:
                return valor
            print(f"Ingresa un número entre {rango_min} y {rango_max}.")
        except ValueError:
            print("Ingresa un número válido.")

def elegir_mes(app):
    return pedir_entero(1, 12, "Ingresa el número de mes (1-12): ") - 1

def elegir_dep(app):
    print("\nDepartamentos:")
    for i, d in enumerate(app.departamentos, start=1):
        print(f"{i}. {d}")
    return pedir_entero(1, len(app.departamentos), "Elige un departamento: ") - 1

ventas = VentasDepartamentos()

while True:
    print("\n--- Menú ---")
    print("1. Insertar venta")
    print("2. Buscar venta")
    print("3. Eliminar venta")
    print("4. Mostrar tabla de ventas")
    print("5. Agregar nuevo departamento")
    print("6. Salir")

    opcion = pedir_entero(1, 6, "Elige una opción: ")

    if opcion == 1:
        mes = elegir_mes(ventas)
        dep = elegir_dep(ventas)
        valor = pedir_entero(0, 10**9, "Ingresa la venta: ")
        ventas.insertar_venta(mes, dep, valor)
        print(" Venta registrada.")

    elif opcion == 2:
        mes = elegir_mes(ventas)
        dep = elegir_dep(ventas)
        print(f"La venta es: {ventas.buscar_venta(mes, dep)}")

    elif opcion == 3:
        mes = elegir_mes(ventas)
        dep = elegir_dep(ventas)
        ventas.eliminar_venta(mes, dep)
        print(" Venta eliminada.")

    elif opcion == 4:
        ventas.mostrar_ventas()

    elif opcion == 5:
        nombre = input("Nombre del nuevo departamento: ")
        ventas.agregar_departamento(nombre)

    elif opcion == 6:
        print("Saliendo...")
        break

