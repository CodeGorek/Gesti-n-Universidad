import unicodedata


def normalizar_cadena(cadena):
    if not isinstance(cadena, str):
        cadena = str(cadena)
    s_decomposed = unicodedata.normalize('NFD', cadena)
    s_without_accents = ''.join(
        c for c in s_decomposed if unicodedata.category(c) != 'Mn')
    return s_without_accents.lower().strip()