import unicodedata


def esPalindromo(cadena):
    """Verifica si una cadena es palíndroma."""
    if not isinstance(cadena, str):
        raise TypeError(f"Se esperaba un string, se recibió {type(cadena).__name__}")
    
    normalizada = unicodedata.normalize('NFD', cadena)
    sin_tildes = u"".join(c for c in normalizada if unicodedata.category(c) != 'Mn')
    limpia = ''.join(char.lower() for char in sin_tildes if char.isalnum())
    return limpia == limpia[::-1]
