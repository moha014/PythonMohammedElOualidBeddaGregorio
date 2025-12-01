r"""
test_palindromo.py
Módulo de tests unitarios para la función esPalindromo.
Prueba diversos casos incluyendo casos normales, casos límite y casos de error.

Última Modificación: 01/12/2024
Autor: Mohammed El Oualid Bedda
Dependencias: unittest, sys, os
"""
import unittest
import sys
import os

# Agregar el directorio src al path para importar nuestros módulos
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
))

from app.palindromo import esPalindromo


class TestEsPalindromo(unittest.TestCase):
    """
    Clase de tests para verificar el funcionamiento correcto de esPalindromo.
    Prueba casos normales, casos límite, casos con caracteres especiales,
    tildes, y casos de error.
    """
    
    # ==================== CASOS POSITIVOS - PALÍNDROMOS ====================
    
    def test_palindromo_simple_minusculas(self):
        """Prueba un palíndromo simple en minúsculas"""
        self.assertTrue(esPalindromo("aba"))
    
    def test_palindromo_simple_mayusculas(self):
        """Prueba que mayúsculas/minúsculas no afecten el resultado"""
        self.assertTrue(esPalindromo("ABA"))
    
    def test_palindromo_mixto_mayusculas_minusculas(self):
        """Prueba un palíndromo con mezcla de mayúsculas y minúsculas"""
        self.assertTrue(esPalindromo("Anilina"))
    
    def test_palindromo_con_espacios(self):
        """Prueba que los espacios se ignoren correctamente"""
        self.assertTrue(esPalindromo("a b a"))
    
    def test_palindromo_con_puntuacion(self):
        """Prueba que la puntuación se ignore correctamente"""
        self.assertTrue(esPalindromo("a,b,a"))
    
    def test_palindromo_con_tildes(self):
        """Prueba que las tildes se normalicen correctamente"""
        self.assertTrue(esPalindromo("Anilína"))
    
    def test_palindromo_con_dieresis(self):
        """Prueba que las diéresis se normalicen correctamente"""
        self.assertTrue(esPalindromo("Ü_ü"))
    
    def test_palindromo_complejo_espacios_puntuacion_mayusculas(self):
        """Prueba un palíndromo complejo con espacios, puntuación y mayúsculas"""
        self.assertTrue(esPalindromo("A man, a plan, a canal: Panama"))
    
    def test_palindromo_numeros(self):
        """Prueba que los números se consideren correctamente"""
        self.assertTrue(esPalindromo("12321"))
    
    def test_palindromo_numeros_con_caracteres(self):
        """Prueba palíndromos con números y caracteres alfabéticos"""
        self.assertTrue(esPalindromo("a1b1a"))
    
    def test_palindromo_letra_unica(self):
        """Prueba que una sola letra sea palíndroma"""
        self.assertTrue(esPalindromo("a"))
    
    def test_palindromo_dos_letras_iguales(self):
        """Prueba que dos letras iguales formen un palíndromo"""
        self.assertTrue(esPalindromo("aa"))
    
    def test_palindromo_oracion_larga_clasica(self):
        """Prueba una oración palíndroma clásica en español"""
        self.assertTrue(esPalindromo("Dábale arroz a la zorra el abad"))
    
    def test_palindromo_numerico_largo(self):
        """Prueba un palíndromo numérico largo"""
        self.assertTrue(esPalindromo("9876543210123456789"))
    
    # ==================== CASOS NEGATIVOS - NO PALÍNDROMOS ====================
    
    def test_no_palindromo_simple(self):
        """Prueba que una palabra no palíndroma retorna False"""
        self.assertFalse(esPalindromo("abc"))
    
    def test_no_palindromo_palabras_diferentes(self):
        """Prueba que palabras diferentes retornen False"""
        self.assertFalse(esPalindromo("hola mundo"))
    
    def test_no_palindromo_casi_palindromo(self):
        """Prueba un casi-palíndromo que no lo es"""
        self.assertFalse(esPalindromo("abac"))
    
    def test_no_palindromo_orden_inverso(self):
        """Prueba palabras en orden claramente invertido"""
        self.assertFalse(esPalindromo("python"))
    
    # ==================== CASOS LÍMITE ====================
    
    def test_cadena_vacia(self):
        """Prueba que una cadena vacía sea palíndroma (por vacuidad)"""
        self.assertTrue(esPalindromo(""))
    
    def test_solo_espacios(self):
        """Prueba que una cadena con solo espacios sea palíndroma"""
        self.assertTrue(esPalindromo("   "))
    
    def test_solo_puntuacion(self):
        """Prueba que una cadena con solo puntuación sea palíndroma"""
        self.assertTrue(esPalindromo(".,;!?"))
    
    def test_espacios_y_puntuacion_sin_letras(self):
        """Prueba cadenas sin caracteres alfanuméricos"""
        self.assertTrue(esPalindromo("   .,;   "))
    
    def test_cadena_con_caracteres_especiales_unicode(self):
        """Prueba caracteres Unicode especiales"""
        self.assertTrue(esPalindromo("©®™"))
    
    # ==================== CASOS DE ERROR ====================
    
    def test_entrada_no_es_cadena_es_entero(self):
        """Prueba que TypeError se lanza cuando se pasa un entero"""
        with self.assertRaises(TypeError):
            esPalindromo(123)
    
    def test_entrada_no_es_cadena_es_lista(self):
        """Prueba que TypeError se lanza cuando se pasa una lista"""
        with self.assertRaises(TypeError):
            esPalindromo(['a', 'b', 'a'])
    
    def test_entrada_no_es_cadena_es_none(self):
        """Prueba que TypeError se lanza cuando se pasa None"""
        with self.assertRaises(TypeError):
            esPalindromo(None)
    
    def test_entrada_no_es_cadena_es_diccionario(self):
        """Prueba que TypeError se lanza cuando se pasa un diccionario"""
        with self.assertRaises(TypeError):
            esPalindromo({'key': 'value'})
    
    def test_entrada_no_es_cadena_es_flotante(self):
        """Prueba que TypeError se lanza cuando se pasa un float"""
        with self.assertRaises(TypeError):
            esPalindromo(3.14)
    
    # ==================== CASOS PARAMETRIZADOS ====================
    
    def test_parametrizados_palindromos_validos(self):
        """
        Prueba parametrizada para múltiples palíndromos válidos.
        Esto permite agregar fácilmente más casos de prueba.
        """
        casos_validos = [
            "aba",
            "ABA",
            "Anilina",
            "radar",
            "Radar",
            "12321",
            "1",
            "aa",
            "a",
            "",
            "   ",
            "a-b-a",
            "A, B, A",
        ]
        
        for cadena in casos_validos:
            with self.subTest(cadena=cadena):
                self.assertTrue(
                    esPalindromo(cadena),
                    f"Se esperaba que '{cadena}' fuera palíndroma"
                )
    
    def test_parametrizados_no_palindromos(self):
        """
        Prueba parametrizada para cadenas que NO son palíndromos.
        """
        casos_no_validos = [
            "abc",
            "abcd",
            "hola",
            "python",
            "hello",
            "mundo",
            "test",
            "12345",
        ]
        
        for cadena in casos_no_validos:
            with self.subTest(cadena=cadena):
                self.assertFalse(
                    esPalindromo(cadena),
                    f"Se esperaba que '{cadena}' NO fuera palíndroma"
                )
    
    def test_parametrizados_tipos_invalidos(self):
        """
        Prueba parametrizada para verificar que se lanza TypeError
        con diferentes tipos de datos inválidos.
        """
        casos_invalidos = [
            123,
            45.67,
            None,
            [],
            {},
            ('a', 'b'),
            {'a': 1},
        ]
        
        for valor in casos_invalidos:
            with self.subTest(valor=valor, tipo=type(valor).__name__):
                with self.assertRaises(TypeError):
                    esPalindromo(valor)


