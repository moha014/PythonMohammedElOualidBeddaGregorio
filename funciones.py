import unicodedata

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas, tildes y signos de puntuación.
    Retorna True si es palíndromo, False en caso contrario.
    """
    # Validación defensiva: Si no es una cadena, no podemos procesarlo
    if not isinstance(cadena, str):
        raise TypeError("La entrada debe ser una cadena de texto.")

    # Normalización para eliminar tildes (NFD separa caracteres de sus acentos)
    cadena_normalizada = unicodedata.normalize('NFD', cadena)
    
    # Nos quedamos solo con los caracteres base (no marcas de acento)
    cadena_sin_tildes = u"".join(
        c for c in cadena_normalizada if unicodedata.category(c) != 'Mn'
    )

    # Convertir a minúsculas y mantener solo caracteres alfanuméricos
    # Esto cumple con eliminar espacios, puntuación, etc. [cite: 6]
    cadena_limpia = ''.join(
        char.lower() for char in cadena_sin_tildes if char.isalnum()
    )

    # Comparar la cadena limpia con su reverso [cite: 25]
    return cadena_limpia == cadena_limpia[::-1]