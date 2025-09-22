import java.util.*;

public class VentasDepartamentos {
    static String[] meses = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};
    static ArrayList<String> departamentos = new ArrayList<>();
    static ArrayList<int[]> ventas = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);

    // Inicializar con 3 departamentos base
    static {
        departamentos.add("Ropa");
        departamentos.add("Deportes");
        departamentos.add("Juguetería");
        for (int i = 0; i < 12; i++) {
            ventas.add(new int[departamentos.size()]);
        }
    }

    // Agregar nuevo departamento
    public static void agregarDepartamento() {
        System.out.print("Ingresa el nombre del nuevo departamento: ");
        String nuevo = sc.next();
        departamentos.add(nuevo);

        // Expandir las filas (meses) para incluir el nuevo departamento
        for (int i = 0; i < 12; i++) {
            int[] filaVieja = ventas.get(i);
            int[] filaNueva = Arrays.copyOf(filaVieja, departamentos.size());
            ventas.set(i, filaNueva);
        }
        System.out.println(" Departamento agregado: " + nuevo);
    }

    // Insertar o actualizar venta
    public static void insertarVenta() {
        int mes = pedirMes();
        int dep = pedirDepartamento();
        System.out.print("Ingresa la venta: ");
        ventas.get(mes)[dep] = sc.nextInt();
        System.out.println(" Venta registrada.");
    }

    // Buscar venta
    public static void buscarVenta() {
        int mes = pedirMes();
        int dep = pedirDepartamento();
        System.out.println("La venta es: " + ventas.get(mes)[dep]);
    }

    // Eliminar venta
    public static void eliminarVenta() {
        int mes = pedirMes();
        int dep = pedirDepartamento();
        ventas.get(mes)[dep] = 0;
        System.out.println(" Venta eliminada.");
    }

    // Mostrar tabla completa
    public static void mostrarVentas() {
        System.out.println("\n--- Tabla de Ventas ---");
        System.out.print("Mes\t\t");
        for (String d : departamentos) {
            System.out.print(d + "\t");
        }
        System.out.println();
        for (int i = 0; i < 12; i++) {
            System.out.print(meses[i] + "\t");
            int[] fila = ventas.get(i);
            for (int v : fila) {
                System.out.print(v + "\t\t");
            }
            System.out.println();
        }
    }

    private static int pedirMes() {
        System.out.print("Ingresa el número de mes (1-12): ");
        return sc.nextInt() - 1;
    }

    private static int pedirDepartamento() {
        System.out.println("Departamentos:");
        for (int i = 0; i < departamentos.size(); i++) {
            System.out.println((i + 1) + ". " + departamentos.get(i));
        }
        System.out.print("Elige un departamento: ");
        return sc.nextInt() - 1;
    }

    public static void main(String[] args) {
        int opcion;
        do {
            System.out.println("\n--- Menú ---");
            System.out.println("1. Insertar/Actualizar venta");
            System.out.println("2. Buscar venta");
            System.out.println("3. Eliminar venta");
            System.out.println("4. Mostrar tabla de ventas");
            System.out.println("5. Agregar nuevo departamento");
            System.out.println("6. Salir");
            System.out.print("Elige una opción: ");
            opcion = sc.nextInt();

            switch (opcion) {
                case 1 -> insertarVenta();
                case 2 -> buscarVenta();
                case 3 -> eliminarVenta();
                case 4 -> mostrarVentas();
                case 5 -> agregarDepartamento();
                case 6 -> System.out.println("Saliendo...");
                default -> System.out.println("Opción inválida.");
            }
        } while (opcion != 6);
    }
}
