import unicodedata

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas, tildes y signos de puntuación.
    Retorna True si es palíndromo, False en caso contrario.
    """
    if not isinstance(cadena, str):
        raise TypeError("La entrada debe ser una cadena de texto.")

    cadena_normalizada = unicodedata.normalize('NFD', cadena)
    
    cadena_sin_tildes = u"".join(
        c for c in cadena_normalizada if unicodedata.category(c) != 'Mn'
    )

    cadena_limpia = ''.join(
        char.lower() for char in cadena_sin_tildes if char.isalnum()
    )

    return cadena_limpia == cadena_limpia[::-1]