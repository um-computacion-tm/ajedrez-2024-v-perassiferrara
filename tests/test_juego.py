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


class TestJuego(unittest.TestCase):

    def setUp(self):
        self.__juego__ = JuegoAjedrez()

    def test_inicializacion_juego(self):
        # Verifica que el juego se inicia correctamente
        self.assertEqual(self.__juego__.turno, "blanco")
        self.assertEqual(self.__juego__.num_turno, 1)
        self.assertIsInstance(self.__juego__.tablero, Tablero)

    def test_cambiar_turno(self):
        # Verifica que el turno cambie correctamente
        self.__juego__.cambiar_turno()
        self.assertEqual(self.__juego__.turno, "negro")
        self.assertEqual(self.__juego__.num_turno, 2)
        self.__juego__.cambiar_turno()
        self.assertEqual(self.__juego__.turno, "blanco")
        self.assertEqual(self.__juego__.num_turno, 3)
        self.__juego__.cambiar_turno()
        self.__juego__.cambiar_turno()
        self.assertEqual(self.__juego__.turno, "blanco")
        self.assertEqual(self.__juego__.num_turno, 5)

    def test_seleccionar_opcion(self):
        # Verifica la selección de opciones
        self.assertEqual(self.__juego__.seleccionar_opcion("1"), "Juego iniciado")
        self.assertEqual(self.__juego__.seleccionar_opcion("2"), "Cerrando juego")
        self.assertEqual(self.__juego__.seleccionar_opcion("3"), "Opción no válida")

    def test_validar_origen(self):
        # Colocar una pieza en el tablero para las pruebas
        peon_blanco = Peon("blanco", 1, 1)
        self.__juego__.tablero.set_pieza(1, 1, peon_blanco)

        # Verifica que la validación del origen funcione correctamente
        self.assertEqual(self.__juego__.validar_origen(1, 1), peon_blanco)

        # Casilla vacía debería lanzar excepción
        with self.assertRaises(EmptyError):
            self.__juego__.validar_origen(3, 3)

        # Seleccionar una pieza del color incorrecto debería lanzar excepción
        peon_negro = Peon("negro", 6, 6)
        self.__juego__.tablero.set_pieza(6, 6, peon_negro)
        with self.assertRaises(ColorError):
            self.__juego__.validar_origen(6, 6)

    def test_validar_destino(self):
        # Colocar piezas en el tablero para las pruebas
        peon_blanco = Peon("blanco", 1, 1)
        self.__juego__.tablero.set_pieza(1, 1, peon_blanco)
        peon_negro = Peon("negro", 2, 2)
        self.__juego__.tablero.set_pieza(2, 2, peon_negro)

        # Movimiento válido
        self.assertIsNone(self.__juego__.validar_destino(6, 6, 5, 6))

        # Mover a la misma casilla debería lanzar excepción
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(1, 1, 1, 1)

    def test_mover_pieza(self):
        # Colocar piezas en el tablero para las pruebas
        peon_blanco = Peon("blanco", 1, 1)
        self.__juego__.tablero.set_pieza(1, 1, peon_blanco)

        # Mover pieza correctamente
        self.assertTrue(self.__juego__.mover_pieza(1, 1, 2, 1))

    def test_checkVictoria(self):
        # Colocar solo un rey negro en el tablero
        self.__juego__.tablero.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]
        
        self.__juego__.cambiar_turno()
        rey_negro = Rey("negro", 7, 7)
        self.__juego__.tablero.set_pieza(7, 7, rey_negro)

        # Con solo el rey del oponente, debería declarar victoria
        self.assertTrue(self.__juego__.checkVictoria())

        # Colocar una pieza adicional del color opuesto
        peon_blanco = Peon("blanco", 6, 6)
        self.__juego__.tablero.set_pieza(6, 6, peon_blanco)

        # No debería declarar victoria porque aún hay piezas oponentes
        self.assertFalse(self.__juego__.checkVictoria())

    def test_finalizar_juego(self):
        # Verificar el mensaje al finalizar el juego
        self.assertEqual(self.__juego__.finalizar_juego(), "\nJuego terminado: Empate\n")



if __name__ == "__main__":
    unittest.main()
