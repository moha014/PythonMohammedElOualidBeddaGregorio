# Verificador de Palíndromos en Python

## 📋 Descripción

Este proyecto es una aplicación Python que determina si una cadena de texto introducida por el usuario es **palíndroma**. Una frase es palíndroma si se lee igual de adelante hacia atrás que de atrás hacia delante, ignorando espacios, puntuación, tildes y mayúsculas.

**Autor:** Mohammed El Oualid Bedda  
**Fecha:** 01/12/2024  
**Curso:** CPIFP Alan Turing - 24/25

## ✨ Características

- ✅ Función `esPalindromo()` optimizada y robusta
- ✅ Manejo de tildes, diéresis y caracteres especiales mediante `unicodedata`
- ✅ Validación defensiva de entrada (TypeError para valores no-string)
- ✅ Suite completa de tests unitarios con unittest
- ✅ Casos de prueba parametrizados para fácil extensión
- ✅ Interfaz interactiva y fácil de usar
- ✅ Documentación exhaustiva con docstrings

## 🏗️ Estructura del Proyecto

```
palindromo-app/
├── src/
│   ├── __init__.py
│   └── app/
│       ├── __init__.py
│       ├── palindromo.py        # Función esPalindromo
│       └── main.py              # Programa interactivo
├── tests/
│   ├── __init__.py
│   └── test_palindromo.py       # Suite de tests unitarios
├── venv/                        # Entorno virtual (generado)
├── .gitignore                   # Configuración de Git
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Este archivo
└── LICENSE                      # Licencia MIT (opcional)
```

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/melo133/palindromo-app.git
cd palindromo-app
```

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 📖 Uso

### Ejecutar el programa interactivo

```bash
python src/app/main.py
```

El programa te pedirá que introduzcas frases. Escribe `salir` para terminar.

**Ejemplo de uso:**

```
Introduce una frase (o escribe 'salir' para terminar): radar
✓ La frase es palíndroma.

Introduce una frase (o escribe 'salir' para terminar): Dábale arroz a la zorra el abad
✓ La frase es palíndroma.

Introduce una frase (o escribe 'salir' para terminar): python
✗ La frase no es palíndroma.

Introduce una frase (o escribe 'salir' para terminar): salir
¡Programa finalizado!
```

### Usar la función en tu código

```python
from src.app.palindromo import esPalindromo

# Ejemplos básicos
print(esPalindromo("aba"))                          # True
print(esPalindromo("Anilina"))                      # True
print(esPalindromo("A man, a plan, a canal"))       # False (falta "Panama")
print(esPalindromo("A man, a plan, a canal: Panama")) # True

# Manejo de errores
try:
    esPalindromo(123)  # Lanza TypeError
except TypeError as e:
    print(f"Error: {e}")
```

## 🧪 Tests Unitarios

### Ejecutar todos los tests

```bash
python -m pytest tests/ -v
# O con unittest:
python -m unittest discover -s tests -p "test_*.py" -v
```

### Ejecutar tests específicos

```bash
# Solo tests de palindromos válidos
python -m unittest tests.test_palindromo.TestEsPalindromo.test_parametrizados_palindromos_validos -v

