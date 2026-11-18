def convierte_binario_a_decimal(binario: str) -> int:
    """
    Convierte un número binario (representado como cadena) a su 
    representación decimal (como número entero).
    
    Por ejemplo, "1010" se convierte a 10.

    Parámetros:
    binario (str): Número binario como cadena.

    Devuelve:
    int: El número decimal correspondiente.
    """
    res = 0
    pos = 0
    for i in binario[::-1]: #para que mire la cadena de derecha a izquierda
        if i == '1':
            res += 2 ** pos
        pos += 1
    return res