class TestEsPalindromoIntegracion(unittest.TestCase):
    """
    Clase de tests de integración para verificar el comportamiento
    completo de la función en escenarios más realistas.
    """
    
    def test_casos_reales_frases_palindromas(self):
        """
        Prueba con frases palindrómicas reales en español e inglés.
        Estas son frases que en la vida real podrían ser ingresadas.
        """
        # Frases palindrómicas reales verificadas
        frases_palindromas = [
            "Dábale arroz a la zorra el abad",
            "A man a plan a canal Panama",
            "Radar",
        ]
        
        for frase in frases_palindromas:
            with self.subTest(frase=frase):
                resultado = esPalindromo(frase)
                self.assertTrue(
                    resultado,
                    f"La frase '{frase}' debería ser palíndroma"
                )
    
    def test_entrada_usuario_tipica(self):
        """
        Simula entrada típica de un usuario en el programa interactivo.
        Incluye errores de tipeo, espacios extra, etc.
        """
        entrada_usuario = "   Radar   "  # Con espacios extra
        self.assertTrue(esPalindromo(entrada_usuario))
        
        entrada_usuario = "A,b,A"  # Con puntuación
        self.assertTrue(esPalindromo(entrada_usuario))
        
        entrada_usuario = "Anilina"  # Una palabra palíndroma válida
        self.assertTrue(esPalindromo(entrada_usuario))


if __name__ == '__main__':
    # Ejecutar los tests con mayor detalle
    unittest.main(verbosity=2)
