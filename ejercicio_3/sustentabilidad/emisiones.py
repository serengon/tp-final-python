# Ejercicio 3 - Cálculo de emisiones y métricas de consumo


# Función dada por el enunciado (Guía M2-C1)
def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float = 0.4) -> float:
    """Calcula emisiones estimadas. Eleva error si el consumo es negativo."""
    if consumo_kwh < 0:
        raise ValueError("El consumo energético no puede ser negativo.")

    emisiones = consumo_kwh * factor_emision
    return emisiones


# Punto B: Procesamiento de métricas
def obtener_metricas_consumo(registros: list) -> dict:
    """Recibe el historial de consumos y retorna el total de emisiones y la planta que más consume."""

    # 1. Sumamos el consumo de cada planta en un diccionario (Guía M1-C4).
    #    Una misma planta puede aparecer varias veces en el historial,
    #    por eso primero acumulamos y después comparamos.
    consumo_por_planta = {}
    for registro in registros:
        planta = registro["planta"]
        consumo = registro["consumo_kwh"]
        consumo_por_planta[planta] = consumo_por_planta.get(planta, 0) + consumo

    # 2. Total global de emisiones usando la función auditada
    total_emisiones = 0
    for registro in registros:
        total_emisiones += calcular_emisiones_carbono(registro["consumo_kwh"])

    # 3. Planta de mayor consumo (Guía M2-C2: max con lambda)
    if len(consumo_por_planta) == 0:
        planta_top = "Sin datos"
    else:
        planta_top = max(consumo_por_planta, key=lambda planta: consumo_por_planta[planta])

    return {
        "total_emisiones": total_emisiones,
        "planta_top": planta_top,
        "consumo_por_planta": consumo_por_planta
    }
