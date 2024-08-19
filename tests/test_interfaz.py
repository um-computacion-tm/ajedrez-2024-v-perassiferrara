import unittest
from juego.interfaz import *
from juego.juego import *
from juego.excepciones import *
from juego.tablero import *
from juego.pieza import *
from juego.casilla import *
from juego.peon import *
from juego.torre import *
from juego.caballo import *
from juego.alfil import *
from juego.dama import *
from juego.rey import *


class TestInterfaz(unittest.TestCase):

    def setUp(self):
        self.__juego__ = JuegoAjedrez()

    def test_traducir_a_coordenadas_valida(self):
        interfaz = CLI()
        self.assertEqual(interfaz.traducir_a_coordenadas("A8"), (0, 0))
        self.assertEqual(interfaz.traducir_a_coordenadas("H1"), (7, 7))
        self.assertEqual(interfaz.traducir_a_coordenadas("D5"), (3, 3))

    def test_traducir_a_coordenadas_invalida(self):
        interfaz = CLI()
        with self.assertRaises(ValueError):
            interfaz.traducir_a_coordenadas("Z9")

    def test_traducir_a_posicion(self):
        interfaz = CLI()
        self.assertEqual(interfaz.traducir_a_posicion(0, 0), "A8")
        self.assertEqual(interfaz.traducir_a_posicion(7, 7), "H1")
        self.assertEqual(interfaz.traducir_a_posicion(3, 3), "D5")



if __name__ == "__main__":
    unittest.main()