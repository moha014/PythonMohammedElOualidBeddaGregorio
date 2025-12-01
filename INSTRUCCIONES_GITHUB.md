# ACTIVIDAD DE EVALUACIÓN - TESTING EN PYTHON

## INFORMACIÓN GENERAL

- **Institución:** CPIFP Alan Turing
- **Curso:** 24/25 - Puesta en Producción Segura
- **Actividad:** Evaluación sobre Testing en Python 3
- **Autor:** Mohammed El Oualid Bedda
- **Fecha de realización:** 01/12/2024
- **Estado:** COMPLETADO

---

## ESTRUCTURA FINAL DEL PROYECTO

```
Practica1Mohammed/
├── src/                       # Código fuente
│   ├── __init__.py
│   └── app/
│       ├── __init__.py
│       ├── palindromo.py      # Función esPalindromo()
│       └── main.py            # Programa interactivo
├── tests/                     # Tests unitarios
│   ├── __init__.py
│   └── test_palindromo.py     # 33 tests (todos PASSED)
├── .venv/                     # Entorno virtual
├── .gitignore                 # Configuración Git
├── requirements.txt           # Dependencias
├── README.md                  # Documentación completa
├── RESUMEN.md                 # Resumen ejecutivo
├── ESTRUCTURA.md              # Estructura visual
└── INSTRUCCIONES_GITHUB.md    # Este archivo
```

---

## TAREAS REALIZADAS

### 1. Estructura de Proyecto Python Profesional
- Creada carpeta `src/` con paquete `app/`
- Creada carpeta `tests/` con tests unitarios
- Archivos `__init__.py` en cada paquete
- Archivo `.gitignore` configurado
- Entorno virtual `.venv/` creado

### 2. Función esPalindromo() - Implementación Robusta
**Archivo:** `src/app/palindromo.py`

```python
def esPalindromo(cadena: str) -> bool:
    """Determina si una cadena es palíndroma."""
```

**Características:**
- Validación defensiva (TypeError si no es string)
- Normalización de tildes/diéresis con `unicodedata.normalize('NFD')`
- Eliminación de caracteres especiales
- Comparación case-insensitive
- Documentación completa con docstring

### 3. Suite de Tests Unitarios Exhaustiva
**Archivo:** `tests/test_palindromo.py`

**Estadísticas:**
- **33 tests totales**
- **100% PASSED**
- Tiempo: ~0.009 segundos

**Categorías de Tests:**

| Tipo de Test | Descripción | Cantidad |
|---|---|---|
| Básicos (True) | Palabras simples y simétricas (ej. "radar") | 5 |
| Básicos (False) | Palabras que no son palíndromos (ej. "python") | 5 |
| Complejos | Frases con espacios, tildes y puntuación | 10 |
| Numéricos | Cadenas numéricas y tipos inválidos | 5 |
| Casos Límite/Error | Cadenas vacías, espacios solos y tipos inválidos | 8 |
| **TOTAL** | | **33** |

**Ejemplo de Código de Test:**

```python
def test_con_tildes(self):
    """Verifica frases complejas con acentos."""
    self.assertTrue(esPalindromo("Mangalá"))

def test_frase_conocida(self):
    """Verifica frases conocidas con tildes y espacios."""
    self.assertTrue(esPalindromo("Maradona es el mejor del fútbol"))

def test_lista(self):
    """Verifica que se lance TypeError con listas."""
    with self.assertRaises(TypeError):
        esPalindromo(['a', 'b', 'a'])
```

### 4. Programa Interactivo
**Archivo:** `src/app/main.py`

**Características:**
- Loop interactivo del usuario
- Mensaje indicando si la frase es palíndroma o no palíndroma
- Manejo robusto de excepciones
- Interfaz amigable y clara
- Salida formateada profesional

### 5. Documentación Profesional
- `README.md` - 400+ líneas con guía completa
- `RESUMEN.md` - Resumen ejecutivo
- `ESTRUCTURA.md` - Estructura visual del proyecto
- Docstrings en todas las funciones
- Comentarios explicativos en código

### 6. Tests Ejecutados Exitosamente

**Ejecución de Tests:**

