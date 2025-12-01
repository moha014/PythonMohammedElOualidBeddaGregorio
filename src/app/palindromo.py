r"""
palindromo.py
Módulo que contiene la función esPalindromo para determinar si una cadena
es palíndroma. Una cadena es palíndroma si se lee igual de adelante hacia
atrás y de atrás hacia delante, ignorando espacios, puntuación, tildes
y diferencias entre mayúsculas y minúsculas.

Última Modificación: 01/12/2024
Autor: Mohammed El Oualid Bedda
Dependencias: unicodedata
"""
import unicodedata


def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    
    Una cadena es palíndroma si se lee igual de adelante hacia atrás que de
    atrás hacia delante, después de eliminar espacios, puntuación, tildes
    y diéresis, e ignorando diferencias entre mayúsculas y minúsculas.
    
    Args:
        cadena (str): La cadena de texto a verificar.
    
    Returns:
        bool: True si la cadena es palíndroma, False en caso contrario.
    
    Raises:
        TypeError: Si el argumento no es una cadena de texto.
        
    Examples:
        >>> esPalindromo("Anilina")
        True
        >>> esPalindromo("A man, a plan, a canal: Panama")
        True
        >>> esPalindromo("Hola mundo")
        False
    """
    # Validación defensiva: Verificar que la entrada sea una cadena
    if not isinstance(cadena, str):
        raise TypeError(
            f"La entrada debe ser una cadena de texto, "
            f"se recibió {type(cadena).__name__}"
        )
    
    # Normalización para eliminar tildes y diéresis
    # NFD (Decomposed Form) separa caracteres de sus acentos
    cadena_normalizada = unicodedata.normalize('NFD', cadena)
    
    # Eliminar marcas de acento (categoría 'Mn' = Mark, nonspacing)
    cadena_sin_tildes = u"".join(
        c for c in cadena_normalizada if unicodedata.category(c) != 'Mn'
    )
    
    # Convertir a minúsculas y mantener solo caracteres alfanuméricos
    # Esto elimina espacios, puntuación y otros caracteres especiales
    cadena_limpia = ''.join(
        char.lower() for char in cadena_sin_tildes if char.isalnum()
    )
    
    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]
