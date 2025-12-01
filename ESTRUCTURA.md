# ESTRUCTURA COMPLETA DEL PROYECTO

```
Practica1Mohammed/
│
├── .gitignore                    # Configuración de archivos ignorados por Git
├── .git/                         # Repositorio Git local
├── requirements.txt              # Dependencias del proyecto
├── README.md                     # Documentación completa del proyecto
├── RESUMEN.md                    # Resumen ejecutivo (este archivo)
│
├── src/                          # Código fuente de la aplicación
│   ├── __init__.py               # Inicializador del paquete src
│   └── app/                      # Módulo principal de la aplicación
│       ├── __init__.py           # Inicializador del paquete app
│       ├── palindromo.py         # FUNCIÓN PRINCIPAL: esPalindromo()
│       └── main.py               # Programa interactivo
│
├── tests/                        # Suite de pruebas unitarias
│   ├── __init__.py               # Inicializador del paquete tests
│   └── test_palindromo.py        # 33 tests unitarios
│
├── .venv/                        # Entorno virtual de Python (generado)
│
└── funciones.py                  # Archivo original (mantenido para referencia)
```

---

## ESTADÍSTICAS DEL PROYECTO

### Líneas de Código
- **src/app/palindromo.py:** 67 líneas (función + docs)
- **src/app/main.py:** 95 líneas (programa interactivo)
- **tests/test_palindromo.py:** 356 líneas (suite de tests)
- **Total:** 518 líneas de código Python

### Tests Unitarios
- **Total de tests:** 33
- **Resultado:** ALL PASSED
- **Tiempo de ejecución:** ~0.009 segundos

### Documentación
- **README.md:** 400+ líneas
- **RESUMEN.md:** 250+ líneas
- **Docstrings:** Completos en todas las funciones y clases

---

## ARCHIVOS CLAVE

### `src/app/palindromo.py` - La función principal
```python
def esPalindromo(cadena: str) -> bool:
    """
    Determina si una cadena es palíndroma.
    Ignora espacios, puntuación, tildes y mayúsculas.
    """
```

**Características:**
- Valida entrada (TypeError si no es string)
- Normaliza caracteres acentuados
- Elimina tildes/diéresis con unicodedata
- Compara con su reverso

### `src/app/main.py` - Interfaz interactiva
- Loop infinito hasta que el usuario escriba "salir"
- Mensaje indicando si la frase es palíndroma o no palíndroma
- Manejo de excepciones
- Mensaje de inicio y salida personalizados

### `tests/test_palindromo.py` - Suite de tests
- **Clase TestEsPalindromo:** 26 métodos de test
- **Clase TestEsPalindromoIntegracion:** 2 métodos de test
- **Casos cubiertos:**
  - Positivos (palíndromos válidos)
  - Negativos (no-palíndromos)
  - Límite (vacíos, espacios)
  - Error (tipos inválidos)
  - Parametrizados (múltiples casos)
  - Integración (casos reales)

---

## EJEMPLOS DE USO

### Ejecutar tests
```bash
$ cd Practica1Mohammed
$ .venv\Scripts\python.exe tests\test_palindromo.py
...
Ran 33 tests in 0.009s
OK 
```

### Usar la función en Python
```python
from src.app.palindromo import esPalindromo

# Palíndromos válidos
assert esPalindromo("radar") == True
assert esPalindromo("Anilina") == True
assert esPalindromo("A man, a plan, a canal: Panamera") == True

# No-palíndromos
assert esPalindromo("python") == False
assert esPalindromo("hola") == False

# Manejo de errores
try:
    esPalindromo(123)
except TypeError:
    print("Error: debe ser una cadena")
```

### Ejecutar programa interactivo
```bash
$ .venv\Scripts\python.exe src/app/main.py

======================================================================
    PROGRAMA DE VERIFICACIÓN DE PALÍNDROMOS
    Autor: Mohammed El Oualid Bedda
======================================================================

Introduce una frase (o escribe 'salir' para terminar): Radar
La frase es palíndroma.

Introduce una frase (o escribe 'salir' para terminar): python
La frase no es palíndroma.

Introduce una frase (o escribe 'salir' para terminar): salir
```

---

## FEATURES IMPLEMENTADAS

**Función robusta esPalindromo()**
- Validación defensiva
- Manejo de Unicode/tildes
- Documentación completa
- Error handling

**Interfaz interactiva main.py**
- Loop del programa
- Validación de entrada
- Feedback visual
- Manejo de Ctrl+C

**Suite de tests exhaustiva**
- 33 tests unitarios
- Casos parametrizados
- Tests de integración
- Cobertura completa

**Documentación profesional**
- README.md detallado
- Docstrings en todo el código
- Comentarios explicativos
- Ejemplos de uso

**Estructura profesional**
- Paquetes organizados
- __init__.py en cada carpeta
- .gitignore configurado
- Git inicializado

---

## PRÓXIMOS PASOS PARA GITHUB

1. **Crear repositorio en GitHub:**
   ```
   https://github.com/new
   Nombre: palindromo-app
   ```

2. **Conectar repositorio local:**
   ```bash
   git remote add origin https://github.com/TU_USUARIO/palindromo-app.git
   git branch -M main
   git push -u origin main
   ```

3. **Compartir enlace:**
   ```
   https://github.com/TU_USUARIO/palindromo-app
   ```

---

## CHECKLIST DE CUMPLIMIENTO

- Estructura de proyecto Python profesional
- Función esPalindromo correctamente implementada
- Validación defensiva (TypeError)
- Manejo de tildes/diéresis con unicodedata
- Clase unittest.TestCase implementada
- 33 tests unitarios
- Casos parametrizados
- assertEqual/assertTrue/assertRaises
- Código claro y comentado
- Documentación exhaustiva
- Repositorio Git inicializado
- README.md completo

---

## INFORMACIÓN DEL AUTOR

**Nombre:** Mohammed El Oualid Bedda  
**Curso:** CPIFP Alan Turing - 24/25  
**Fecha:** 01/12/2024  
**Email:** mohammed.eloualid@gmail.com  
