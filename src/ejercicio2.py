def divide_cadena(texto: str) -> tuple[str, str]:
    """
    Divide la cadena en dos, una fomada por los caracteres
    pares y otra por los impares.

    Parámetros:
    texto (str): El texto original.

    Devuelve:
    tuple[str, str]: Una tupla con dos cadenas, la primera con los caracteres en posiciones pares
                     y la segunda con los caracteres en posiciones impares.
    """
    pares = ""
    impares = ""
    for i in range(len(texto)):
        if i % 2 == 0:
            pares += texto[i]
        else:
            impares += texto[i]
    return pares, impares