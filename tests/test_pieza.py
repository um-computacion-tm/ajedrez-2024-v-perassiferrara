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



class TestPieza(unittest.TestCase):


    def setUp(self):
        self.__juego__ = JuegoAjedrez()

    def test_mover_pieza_exito(self): # Con este método solo se cambian las coordenadas internas
        torre = self.__juego__.get_pieza(0, 0)
        torre.mover(3, 0)
        self.assertEqual((torre.x,torre.y), (3, 0))
        torre.mover(0, 0)
        self.assertEqual((torre.x,torre.y), (0, 0))
        torre.mover(8, 3)
        self.assertEqual((torre.x,torre.y), (8, 3))

    def test_check_misma_casilla(self):
        with self.assertRaises(ValueError):
            self.__juego__.checkMismaCasilla(0, 0, 0, 0)

    def test_check_destino_pieza_rival(self):
        pieza = Torre("blanco", 0, 0)
        pieza_destino = Peon("negro", 2, 0)
        self.assertTrue(self.__juego__.tablero.checkDestino(pieza, pieza_destino))

    def test_check_destino_vacio(self):
        pieza = Torre("blanco", 0, 0)
        pieza_destino = Casilla(2, 0)
        self.assertFalse(self.__juego__.tablero.checkDestino(pieza, pieza_destino))

    def test_peon_primer_movimiento(self):
        peon = self.__juego__.get_pieza(6, 0)
        self.assertTrue(self.__juego__.mover_pieza(6, 0, 4, 0))
        self.assertEqual((peon.x,peon.y), (4, 0))

if __name__ == "__main__":
    unittest.main()