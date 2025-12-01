r"""
main.py
Programa principal interactivo que determina si una cadena proporcionada
por el usuario es palíndroma. Solicita al usuario repetidamente que
introduzca cadenas hasta que escriba 'salir'.

Última Modificación: 01/12/2024
Autor: Mohammed El Oualid Bedda
Dependencias: palindromo
"""
import sys
import os

# Agregar el directorio actual al path para importar el módulo
sys.path.insert(0, os.path.dirname(__file__))

from palindromo import esPalindromo


def main():
    """
    Función principal que ejecuta el bucle interactivo de la aplicación.
    Solicita frases al usuario y determina si son palíndromos.
    """
    print("=" * 70)
    print("    PROGRAMA DE VERIFICACIÓN DE PALÍNDROMOS")
    print("    Autor: Mohammed El Oualid Bedda")
    print("=" * 70)
    print()
    print("Este programa verifica si una frase es palíndroma.")
    print("Una frase es palíndroma si se lee igual de adelante hacia atrás")
    print("ignorando espacios, puntuación, tildes y mayúsculas.")
    print()
    print("Escribe 'salir' para terminar el programa.")
    print("-" * 70)
    print()
    
    while True:
        try:
            # Solicitar entrada del usuario
            frase = input("Introduce una frase (o escribe 'salir' para terminar): ")
            
            # Verificar si el usuario quiere salir
            if frase.lower() == "salir":
                print()
                print("-" * 70)
                print("¡Programa finalizado! Gracias por usar nuestro verificador.")
                print("=" * 70)
                break
            
            # Verificar si la entrada está vacía
            if not frase.strip():
                print("⚠️  Por favor, introduce una frase válida (no puede estar vacía).")
                print()
                continue
            
            # Comprobar si es palíndromo
            resultado = esPalindromo(frase)
            
            if resultado:
                print(f"✓ La frase es palíndroma.")
            else:
                print(f"✗ La frase no es palíndroma.")
            
            print()
        
        except KeyboardInterrupt:
            # Manejar Ctrl+C elegantemente
            print()
            print()
            print("-" * 70)
            print("¡Programa interrumpido por el usuario!")
            print("=" * 70)
            break
        
        except Exception as e:
            # Manejar cualquier otro error
            print(f"❌ Error inesperado: {e}")
            print("Por favor, intenta nuevamente.")
            print()


if __name__ == "__main__":
    main()
