# Ejercicio 3 - Punto B: Vista de Django (Guía M6-C1, arquitectura MVT)
from django.shortcuts import render
from .emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    # Historial de consumos por planta (más adelante vendría del models.py)
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 1200},
        {"planta": "Planta Sur", "consumo_kwh": 850},
        {"planta": "Planta Este", "consumo_kwh": 1500},
        {"planta": "Planta Norte", "consumo_kwh": 640},
    ]

    # Procesamos las métricas con la función del Punto B
    metricas = obtener_metricas_consumo(registros)

    # Empaquetamos los datos en el diccionario de contexto
    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_top": metricas["planta_top"],
        "consumo_por_planta": metricas["consumo_por_planta"],
    }

    # Renderizamos la plantilla con el contexto
    return render(request, "sustentabilidad/panel.html", contexto)
