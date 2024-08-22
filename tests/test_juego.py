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

    def test_reinicializacion_luego_de_movimiento(self):
        # Verifica que el juego se reinicia tras iniciarlo, mover, finalizar e iniciar nuevamente
        self.assertEqual(self.__juego__.turno, "blanco")
        self.assertEqual(self.__juego__.num_turno, 1)

        pieza = self.__juego__.get_pieza(6,0)

        self.__juego__.mover_pieza(6,0,4,0)
        self.__juego__.cambiar_turno()

        self.assertEqual(self.__juego__.get_pieza(4,0) , pieza)
        self.assertTrue(isinstance(self.__juego__.get_pieza(6,0), Casilla))
        self.assertEqual(self.__juego__.turno, "negro")
        self.assertEqual(self.__juego__.num_turno, 2)

        self.__juego__.finalizar_juego()

        self.__juego__.iniciar_juego()

        pieza = self.__juego__.get_pieza(6,0)

        self.assertEqual(self.__juego__.turno, "blanco")
        self.assertEqual(self.__juego__.num_turno, 1)
        self.assertEqual(self.__juego__.get_pieza(6,0) , pieza)
        self.assertTrue(isinstance(self.__juego__.get_pieza(4,0), Casilla))


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
        self.assertTrue(self.__juego__.validar_destino(6, 6, 5, 6))

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

        # Con solo el rey negro, se deberia declarar victoria de negro
        self.assertTrue(self.__juego__.checkVictoria())

        # Colocar una pieza adicional del color opuesto
        peon_blanco = Peon("blanco", 6, 6)
        self.__juego__.tablero.set_pieza(6, 6, peon_blanco)

        # Como sigue sin haber rey blanco, sigue siendo victoria de negro
        self.assertTrue(self.__juego__.checkVictoria())

        # Colocar un rey blanco
        rey_blanco = Rey("blanco", 0, 0)
        self.__juego__.tablero.set_pieza(0, 0, rey_blanco)

        # Como ambos reyes están en el tablero, no se declara victoria de nadie
        self.assertFalse(self.__juego__.checkVictoria())

    def test_finalizar_juego(self):
        # Verificar el reset de atributos al finalizar el juego
        self.__juego__.finalizar_juego()
        
        self.assertEqual(self.__juego__.tablero, None)
        self.assertEqual(self.__juego__.turno, None)
        self.assertEqual(self.__juego__.num_turno, None)



if __name__ == "__main__":
    unittest.main()
