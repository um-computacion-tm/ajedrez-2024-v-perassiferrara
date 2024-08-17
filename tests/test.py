import unittest
from unittest.mock import patch

from clases.tablero import *
from clases.excepciones import *
from clases.pieza import *
from clases.casilla import *
from clases.peon import *
from clases.torre import *
from clases.caballo import *
from clases.alfil import *
from clases.dama import *
from clases.rey import *

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.__tablero__ = Tablero()

    def test_inicializar_piezas(self):
        piezas_inicio = {
            "A8": Torre, "B8": Caballo, "C8": Alfil, "D8": Dama, "E8": Rey, "F8": Alfil, "G8": Caballo, "H8": Torre,
            "A7": Peon, "B7": Peon, "C7": Peon, "D7": Peon, "E7": Peon, "F7": Peon, "G7": Peon, "H7": Peon,
            "A1": Torre, "B1": Caballo, "C1": Alfil, "D1": Dama, "E1": Rey, "F1": Alfil, "G1": Caballo, "H1": Torre,
            "A2": Peon, "B2": Peon, "C2": Peon, "D2": Peon, "E2": Peon, "F2": Peon, "G2": Peon, "H2": Peon
        }
        for posicion, tipo_pieza in piezas_inicio.items():
            x, y = self.__tablero__.traducir_a_coordenadas(posicion)
            pieza = self.__tablero__.cuadricula(x, y)
            self.assertIsInstance(pieza, tipo_pieza, f"La pieza en {posicion} debería ser {tipo_pieza.__name__}.")

    def test_cambiar_turno(self):
        self.assertEqual(self.__tablero__.turno, "blanco")
        self.__tablero__.cambiar_turno()
        self.assertEqual(self.__tablero__.turno, "negro")
        self.__tablero__.cambiar_turno()
        self.assertEqual(self.__tablero__.turno, "blanco")

    def test_traducir_a_coordenadas_valida(self):
        self.assertEqual(self.__tablero__.traducir_a_coordenadas("A8"), (0, 0))
        self.assertEqual(self.__tablero__.traducir_a_coordenadas("H1"), (7, 7))
        self.assertEqual(self.__tablero__.traducir_a_coordenadas("D5"), (3, 3))

    def test_traducir_a_coordenadas_invalida(self):
        with self.assertRaises(ValueError):
            self.__tablero__.traducir_a_coordenadas("Z9")

    def test_traducir_a_posicion(self):
        self.assertEqual(self.__tablero__.traducir_a_posicion(0, 0), "A8")
        self.assertEqual(self.__tablero__.traducir_a_posicion(7, 7), "H1")
        self.assertEqual(self.__tablero__.traducir_a_posicion(3, 3), "D5")

    def test_seleccionar_pieza_exito(self):
        pieza = self.__tablero__.seleccionarPieza("A1")
        self.assertIsInstance(pieza, Torre)
        self.assertEqual(pieza.color, "blanco")

    def test_seleccionar_pieza_casilla_vacia(self):
        with self.assertRaises(EmptyError):
            self.__tablero__.seleccionarPieza("A6")

    def test_seleccionar_pieza_oponente(self):
        self.__tablero__.cambiar_turno()  # Cambia el turno a "negro"
        with self.assertRaises(ColorError):
            self.__tablero__.seleccionarPieza("A1")

class TestPieza(unittest.TestCase):

    @patch("builtins.print")
    def test_mover_pieza_exito(self, mock_print):
        self.__tablero__.cambiarTurno()  # Cambia el turno a "negro"
        self.__tablero__.__cuadricula__[1][0] = Casilla(1, 0)
        torre = self.__tablero__.seleccionarPieza("A8")
        self.assertTrue(torre.mover("A6", self.__tablero__))
        self.assertEqual(self.__tablero__.cuadricula(2, 0), torre)
        self.assertIsInstance(self.__tablero__.cuadricula(0, 0), Casilla)

    def test_mover_pieza_destino_ocupado_aliado(self):
        torre = self.__tablero__.seleccionarPieza("A1")
        with self.assertRaises(ValueError):
            torre.mover("A2", self.__tablero__)

    @patch("builtins.print")
    def test_mover_pieza_destino_ocupado_rival(self, mock_print):
        self.__tablero__.cambiarTurno()  # Cambia al turno de las piezas negras
        self.__tablero__.__cuadricula__[1][0] = Casilla(1, 0)
        torre_negra = self.__tablero__.seleccionarPieza("A8")
        self.assertTrue(torre_negra.mover("A2", self.__tablero__))

    def test_check_victoria(self):
        self.__tablero__.set_cuadricula(0, 0, Torre("blanco", 0, 0))
        self.__tablero__.set_cuadricula(1, 0, Peon("negro", 1, 0))
        self.assertFalse(self.__tablero__.checkVictoria())

    @patch("builtins.print")
    def test_check_victoria2(self, mock_print):
        self.__tablero__.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]
        pieza_blanca = Torre("blanco", 7, 7)
        pieza_negra = Torre("negro", 0, 0)
        self.__tablero__.set_cuadricula(7, 7, pieza_blanca)
        self.__tablero__.set_cuadricula(0, 0, pieza_negra)
        self.__tablero__.set_cuadricula(0, 0, Casilla(0, 0))
        self.assertTrue(self.__tablero__.checkVictoria())

    def test_mostrarTurno(self):
        self.assertEqual(self.__tablero__.turno, "blanco")
        self.assertEqual(self.__tablero__.num_turno, 1)
        self.__tablero__.cambiarTurno()
        self.assertEqual(self.__tablero__.turno, "negro")
        self.assertEqual(self.__tablero__.num_turno, 2)

