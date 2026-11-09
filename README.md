# TP Final - Programación con Python (EcoTech Solutions)

Resolución de los 3 ejercicios del trabajo práctico final.

## Estructura

```
├── ejercicio_1/          Sanitización y análisis estadístico de sensores
│   └── ejercicio1.py
├── ejercicio_2/          Modelo de productos, excepciones y persistencia
│   └── ejercicio2.py
├── ejercicio_3/          Tests unitarios e integración web (proyecto Django)
│   ├── manage.py
│   ├── config/           Configuración del proyecto (settings, urls)
│   └── sustentabilidad/  App con la lógica, los tests, la vista y la plantilla
│       ├── emisiones.py
│       ├── tests.py
│       ├── views.py
│       └── templates/sustentabilidad/panel.html
└── requirements.txt
```

## Instalación

Requiere Python 3.10 o superior.

```bash
git clone <url-de-este-repositorio>
cd <carpeta-del-repositorio>

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / Mac:
source .venv/bin/activate

pip install -r requirements.txt
```

## Cómo ejecutar cada ejercicio

**Ejercicio 1**
```bash
cd ejercicio_1
python ejercicio1.py
```

**Ejercicio 2** (genera el archivo `catalogo_ecotech.json` en la misma carpeta)
```bash
cd ejercicio_2
python ejercicio2.py
```

**Ejercicio 3**
```bash
cd ejercicio_3

# Punto A: tests unitarios
python -m unittest sustentabilidad.tests -v

# Punto B: panel web
python manage.py runserver
```
Después abrir http://127.0.0.1:8000/ en el navegador.

---

## Consignas

### Ejercicio 1 - Sanitización y Análisis Estadístico de Sensores (20 puntos)

Los microcontroladores de EcoTech Solutions transmiten lecturas térmicas en formato heterogéneo con espacios indeseados, textos mezclados con unidades de medida y atributos incompletos. Se necesita un componente que normalice estos registros individuales y genere un reporte consolidado para la toma de decisiones.

**Punto A: Normalización de Lecturas (`limpiar_registro_sensor`):** Diseña la función `limpiar_registro_sensor(registro_raw)` encargada de procesar un diccionario con datos crudos de un sensor (por ejemplo: `{"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}`). La función debe transformar la información para retornar un nuevo diccionario estandarizado, garantizando que el identificador quede sin espacios sobrantes, la temperatura sea un valor numérico de tipo float sin sufijos de unidad, y la ubicación posea un valor por defecto seguro en caso de no haberse registrado.

**Punto B: Monitoreo y Mapeo Estadístico (`generar_resumen_sensores`):** Desarrolla la función `generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura)` que tome una colección de registros sanitizados previamente con la función del Punto A y un valor límite. Debe retornar una tupla `(lista_sensores_alerta, promedio_temperatura)` conteniendo los IDs de los dispositivos que superan el umbral estipulado y el promedio térmico global de la planta. Incluye un bloque de ejecución que demuestre el flujo completo desde la limpieza de registros crudos hasta la impresión formateada del reporte final.

### Ejercicio 2 - Modelo de Productos, Excepciones y Persistencia (40 puntos)

Para la división de equipamiento sustentable de EcoTech Solutions, se requiere un módulo de software que gestione los productos del catálogo, impida inconsistencias en el inventario mediante validaciones de negocio y garantice la persistencia del stock en disco.

**Punto A: Dominio del Catálogo y Reglas de Inventario:** Construye la jerarquía orientada a objetos para los productos ecológicos. Diseña una clase de excepción personalizada `StockInvalidoError` y aplícala dentro de la clase base `DispositivoEcológico` para impedir que el stock tome valores negativos mediante encapsulamiento explícito. Desarrolla la clase especializada `PanelSolar`, incorporando sus atributos específicos mediante herencia y aplicando polimorfismo para personalizar la emisión de su ficha técnica comercial.

**Punto B: Persistencia y Gestión del Catálogo:** Implementa la clase `GestorInventario` con el método `guardar_catalogo_json(lista_dispositivos, ruta_archivo)` capaz de serializar y almacenar en `catalogo_ecotech.json` las instancias creadas en el Punto A. Incluye un bloque de prueba donde se verifique la captura controlada de `StockInvalidoError` ante un intento de asignación de stock erróneo, finalizando con la exportación exitosa de los productos válidos al archivo JSON.

### Ejercicio 3 - Auditoría con Tests Unitarios e Integración Web (40 puntos)

Previo a la puesta en producción, EcoTech Solutions debe certificar la precisión del algoritmo de cálculo de huella de carbono industrial. Tras auditar su comportamiento mediante pruebas automatizadas, dicho algoritmo debe integrarse en la tubería de datos que alimenta la interfaz web administrativa de la empresa.

**Punto A: Auditoría de Algoritmo de Emisiones (`unittest`):** A partir de la función `calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4)` (la cual eleva `ValueError` si el consumo es negativo), implementa la clase de prueba `TestCalculoEmisiones(unittest.TestCase)`. Diseña los casos de prueba necesarios para validar tanto la exactitud numérica del cálculo ante valores nominales como la correcta elevación de la excepción ante consumos fuera de rango.

**Punto B: Procesamiento de Métricas y Renderizado Web:** Incorpora la función `calcular_emisiones_carbono` en la función `obtener_metricas_consumo(registros)`, procesando un historial de consumos por planta industrial para determinar el total global de emisiones y la planta de mayor consumo. Por último, diseña la función de vista en Django `vista_panel_sustentabilidad(request)` que invoque dicho procesamiento y proporcione el diccionario de contexto listo para ser renderizado en la plantilla `sustentabilidad/panel.html`.
