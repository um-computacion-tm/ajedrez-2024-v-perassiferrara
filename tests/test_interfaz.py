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
from unittest.mock import patch, MagicMock

class TestTraducirCoordenadas(unittest.TestCase):

    def setUp(self):
        self.__interfaz__ = CLI()

    def test_traducir_a_coordenadas_valida(self):
        self.assertEqual(self.__interfaz__.traducir_a_coordenadas("A8"), (0, 0))
        self.assertEqual(self.__interfaz__.traducir_a_coordenadas("H1"), (7, 7))
        self.assertEqual(self.__interfaz__.traducir_a_coordenadas("D5"), (3, 3))

    def test_traducir_a_coordenadas_invalida(self):
        with self.assertRaises(ValueError):
            self.__interfaz__.traducir_a_coordenadas("Z9")
            self.__interfaz__.traTestInterfazducir_a_coordenadas("D0")
            self.__interfaz__.traducir_a_coordenadas("A14")
            self.__interfaz__.traducir_a_coordenadas("H-1")
            self.__interfaz__.traducir_a_coordenadas("D-5")

    def test_traducir_a_posicion(self):
        self.assertEqual(self.__interfaz__.traducir_a_posicion(0, 0), "A8")
        self.assertEqual(self.__interfaz__.traducir_a_posicion(7, 7), "H1")
        self.assertEqual(self.__interfaz__.traducir_a_posicion(3, 3), "D5")

class TestMenuPrincipal(unittest.TestCase):

    def setUp(self):
        self.__interfaz__ = CLI()

    # Cerrar juego desde menu principal
    @patch('builtins.input', side_effect=["2"])
    @patch('builtins.print')
    def test_menu_principal_cerrar_juego(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            main()

        self.assertEqual(mock_input.call_count, 1) # El flujo incluye 1 llamada a input
        self.assertEqual(mock_print.call_count, 6) # El flujo incluye 6 llamadas a print

    # Iniciar juego, terminar en empate y cerrar
    @patch('builtins.input', side_effect=["1", "2", "2"])
    @patch('builtins.print') 
    def test_menu_principal(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            main()

        self.assertEqual(mock_input.call_count, 3) # El flujo incluye 3 llamadas a input
        self.assertEqual(mock_print.call_count, 18) # El flujo incluye 18 llamadas a print



if __name__ == "__main__":
    unittest.main()