# Ejercicio 3 - Punto A: Auditoría con unittest (Guía M5-C1)
import unittest
from sustentabilidad.emisiones import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    # Pruebas de casos nominales (exactitud numérica)
    def test_calculo_correcto(self):
        resultado = calcular_emisiones_carbono(100.0, 0.4)
        self.assertEqual(resultado, 40.0)

    def test_usa_factor_por_defecto(self):
        resultado = calcular_emisiones_carbono(1000.0)
        self.assertEqual(resultado, 400.0)

    def test_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(200.0, 0.5)
        self.assertEqual(resultado, 100.0)

    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0)

    def test_valor_con_decimales(self):
        resultado = calcular_emisiones_carbono(0.1)
        # Con decimales se usa assertAlmostEqual porque 0.1 * 0.4 no da exacto 0.04
        self.assertAlmostEqual(resultado, 0.04)

    # Pruebas de excepción (consumos fuera de rango)
    def test_consumo_negativo_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50.0)

    def test_consumo_apenas_negativo_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-0.1)


if __name__ == "__main__":
    unittest.main()
