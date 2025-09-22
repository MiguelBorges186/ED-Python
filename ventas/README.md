# Programa de Ventas Mensuales (Java & Python)

Este proyecto contiene dos programas: uno en **Java** y otro en **Python**, que permiten administrar las ventas mensuales de los departamentos **Ropa, Deportes y Juguetería** durante los 12 meses del año.

El programa utiliza un **arreglo bidimensional** donde:
- Las filas representan los meses (Enero a Diciembre).
- Las columnas representan los departamentos.
- Cada celda guarda el valor de la venta correspondiente.

---

## Versión en Java

### ¿En qué consiste?
El programa en Java administra las ventas en un arreglo bidimensional dinámico.  
Además de manejar los tres departamentos iniciales, también permite **agregar nuevos departamentos** si el usuario lo desea.

### Métodos principales
- **insertarVenta()** → Inserta o actualiza una venta en un mes y departamento.  
- **buscarVenta()** → Busca y muestra la venta registrada en un mes y departamento específico.  
- **eliminarVenta()** → Elimina la venta registrada, dejando el valor en `0`.  
- **mostrarVentas()** → Muestra en forma de tabla todas las ventas de los 12 meses y departamentos.  
- **agregarDepartamento()** → Agrega un nuevo departamento a la tabla.  

---

## Versión en Python

### ¿En qué consiste?
El programa en Python también administra las ventas en un arreglo bidimensional,  
y al igual que en Java, permite **agregar nuevos departamentos** además de los tres iniciales.

### Métodos principales
- **insertar_venta(mes, dep, valor)** → Registra una venta en un mes y departamento específico.  
- **buscar_venta(mes, dep)** → Devuelve la venta registrada en el mes y departamento elegido.  
- **eliminar_venta(mes, dep)** → Elimina la venta registrada (coloca el valor en `0`).  
- **mostrar_ventas()** → Imprime en consola la tabla completa de ventas (12 meses × departamentos).  
- **agregar_departamento(nombre)** → Permite agregar un nuevo departamento (por ejemplo, *Comida*). La tabla se expande automáticamente para incluirlo en todos los meses.  

---


