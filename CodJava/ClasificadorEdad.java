
import java.util.Scanner;

public class ClasificadorEdad {

    public static void main(String[] args) {
        // Crear un objeto Scanner para leer la entrada del usuario
        Scanner scanner = new Scanner(System.in);

        // Solicitar la edad del usuario
        System.out.print("Por favor, ingresa tu edad: ");

        try {
            // Leer la entrada del usuario
            int edad = scanner.nextInt();

            // Verificar si la edad es válida (no negativa)
            if (edad < 0) {
                System.out.println("Por favor, ingresa una edad válida (no negativa).");
            } else {
                // Clasificar al usuario según su edad
                if (edad < 13) {
                    System.out.println("Eres un niño.");
                } else if (edad >= 13 && edad <= 17) {
                    System.out.println("Eres un adolescente.");
                } else if (edad >= 18 && edad <= 64) {
                    System.out.println("Eres un adulto.");
                } else {
                    System.out.println("Eres un adulto mayor.");
                }
            }
        } catch (Exception e) {
            System.out.println("Por favor, ingresa un número válido.");
        } finally {
            // Cerrar el scanner
            scanner.close();
        }
    }
}
