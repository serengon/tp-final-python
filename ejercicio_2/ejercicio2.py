# Ejercicio 2 - Modelo de Productos, Excepciones y Persistencia
import json


# Punto A: Dominio del catálogo y reglas de inventario

# Guía M5-C2: excepción personalizada que hereda de Exception
class StockInvalidoError(Exception):
    """Lanzada cuando el stock viola las reglas de negocio."""
    pass


# Guía M3-C1: la clase se nombra en PascalCase
class DispositivoEcológico:
    def __init__(self, modelo: str, precio: float, stock: int):
        self.modelo = modelo
        self.precio = precio
        # Guía M3-C4: asignación segura usando el setter (valida desde el inicio)
        self.set_stock(stock)

    # Getter (Guía M3-C4)
    def get_stock(self) -> int:
        return self.__stock

    # Setter con regla de negocio (Guía M3-C4 + M5-C2)
    def set_stock(self, nuevo_stock: int):
        if nuevo_stock < 0:
            raise StockInvalidoError("El stock no puede tomar valores negativos.")
        self.__stock = nuevo_stock   # Guía M3-C4: atributo privado con doble guion bajo

    def obtener_ficha_tecnica(self) -> str:
        return f"Modelo: {self.modelo} | Precio: ${self.precio} | Stock: {self.get_stock()}"

    # Guía M4-C3: patrón DTO, convierte el objeto en un diccionario para json.dump
    def a_diccionario(self) -> dict:
        return {
            "tipo": "DispositivoEcológico",
            "modelo": self.modelo,
            "precio": self.precio,
            "stock": self.get_stock()
        }

    # Guía M3-C2: método mágico para print()
    def __str__(self) -> str:
        return self.obtener_ficha_tecnica()


# Guía M3-C3: herencia, PanelSolar es hija de DispositivoEcológico
class PanelSolar(DispositivoEcológico):
    def __init__(self, modelo: str, precio: float, stock: int, eficiencia_watts: int):
        # Delegamos los atributos comunes a la clase padre
        super().__init__(modelo, precio, stock)
        # Atributo propio del panel
        self.eficiencia_watts = eficiencia_watts

    # Guía M3-C4: polimorfismo, sobrescribimos la ficha técnica
    def obtener_ficha_tecnica(self) -> str:
        ficha_base = super().obtener_ficha_tecnica()
        return f"[PANEL SOLAR] {ficha_base} | Potencia: {self.eficiencia_watts}W"

    def a_diccionario(self) -> dict:
        datos = super().a_diccionario()
        datos["tipo"] = "PanelSolar"
        datos["eficiencia_watts"] = self.eficiencia_watts
        return datos


# Punto B: Persistencia y gestión del catálogo
class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos: list, ruta_archivo: str):
        # Convertimos cada objeto a diccionario (json.dump no acepta objetos propios)
        lista_diccionarios = []
        for dispositivo in lista_dispositivos:
            lista_diccionarios.append(dispositivo.a_diccionario())

        # Guía M4-C1 y M4-C2: with open + json.dump
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)

        print(f"Catálogo guardado en {ruta_archivo} ({len(lista_diccionarios)} productos)")


# Bloque de prueba
if __name__ == "__main__":
    productos_validos = []

    panel1 = PanelSolar("SolarMax-500", 1200.0, 10, 500)
    panel2 = PanelSolar("Solar-Pro", 950.0, 4, 330)
    termostato = DispositivoEcológico("Termostato-Smart", 350.0, 8)

    productos_validos.append(panel1)
    productos_validos.append(panel2)
    productos_validos.append(termostato)

    # Polimorfismo: el mismo método se comporta distinto según la clase
    print("---- FICHAS TÉCNICAS ----")
    for producto in productos_validos:
        print(producto.obtener_ficha_tecnica())

    # Guía M5-C2: captura controlada del error al crear con stock negativo
    print("\n---- PRUEBA DE STOCK INVÁLIDO ----")
    try:
        panel_roto = PanelSolar("Panel-Defectuoso", 800.0, -3, 250)
        productos_validos.append(panel_roto)   # no llega a ejecutarse
    except StockInvalidoError as error:
        print(f"[REGLA DE NEGOCIO MANEJADA]: {error}")

    # Captura controlada al modificar el stock de un producto que ya existe
    try:
        panel1.set_stock(-5)
    except StockInvalidoError as error:
        print(f"[REGLA DE NEGOCIO MANEJADA]: {error}")
    else:
        print("Stock actualizado")
    finally:
        print(f"El stock de {panel1.modelo} sigue siendo {panel1.get_stock()}")

    # Exportación final solo con los productos válidos
    print("\n---- EXPORTACIÓN ----")
    gestor = GestorInventario()
    gestor.guardar_catalogo_json(productos_validos, "catalogo_ecotech.json")