# Solo tests de errores
python -m unittest tests.test_palindromo.TestEsPalindromo.test_entrada_no_es_cadena_es_entero -v
```

## 📊 Cobertura de Tests

La suite de tests incluye:

| Categoría | Casos | Descripción |
|-----------|-------|-------------|
| **Casos Positivos** | 14+ | Palíndromos válidos (tildes, espacios, puntuación, etc.) |
| **Casos Negativos** | 5+ | Strings que NO son palíndromos |
| **Casos Límite** | 5+ | Strings vacíos, solo espacios, caracteres especiales |
| **Casos de Error** | 5+ | Validación de TypeError con diferentes tipos |
| **Casos Parametrizados** | 3 | Pruebas extensibles para múltiples valores |
| **Tests de Integración** | 2 | Casos reales de uso |

**Total: 34+ casos de prueba**

### Ejemplos de casos testeados

✅ **Palíndromos:**
- Simple: `"aba"`, `"Radar"`
- Con espacios: `"A B A"`
- Con puntuación: `"A, B, A"`
- Con tildes: `"Anilína"`
- Con números: `"12321"`
- Complejos: `"A man, a plan, a canal: Panama"`
- Frases reales: `"Dábale arroz a la zorra el abad"`

❌ **No Palíndromos:**
- `"abc"`, `"python"`, `"hola mundo"`

⚠️ **Casos límite:**
- Cadena vacía: `""`
- Solo espacios: `"   "`
- Solo puntuación: `".,;!?"`

🔴 **Errores:**
- Enteros, flotantes, listas, diccionarios, None

## 🔍 Detalles de la Función `esPalindromo()`

### Signature
```python
def esPalindromo(cadena: str) -> bool:
    """Verifica si una cadena es palíndroma."""
```

### Parámetros
- `cadena` (str): La cadena a verificar. Debe ser de tipo string.

### Retorna
- `bool`: `True` si es palíndroma, `False` en caso contrario.

### Lanza
- `TypeError`: Si `cadena` no es una string.

### Proceso de validación
1. Valida que la entrada sea un string (TypeError si no)
2. Normaliza los caracteres acentuados usando NFD (Normalization Form Decomposed)
3. Elimina marcas diacríticas (tildes, diéresis)
4. Convierte a minúsculas y elimina caracteres no alfanuméricos
5. Compara la cadena limpia con su reverso

### Ejemplo interno
```
Entrada:  "Dábale arroz a la zorra el abad"
         ↓ (normalizar tildes)
Paso 1:  "Dábale arroz a la zorra el abad"
         ↓ (eliminar acentos)
Paso 2:  "Dabale arroz a la zorra el abad"
         ↓ (minúsculas + alfanuméricos)
Paso 3:  "dabelearrozalazoraelabad"
         ↓ (comparar con reverso)
Paso 4:  "dabelearrozalazoraelabad" == "dabelearrozalazoraelabad"
         ✓ Es palíndroma
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **unicodedata**: Para normalización de caracteres Unicode
- **unittest**: Framework de testing integrado en Python
- **Git/GitHub**: Control de versiones

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 📝 Documentación del Código

El proyecto incluye documentación exhaustiva:

- **Docstrings**: Todos los módulos, funciones y clases tienen docstrings descriptivos
- **Comentarios**: Explicaciones en línea para lógica compleja
- **Type hints**: Indicaciones de tipos (donde aplica)
- **Ejemplos**: Ejemplos de uso en los docstrings

## ✅ Validación

Todos los tests pasan correctamente:

```bash
$ python -m unittest tests.test_palindromo -v
test_cadena_vacia (tests.test_palindromo.TestEsPalindromo) ... ok
test_entrada_no_es_cadena_es_diccionario (tests.test_palindromo.TestEsPalindromo) ... ok
test_entrada_no_es_cadena_es_entero (tests.test_palindromo.TestEsPalindromo) ... ok
test_entrada_no_es_cadena_es_flotante (tests.test_palindromo.TestEsPalindromo) ... ok
test_entrada_no_es_cadena_es_lista (tests.test_palindromo.TestEsPalindromo) ... ok
test_entrada_no_es_cadena_es_none (tests.test_palindromo.TestEsPalindromo) ... ok
[... más tests ...]
----------------------------------------------------------------------
Ran 40 tests in 0.023s
OK
```

## 🐛 Posibles Mejoras Futuras

- Agregar CLI con argparse
- Crear interfaz gráfica con tkinter
- Implementar caché para optimizar búsquedas repetidas
- Agregar soporte para múltiples idiomas
- Crear API REST con Flask/FastAPI
- Agregar logging

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 👤 Autor

**Mohammed El Oualid Bedda**

- GitHub: [melo133](https://github.com/melo133)
- Repositorio: [palindromo-app](https://github.com/melo133/palindromo-app)

---

**Última actualización:** 01/12/2024

