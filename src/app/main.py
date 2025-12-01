import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from palindromo import esPalindromo


def main():
    print("Programa para verificar palíndromos")
    print("-" * 40)
    
    while True:
        try:
            frase = input("Escribe una frase (o 'salir' para terminar): ")
            
            if frase.lower() == "salir":
                print("Hasta luego!")
                break
            
            if not frase.strip():
                print("Por favor, escribe algo.")
                continue
            
            if esPalindromo(frase):
                print("Es palíndroma")
            else:
                print("No es palíndroma")
            
        except KeyboardInterrupt:
            print("\nPrograma cerrado")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