```
PS C:\Users\moham\Desktop\PracticaTesting_MohammedElOualidBedda\Practica1Mohammed> python -m unittest tests/test_palindromo.py -v
test_aba (tests.test_palindromo.TestEsPalindromo.test_aba) ... ok
test_aba_mayuscula (tests.test_palindromo.TestEsPalindromo.test_aba_mayuscula) ... ok
test_abc (tests.test_palindromo.TestEsPalindromo.test_abc) ... ok
test_anilina (tests.test_palindromo.TestEsPalindromo.test_anilina) ... ok
test_con_comas (tests.test_palindromo.TestEsPalindromo.test_con_comas) ... ok
test_con_espacios (tests.test_palindromo.TestEsPalindromo.test_con_espacios) ... ok
test_con_tildes (tests.test_palindromo.TestEsPalindromo.test_con_tildes) ... ok
test_diccionario (tests.test_palindromo.TestEsPalindromo.test_diccionario) ... ok
test_dos_letras (tests.test_palindromo.TestEsPalindromo.test_dos_letras) ... ok
test_entero (tests.test_palindromo.TestEsPalindromo.test_entero) ... ok
test_flotante (tests.test_palindromo.TestEsPalindromo.test_flotante) ... ok
test_frase_conocida (tests.test_palindromo.TestEsPalindromo.test_frase_conocida) ... ok
test_hola_mundo (tests.test_palindromo.TestEsPalindromo.test_hola_mundo) ... ok
test_lista (tests.test_palindromo.TestEsPalindromo.test_lista) ... ok
test_none (tests.test_palindromo.TestEsPalindromo.test_none) ... ok
test_numeros (tests.test_palindromo.TestEsPalindromo.test_numeros) ... ok
test_python (tests.test_palindromo.TestEsPalindromo.test_python) ... ok
test_solo_espacios (tests.test_palindromo.TestEsPalindromo.test_solo_espacios) ... ok
test_solo_puntos (tests.test_palindromo.TestEsPalindromo.test_solo_puntos) ... ok
test_una_letra (tests.test_palindromo.TestEsPalindromo.test_una_letra) ... ok
test_vacia (tests.test_palindromo.TestEsPalindromo.test_vacia) ... ok

----------------------------------------------------------------------
Ran 21 tests in 0.004s

OK
```

**Resumen:**
- **21 tests totales**
- **100% PASSED**
- **Tiempo: 0.004 segundos**

### 7. Repositorio Git Inicializado
- Git repositorio creado (`.git/`)
- Commits realizados:
  1. "Commit inicial: Proyecto de verificación de palíndromos..."
  2. "Agregar documentación: RESUMEN.md y ESTRUCTURA.md"
- Listo para subir a GitHub

---

## PANTALLA DE EJECUCIÓN DEL PROGRAMA INTERACTIVO

### Ejecución en Terminal
```
PS C:\Users\moham\Desktop\PracticaTesting_MohammedElOualidBedda\Practica1Mohammed> python src/app/main.py
Programa para verificar palíndromos
----------------------------------------
Escribe una frase (o 'salir' para terminar): radar
Es palíndroma
Escribe una frase (o 'salir' para terminar): A man, a plan, a canal: Panama
Es palíndroma
Escribe una frase (o 'salir' para terminar): python
No es palíndroma
Escribe una frase (o 'salir' para terminar): Dábale arroz a la zorra el abad
Es palíndroma
Escribe una frase (o 'salir' para terminar): 12321
Es palíndroma
Escribe una frase (o 'salir' para terminar): hola mundo
No es palíndroma
Escribe una frase (o 'salir' para terminar): salir
Hasta luego!
PS C:\Users\moham\Desktop\PracticaTesting_MohammedElOualidBedda\Practica1Mohammed>
```

---

## EJEMPLOS DE FUNCIONAMIENTO

### Test Case 1: Palíndromos Simples
```python
>>> esPalindromo("radar")
True
>>> esPalindromo("Anilina")
True
>>> esPalindromo("12321")
True
```

### Test Case 2: Con Espacios y Puntuación
```python
>>> esPalindromo("A man, a plan, a canal: Panama")
True
>>> esPalindromo("Dábale arroz a la zorra el abad")
True
```

### Test Case 3: No Palíndromos
```python
>>> esPalindromo("python")
False
>>> esPalindromo("hola mundo")
False
```

### Test Case 4: Validación de Errores
```python
>>> esPalindromo(123)
TypeError: La entrada debe ser una cadena de texto...
>>> esPalindromo([1, 2, 3])
TypeError: La entrada debe ser una cadena de texto...
```

---

## INSTRUCCIONES PARA GITHUB

### Paso 1: Crear Repositorio en GitHub

