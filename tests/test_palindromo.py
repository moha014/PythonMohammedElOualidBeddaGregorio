import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
))

from app.palindromo import esPalindromo


class TestEsPalindromo(unittest.TestCase):
    
    def test_aba(self):
        self.assertTrue(esPalindromo("aba"))
    
    def test_aba_mayuscula(self):
        self.assertTrue(esPalindromo("ABA"))
    
    def test_anilina(self):
        self.assertTrue(esPalindromo("Aba"))
    
    def test_con_espacios(self):
        self.assertTrue(esPalindromo("a b a"))
    
    def test_con_comas(self):
        self.assertTrue(esPalindromo("a,b,a"))
    
    def test_con_tildes(self):
        self.assertTrue(esPalindromo("Oso"))
    
    def test_numeros(self):
        self.assertTrue(esPalindromo("12321"))
    
    def test_una_letra(self):
        self.assertTrue(esPalindromo("a"))
    
    def test_dos_letras(self):
        self.assertTrue(esPalindromo("aa"))
    
    def test_frase_conocida(self):
        self.assertTrue(esPalindromo("Anilina"))
    
    def test_abc(self):
        self.assertFalse(esPalindromo("abc"))
    
    def test_hola_mundo(self):
        self.assertFalse(esPalindromo("hola mundo"))
    
    def test_python(self):
        self.assertFalse(esPalindromo("python"))
    
    def test_vacia(self):
        self.assertTrue(esPalindromo(""))
    
    def test_solo_espacios(self):
        self.assertTrue(esPalindromo("   "))
    
    def test_solo_puntos(self):
        self.assertTrue(esPalindromo(".,;!?"))
    
    def test_entero(self):
        with self.assertRaises(TypeError):
            esPalindromo(123)
    
    def test_lista(self):
        with self.assertRaises(TypeError):
            esPalindromo(['a', 'b', 'a'])
    
    def test_none(self):
        with self.assertRaises(TypeError):
            esPalindromo(None)
    
    def test_diccionario(self):
        with self.assertRaises(TypeError):
            esPalindromo({'key': 'value'})
    
    def test_flotante(self):
        with self.assertRaises(TypeError):
            esPalindromo(3.14)


if __name__ == '__main__':
    unittest.main()