class TestChecksPiezas(unittest.TestCase):
    
    def setUp(self):
        self.tablero = Tablero()

    def test_set_x_valido(self):
        pieza = Torre("blanco", 0, 0)
        pieza.set_x(4)
        self.assertEqual(pieza.x, 4)

    def test_set_y_valido(self):
        pieza = Torre("blanco", 0, 0)
        pieza.set_y(4)
        self.assertEqual(pieza.y, 4)

    def test_check_misma_casilla(self):
        pieza = Torre("blanco", 0, 0)
        with self.assertRaises(ValueError):
            pieza.checkMismaCasilla(0, 0)

    def test_check_destino_pieza_rival(self):
        pieza = Torre("blanco", 0, 0)
        self.tablero.set_pieza(2, 0, Peon("negro", 2, 0))
        self.assertTrue(pieza.checkDestino(2, 0, self.tablero))

    def test_check_destino_pieza_aliada(self):
        pieza = Torre("blanco", 0, 0)
        self.tablero.set_pieza(2, 0, Peon("blanco", 2, 0))
        with self.assertRaises(ValueError):
            pieza.checkDestino(2, 0, self.tablero)

class TestMovimientosPiezas(unittest.TestCase):
    
    def setUp(self):
        self.__tablero__ = Tablero()

    @patch("builtins.print")
    def test_check_movimiento_torre(self, mock_print):
            # Limpia el tablero
        self.__tablero__.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]
        
        torre = Torre("blanco", 0, 0)
        self.__tablero__.set_pieza(0, 0, torre)
        # Movimiento válido
        self.assertTrue(torre.checkMovimiento(0, 5, self.__tablero__))  # Movimiento vertical
        self.assertTrue(torre.checkMovimiento(5, 0, self.__tablero__))  # Movimiento horizontal
        # Movimiento inválido
        self.assertFalse(torre.checkMovimiento(2, 2, self.__tablero__))  # Movimiento diagonal

    @patch("builtins.print")
    def test_check_movimiento_caballo(self, mock_print):
        caballo = Caballo("blanco", 0, 0)
        self.__tablero__.set_pieza(0, 0, caballo)
        # Movimiento válido
        self.assertTrue(caballo.checkMovimiento(2, 1, self.__tablero__))  # Movimiento en L
        self.assertTrue(caballo.checkMovimiento(1, 2, self.__tablero__))  # Movimiento en L
        # Movimiento inválido
        self.assertFalse(caballo.checkMovimiento(0, 1, self.__tablero__))  # Movimiento en línea recta

    @patch("builtins.print")
    def test_check_movimiento_alfil(self, mock_print):
                    # Limpia el tablero
        self.__tablero__.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]

        alfil = Alfil("blanco", 0, 0)
        self.__tablero__.set_pieza(0, 0, alfil)
        # Movimiento válido
        self.assertTrue(alfil.checkMovimiento(3, 3, self.__tablero__))  # Movimiento diagonal
        # Movimiento inválido
        self.assertFalse(alfil.checkMovimiento(0, 1, self.__tablero__))  # Movimiento vertical

    @patch("builtins.print")
    def test_check_movimiento_dama(self, mock_print):
                    # Limpia el tablero
        self.__tablero__.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]

        dama = Dama("blanco", 0, 0)
        
        self.__tablero__.set_pieza(0, 0, dama)
        # Movimiento válido
        self.assertTrue(dama.checkMovimiento(0, 5, self.__tablero__))  # Movimiento horizontal
        self.assertTrue(dama.checkMovimiento(5, 5, self.__tablero__))  # Movimiento diagonal
        # Movimiento inválido
        self.assertFalse(dama.checkMovimiento(1, 2, self.__tablero__))  # Movimiento no válido

    @patch("builtins.print")
    def test_check_movimiento_rey(self, mock_print):
                    # Limpia el tablero
        self.__tablero__.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]

        rey = Rey("blanco", 4, 4)
        self.__tablero__.set_pieza(4, 4, rey)
        # Movimiento válido
        self.assertTrue(rey.checkMovimiento(5, 4, self.__tablero__))  # Movimiento vertical
        self.assertTrue(rey.checkMovimiento(4, 5, self.__tablero__))  # Movimiento horizontal
        self.assertTrue(rey.checkMovimiento(5, 5, self.__tablero__))  # Movimiento diagonal
        # Movimiento inválido
        self.assertFalse(rey.checkMovimiento(6, 6, self.__tablero__))  # Movimiento mayor a 1 casilla

    @patch("builtins.print")
    def test_check_movimiento_peon(self, mock_print):
            # Limpia el tablero
        self.__tablero__.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]
        
        peon_blanco = Peon("blanco", 6, 0)
        self.__tablero__.set_pieza(6, 0, peon_blanco)
        peon_negro = Peon("negro", 1, 0)
        self.__tablero__.set_pieza(1, 0, peon_negro)
        peon_negro2 = Peon("negro", 5, 1)
        self.__tablero__.set_pieza(5, 1, peon_negro2)
        # Movimiento válido
        self.assertTrue(peon_blanco.checkMovimiento(5, 0, self.__tablero__))  # Movimiento 1 casilla adelante
        self.assertTrue(peon_blanco.checkMovimiento(4, 0, self.__tablero__))  # Movimiento 2 casillas adelante
        self.assertTrue(peon_blanco.checkMovimiento(5, 1, self.__tablero__))  # Movimiento en diagonal
        # Movimiento inválido
        with self.assertRaises(ValueError):
            peon_blanco.checkMovimiento(4, 1, self.__tablero__)  # Movimiento no válido
            peon_negro.checkMovimiento(4, 6, self.__tablero__)  # Movimiento no válido

if __name__ == "__main__":
    unittest.main()