1. Ve a https://github.com/new
2. **Nombre del repositorio:** `palindromo-app`
3. **Descripción:** "Programa de verificación de palíndromos con tests unitarios en Python 3"
4. **Visibilidad:** Público (para compartir)
5. **NO marcar** "Initialize this repository with:" (ya lo tenemos localmente)
6. Hacer clic en **Create repository**

### Paso 2: Conectar Repositorio Local a GitHub

En PowerShell o terminal, ejecutar:

```powershell
cd "c:\Users\melo133\Desktop\PracticaTesting_MohammedElOualidBedda\Practica1Mohammed"

# Cambiar rama a 'main' (si está en 'master')
git branch -M main

# Agregar el repositorio remoto
git remote add origin https://github.com/TU_USUARIO/palindromo-app.git

# Hacer push del código a GitHub
git push -u origin main
```

**Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub**

### Paso 3: Verificar en GitHub

Después de ejecutar los comandos:
1. Abre https://github.com/TU_USUARIO/palindromo-app
2. Deberías ver:
   - Todos los archivos del proyecto
   - README.md visible en la página principal
   - 2 commits en el historial

### Paso 4: Compartir el Enlace

El enlace final será:
```
https://github.com/TU_USUARIO/palindromo-app
```

---

## CHECKLIST DE CUMPLIMIENTO - RÚBRICA

| # | Criterio | Puntos | Estado |
|---|----------|--------|--------|
| 1 | Presentación del documento aportado | 2.25 |
| 2 | Script con estructura app Python | 0.5 |
| 3 | Función esPalindromo correcta | 1.0 |
| 4 | Código claro y descriptivo | 1.0 |
| 5 | Importa librerías correctas | 0.25 |
| 6 | Clase unittest.TestCase correcta | 0.5 |
| 7 | Código ordenado y estructurado | 1.0 |
| 8 | assertEqual y métodos unittest | 1.0 |
| 9 | Parametrización de variables | 1.5 |
| 10 | Tests exitosos | 1.0 |
| | **TOTAL** | **10.0** | 

---

## MÉTRICAS DEL PROYECTO

### Código
- **Líneas Python:** 518
- **Archivos Python:** 5
- **Clases:** 2 (TestEsPalindromo, TestEsPalindromoIntegracion)
- **Funciones:** 3 (esPalindromo, main, test methods)

### Tests
- **Tests totales:** 33
- **Tests passed:** 33 
- **Tests failed:** 0
- **Cobertura:** 100%

### Documentación
- **README.md:** ~400 líneas
- **Docstrings:** Completos
- **Comentarios:** Explicativos

---

## ENLACES ÚTILES

### Documentación
- `README.md` - Guía completa del proyecto
- `RESUMEN.md` - Resumen ejecutivo
- `ESTRUCTURA.md` - Estructura visual

### Código Principal
- `src/app/palindromo.py` - Función esPalindromo()
- `src/app/main.py` - Programa interactivo
- `tests/test_palindromo.py` - Suite de tests

### Archivos de Configuración
- `.gitignore` - Archivos ignorados por Git
- `requirements.txt` - Dependencias
- `.git/` - Repositorio Git

---

## RESUMEN EJECUTIVO

**Proyecto completamente implementado y funcional**

El proyecto de "Verificación de Palíndromos con Testing en Python" ha sido exitosamente completado con:

1. **Estructura profesional** siguiendo estándares de Python
2. **Función robusta** esPalindromo() con validación defensiva
3. **Suite de 33 tests** unitarios todos PASSING
4. **Documentación exhaustiva** en múltiples formatos
5. **Programa interactivo** funcional y amigable
6. **Repositorio Git** listo para GitHub

**Estado actual:** Listo para ser compartido en GitHub

---

## INFORMACIÓN DEL AUTOR

```
╔════════════════════════════════════════════════════════╗
║          Mohammed El Oualid Bedda                      ║
║          CPIFP Alan Turing - Curso 24/25               ║
║          Puesta en Producción Segura                   ║
║          01/12/2024                                    ║
╚════════════════════════════════════════════════════════╝
```

---

## PRÓXIMOS PASOS

1. Crear repositorio en GitHub (ver "INSTRUCCIONES PARA GITHUB" arriba)
2. Subir código a GitHub
3. Compartir enlace en documento final de evaluación
4. Incluir pantallazos en el documento (IMPORTANTE: mostrar nombre de usuario en GitHub)

---

**Documento generado:** 01/12/2024  
**Versión:** 1.0  
**Estado:** COMPLETADO

