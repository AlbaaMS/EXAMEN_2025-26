from datetime import date, timedelta

def calcula_racha_maxima(fechas: list[date]) -> int:
    '''
    Dada una lista de fechas, calcula la racha máxima de días consecutivos.
    
    La lista de fechas puede no estar ordenadas y puede contener duplicados, los cuáles
    no serán tenidos en cuenta para el cálculo de las rachas.

    Parámetros:
    fechas (list[date]): Lista de fechas.

    Devuelve:
    int: La racha máxima de días consecutivos.  
    '''
    sin_duplicados = []

    if not fechas:
        return 0
    
    racha_maxima = 1
    racha_actual = 1
    
    for f in fechas:
        if f not in sin_duplicados:
            sin_duplicados.append(f)
    sin_duplicados.sort() #cuidado, si lo hubiera hecho sobre la original la hubiera modificado y no queremos eso

    for pos in range(len(sin_duplicados)-1): #para que no se salga del rango
        fecha1 = sin_duplicados[pos]
        fecha2 = sin_duplicados[pos + 1]
        if fecha2 - fecha1 == timedelta(days = 1):
            racha_actual +=1
            if racha_actual > racha_maxima:
                racha_maxima = racha_actual
        else:
            racha_actual = 1

    return racha_maxima