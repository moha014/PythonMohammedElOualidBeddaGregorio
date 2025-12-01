# Palindromo

Un programa que verifica si una frase es un palíndromo.

## Instalación

```bash
git clone https://github.com/melo133/palindromo-app.git
cd palindromo-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Cómo ejecutar

```bash
python src/app/main.py
```

Escribe frases y te dirá si son palíndromos o no.

## Ejemplo

```
Escribe una frase (o 'salir' para terminar): radar
Es palíndroma

Escribe una frase (o 'salir' para terminar): python
No es palíndroma

Escribe una frase (o 'salir' para terminar): salir
Hasta luego!
```

## Código

```python
from src.app.palindromo import esPalindromo

print(esPalindromo("aba"))  # True
print(esPalindromo("hola"))  # False
```

## Tests

Ejecutar los tests:

```bash
python -m unittest tests.test_palindromo -v
```

## Funcionalidad

- Verifica si una cadena es un palíndromo
- Ignora espacios, puntuación y mayúsculas
- Maneja tildes
- Valida que sea un string
- Incluye tests

## Requisitos

- Python 3.8+

## Autor

Mohammed El Oualid Bedda
