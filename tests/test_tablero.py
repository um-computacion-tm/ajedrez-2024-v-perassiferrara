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



class TestTablero(unittest.TestCase):

    def setUp(self):
        self.__juego__ = JuegoAjedrez()

    def test_inicializar_piezas(self):
        piezas_inicio = (
            (0, 0, Torre), (0, 1, Caballo), (0, 2, Alfil), (0, 3, Dama), 
            (0, 4, Rey), (0, 5, Alfil), (0, 6, Caballo), (0, 7, Torre),
            (1, 0, Peon), (1, 1, Peon), (1, 2, Peon), (1, 3, Peon), 
            (1, 4, Peon), (1, 5, Peon), (1, 6, Peon), (1, 7, Peon),
            (6, 0, Peon), (6, 1, Peon), (6, 2, Peon), (6, 3, Peon), 
            (6, 4, Peon), (6, 5, Peon), (6, 6, Peon), (6, 7, Peon),
            (7, 0, Torre), (7, 1, Caballo), (7, 2, Alfil), (7, 3, Dama), 
            (7, 4, Rey), (7, 5, Alfil), (7, 6, Caballo), (7, 7, Torre)
        )
            
        for x, y, tipo_pieza in piezas_inicio:
            pieza = self.__juego__.get_pieza(x, y)
            self.assertIsInstance(pieza, tipo_pieza)

    def test_check_victoria(self):
        self.__juego__.tablero.set_pieza(0, 0, Torre("negro", 0, 0))
        self.__juego__.tablero.set_pieza(1, 0, Peon("negro", 1, 0))
        self.assertFalse(self.__juego__.checkVictoria())

    def test_check_victoria_2(self):
        self.__juego__.tablero.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]
        pieza_blanca = Torre("blanco", 7, 7)
        pieza_negra = Torre("negro", 0, 0)
        self.__juego__.tablero.set_pieza(7, 7, pieza_blanca)
        self.__juego__.tablero.set_pieza(0, 0, pieza_negra)
        self.__juego__.tablero.set_pieza(0, 0, Casilla(0, 0))
        self.assertTrue(self.__juego__.checkVictoria())

if __name__ == "__main__":
    unittest.main()