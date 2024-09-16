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
from unittest.mock import patch

class TestTraducirCoordenadas(unittest.TestCase):

    def setUp(self):
        self.__interfaz__ = CLI()

    def test_traducir_a_coordenadas_valida(self):
        self.assertEqual(self.__interfaz__.traducir_a_coordenadas("A8"), (0, 0))
        self.assertEqual(self.__interfaz__.traducir_a_coordenadas("H1"), (7, 7))
        self.assertEqual(self.__interfaz__.traducir_a_coordenadas("D5"), (3, 3))

    def test_traducir_a_coordenadas_invalida(self):
        with self.assertRaises(CoordinatesError):
            self.__interfaz__.traducir_a_coordenadas("Z9")
            self.__interfaz__.traTestInterfazducir_a_coordenadas("D0")
            self.__interfaz__.traducir_a_coordenadas("A14")
            self.__interfaz__.traducir_a_coordenadas("H-1")
            self.__interfaz__.traducir_a_coordenadas("D-5")

    def test_traducir_a_posicion(self):
        self.assertEqual(self.__interfaz__.traducir_a_posicion(0, 0), "A8")
        self.assertEqual(self.__interfaz__.traducir_a_posicion(7, 7), "H1")
        self.assertEqual(self.__interfaz__.traducir_a_posicion(3, 3), "D5")


class TestMenusIniciales(unittest.TestCase):

    def setUp(self):
        self.__interfaz__ = CLI()

    # Cerrar juego desde menu principal
    @patch('builtins.input', side_effect=["2"])
    @patch('builtins.print')
    def test_menu_principal_cerrar_juego(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            main()

        self.assertEqual(mock_print.call_count, 2) # El flujo incluye 2 llamadas a print
        self.assertEqual(mock_input.call_count, 1) # El flujo incluye 1 llamada a input

    # Ingresar valores inválidos para input y cerrar
    @patch('builtins.input', side_effect=["a", "", " ", "3", "48949", "#$%&(!())", "2"])
    @patch('builtins.print')
    def test_menu_principal_no_valido(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            main()

        self.assertEqual(mock_print.call_count, 14) # El flujo incluye 14 llamada a print

        mock_print.assert_any_call("\nOpción no valida\n")
        # El flujo llama al menos una vez a un print con este contenido, ya que se atrapo la excepcion

        self.assertEqual(mock_input.call_count, 7) # El flujo incluye 7 llamadas a input

    # Iniciar juego, terminar en empate y cerrar
    @patch('builtins.input', side_effect=["1", "2", "2"])
    @patch('builtins.print') 
    def test_menu_juego_cerrar_juego(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            main()

        self.assertEqual(mock_print.call_count, 6) # El flujo incluye 6 llamadas a print
        self.assertEqual(mock_input.call_count, 3) # El flujo incluye 3 llamadas a input
        
    # Iniciar juego, ingresar valores inválidos para input y cerrar
    @patch('builtins.input', side_effect=["1", "", " ", "3", "48949", "#$%&(!())", "2", "2"])
    @patch('builtins.print')
    def test_menu_juego_no_valido(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            main()

        self.assertEqual(mock_print.call_count, 11) # El flujo incluye 11 llamadas a print

        self.assertEqual(mock_input.call_count, 8) # El flujo incluye 8 llamadas a input 
    

class TestMenuSeleccionMovimiento(unittest.TestCase):
    
    def setUp(self):
        self.__interfaz__ = CLI()
    
    # Iniciar juego, ingresar a menu de seleccion, mover correctamente, terminar en empate y cerrar
    @patch('builtins.input', side_effect=["1", "1", "a2", "a4", "2", "2"])
    @patch('builtins.print') 
    def test_menu_seleccion_cerrar_juego(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            main()

        self.assertEqual(mock_print.call_count, 14) # El flujo incluye 14 llamadas a print
        self.assertEqual(mock_input.call_count, 6) # El flujo incluye 6 llamadas a input

    # Iniciar juego, ingresar a menu de seleccion, ingresar valores inválidos y cerrar
    @patch('builtins.input', side_effect=["1", "1", "", "2", "2"])
    @patch('builtins.print')
    def test_menu_seleccion_no_valido(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            main()

        self.assertEqual(mock_print.call_count, 10) # El flujo incluye 10 llamada a print
        
        mock_print.assert_any_call("Posición no válida. Use casillas del tablero (a-h y 1-8)\n")
        # El flujo llama al menos una vez a un print con este contenido, ya que se atrapo la excepcion
        
        self.assertEqual(mock_input.call_count, 5) # El flujo incluye 5 llamadas a input 

    """Iniciar juego, input inválido, seleccionar pieza, mover con destino incorrecto, mover correctamente,
    terminar en empate, iniciar juego, mover la misma pieza correctamente, capturar correctamente, empate y cerrar"""

    @patch('builtins.input', side_effect=["1", "}\½@\½@ ", "", "1", "a2", "A6", "1", "A2", "a4", "2", "1", "1", "a2", "a4", "1", "b7", "b5", "1", "a4", "b5", "2", "2"])
    @patch('builtins.print')
    def test_menus_con_errores_con_reintentos(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            main()

        self.assertEqual(mock_print.call_count, 50)
        self.assertEqual(mock_input.call_count, 22)
        
        mock_print.assert_any_call("Movimiento inválido para el peón.\n")
        # El flujo llama al menos una vez a un print con este contenido, ya que se atrapó la excepcion

        mock_print.assert_any_call("Peón blanco A4 captura a Peón negro en B5\n")

        mock_print.assert_any_call("Peón blanco A2 se mueve a A4\n")
        # El flujo llama al menos una vez a un print con este contenido, ya que se movió una pieza

        mock_print.assert_any_call("\nJuego terminado: Empate\n")
        # El flujo llama al menos una vez a un print con este contenido, ya que el juego terminó en empate

        self.assertEqual


    """Iniciar juego, múltiples movimientos correctos hasta que
    el rey negro es capturado (que conduce a victoria de blanco) y cerrar"""

    @patch('builtins.input', side_effect=["1", "1", "e2 ", " e3", "1", " D7 ", "d5", "1", "f1", "B5 ", "1", "a7", "a5", "1", "b5", "e8", "2"])
    @patch('builtins.print')
    def test_menu_seleccion_iniciar_juego_victoria(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            main()

        self.assertEqual(mock_print.call_count, 45)
        self.assertEqual(mock_input.call_count, 17)

        mock_print.assert_any_call("¡El jugador blanco ha ganado!\n")
        # El flujo llama al menos una vez a un print con este contenido, ya que el juego terminó en victoria de blanco

if __name__ == "__main__":
    unittest.main()