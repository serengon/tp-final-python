# Ejercicio 1 - Sanitización y Análisis Estadístico de Sensores


# Punto A: Normalización de lecturas
def limpiar_registro_sensor(registro_raw: dict) -> dict:
    """Recibe un registro crudo de un sensor y retorna un diccionario nuevo limpio."""

    # Guía M1-C1: strip() saca los espacios de los extremos
    sensor_id = registro_raw["sensor_id"].strip()

    # Guía M1-C1: limpiamos el texto y hacemos el casting a float
    temperatura_texto = registro_raw["temperatura"].strip()
    temperatura_texto = temperatura_texto.replace("C", "")
    temperatura = float(temperatura_texto)

    # Guía M1-C4: .get() con valor por defecto para no tener KeyError
    ubicacion = registro_raw.get("ubicacion", "Desconocida")
    if ubicacion is None or ubicacion.strip() == "":
        ubicacion = "Desconocida"

    # Retornamos un diccionario NUEVO (no modificamos el original)
    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion.strip()
    }


# Punto B: Monitoreo y mapeo estadístico
def generar_resumen_sensores(lista_sensores_limpios: list, umbral_temperatura: float) -> tuple:
    """Retorna una tupla con (ids de sensores en alerta, promedio de temperatura)."""

    # Si la lista está vacía no se puede dividir por cero
    if len(lista_sensores_limpios) == 0:
        return ([], 0.0)

    # Guía M2-C2: filter + lambda para quedarnos con los que superan el umbral
    sensores_en_alerta = list(filter(lambda s: s["temperatura"] > umbral_temperatura,
                                     lista_sensores_limpios))

    # Guía M2-C2: map + lambda para extraer solo los IDs
    lista_sensores_alerta = list(map(lambda s: s["sensor_id"], sensores_en_alerta))

    # Promedio = suma de temperaturas / cantidad de sensores
    suma = 0
    for sensor in lista_sensores_limpios:
        suma += sensor["temperatura"]
    promedio_temperatura = suma / len(lista_sensores_limpios)

    # Guía M1-C3: la tupla sirve para retornar varios valores juntos
    return (lista_sensores_alerta, promedio_temperatura)


# Bloque de ejecución: flujo completo
if __name__ == "__main__":
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002  ", "temperatura": "31.2C", "ubicacion": "Planta Sur"},
        {"sensor_id": "  SENSOR-003", "temperatura": "  28.9C  "},
        {"sensor_id": "SENSOR-004", "temperatura": "35.0C", "ubicacion": ""},
    ]
    umbral = 30.0

    # 1. Limpiamos cada registro crudo
    sensores_limpios = []
    for registro in registros_crudos:
        sensores_limpios.append(limpiar_registro_sensor(registro))

    # 2. Generamos el resumen (desempaquetamos la tupla)
    alertas, promedio = generar_resumen_sensores(sensores_limpios, umbral)

    # 3. Imprimimos el reporte formateado
    print("=========== REPORTE DE SENSORES ===========")
    for sensor in sensores_limpios:
        print(f"{sensor['sensor_id']} | {sensor['ubicacion']} | {sensor['temperatura']}°C")
    print("-------------------------------------------")
    print(f"Umbral de alerta: {umbral}°C")
    print(f"Sensores en alerta: {alertas}")
    print(f"Promedio de temperatura: {promedio:.2f}°C")
