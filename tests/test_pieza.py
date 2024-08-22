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

    # El checkMovimiento de la clase Pieza no hace nada por sí solo, ya que debe ser implementado en cada pieza
    def test_check_movimiento_pass(self): 
        a = Pieza("blanco", 0, 0)
        self.assertEqual(a.checkMovimiento(2,2), None)

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
        self.__juego__.tablero.set_pieza(0, 0, pieza)
        pieza_destino = Peon("negro", 2, 0)
        self.__juego__.tablero.set_pieza(2, 0, pieza_destino)
        self.assertTrue(self.__juego__.checkDestino(0,0,2,0))

    def test_check_destino_vacio(self):
        pieza = Torre("blanco", 0, 0)
        self.__juego__.tablero.set_pieza(0, 0, pieza)
        pieza_destino = Casilla(2, 0)
        self.__juego__.tablero.set_pieza(2, 0, pieza_destino)
        self.assertFalse(self.__juego__.checkDestino(0,0,2,0))

    def test_peon_primer_movimiento(self):
        peon = self.__juego__.get_pieza(6, 0)
        self.assertTrue(self.__juego__.mover_pieza(6, 0, 4, 0))
        self.assertEqual((peon.x,peon.y), (4, 0))



class TestCasilla(unittest.TestCase):

    def setUp(self):
        self.__juego__ = JuegoAjedrez()
        
    def test_get_coords(self):
        casilla1 = self.__juego__.get_pieza(4,4)
        casilla2 = self.__juego__.get_pieza(6,7)
        casilla3 = self.__juego__.get_pieza(3,1)

        self.assertEqual((casilla1.x, casilla1.y), (4, 4))
        self.assertEqual((casilla2.x, casilla2.y), (6, 7))
        self.assertEqual((casilla3.x, casilla3.y), (3, 1))



class TestAlfil(unittest.TestCase):

    def setUp(self):
        self.__juego__ = JuegoAjedrez()
        self.__juego__.tablero.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]
        self.__alfil__ = Alfil("blanco", 4, 4)
        self.__juego__.tablero.set_pieza(4, 4, self.__alfil__)

    def test_alfil_movimiento_diagonal_valido(self):
        self.assertTrue(self.__juego__.validar_destino(4, 4, 6, 6))
        self.assertTrue(self.__juego__.validar_destino(4, 4, 2, 2))
        self.assertTrue(self.__juego__.validar_destino(4, 4, 5, 3))
        self.assertTrue(self.__juego__.validar_destino(4, 4, 3, 5))

    def test_alfil_movimiento_no_diagonal(self):
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 4, 6)  # Movimiento horizontal

        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 6, 4)  # Movimiento vertical

    def test_alfil_movimiento_bloqueado(self):
        pieza_bloqueo = Peon("blanco", 5, 5)
        self.__juego__.tablero.set_pieza(5, 5, pieza_bloqueo)
        
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 6, 6)
    
    def test_alfil_movimiento_bloqueado2(self):
        pieza_bloqueo = Peon("blanco", 6, 6)
        self.__juego__.tablero.set_pieza(6, 6, pieza_bloqueo)
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 6, 6)

    def test_alfil_movimiento_bloqueado_por_varias_piezas(self):
        pieza_bloqueo1 = Peon("blanco", 5, 5)
        pieza_bloqueo2 = Peon("blanco", 6, 6)
        self.__juego__.tablero.set_pieza(5, 5, pieza_bloqueo1)
        self.__juego__.tablero.set_pieza(6, 6, pieza_bloqueo2)
        
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 7, 7)

    def test_alfil_movimiento_misma_posicion(self):
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 4, 4)



class TestPeon(unittest.TestCase):

    def setUp(self):
        self.__juego__ = JuegoAjedrez()
        self.__juego__.tablero.__cuadricula__ = [[Casilla(fila, columna) for columna in range(8)] for fila in range(8)]
        self.__peon__ = Peon("negro", 1, 4)
        self.__juego__.tablero.set_pieza(1, 4, self.__peon__)

    def test_peon_movimiento_avance_uno_valido(self):
        #Verifica que el peón puede moverse una casilla hacia adelante si está vacío el destino.
        self.assertTrue(self.__juego__.validar_destino(1, 4, 2, 4))

    def test_peon_movimiento_avance_uno_no_valido(self):
        #Verifica que el peón no puede moverse una casilla hacia adelante si está ocupada por otra pieza.
        self.__juego__.tablero.set_pieza(2, 4, Peon("blanco", 2, 4))
        self.assertRaises(ValueError, lambda: self.__juego__.validar_destino(1, 4, 2, 4))
        # Aca tuve que utilizar lambda para poder capturar el error que se lanza

    def test_peon_movimiento_avance_dos_valido(self):
        #Verifica que el peón puede moverse dos casillas hacia adelante desde su posición inicial.
        self.assertTrue(self.__juego__.validar_destino(1, 4, 3, 4))

    def test_peon_movimiento_avance_dos_no_valido(self):
        #Verifica que el peón no puede moverse dos casillas si no está en la posición inicial.
        self.assertTrue(self.__juego__.mover_pieza(1, 4, 2, 4))
        self.assertRaises(ValueError, lambda: self.__juego__.validar_destino(2, 4, 4, 4))
        # Aca tuve que utilizar lambda para poder capturar el error que se lanza

    def test_peon_movimiento_avance_dos_no_valido2(self):
        #Verifica que el peón no puede moverse dos casillas si hay una pieza en el camino.
        self.__juego__.tablero.set_pieza(2, 4, Peon("blanco", 2, 4))
        self.assertRaises(ValueError, lambda: self.__juego__.validar_destino(1, 4, 3, 4))
        # Aca tuve que utilizar lambda para poder capturar el error que se lanza

    def test_peon_movimiento_diagonal_captura_valida(self):
        #Verifica que el peón puede capturar una pieza en diagonal.
        pieza_adversario = Peon("blanco", 2, 3)
        self.__juego__.tablero.set_pieza(2, 3, pieza_adversario)
        self.assertTrue(self.__juego__.validar_destino(1, 4, 2, 3))

    def test_peon_movimiento_diagonal_no_captura(self):
        #Verifica que el peón no puede moverse en diagonal si no hay una pieza para capturar.
        self.assertRaises(ValueError, lambda: self.__juego__.validar_destino(1, 4, 2, 3))
        # Aca tuve que utilizar lambda para poder capturar el error que se lanza

    def test_peon_movimiento_no_valido(self):
        #Verifica que el peón no puede moverse en direcciones no permitidas.
        self.assertRaises(ValueError, lambda: self.__juego__.validar_destino(1, 4, 1, 5))  # Movimiento horizontal
        # Aca tuve que utilizar lambda para poder capturar el error que se lanza

    def test_peon_movimiento_misma_posicion(self):
        #Verifica que el peón no puede moverse a la misma posición en la que ya está.
        self.assertRaises(ValueError, lambda: self.__juego__.validar_destino(1, 4, 1, 4))
        # Aca tuve que utilizar lambda para poder capturar el error que se lanza



class TestTorre(unittest.TestCase):

    def setUp(self):
        self.__juego__ = JuegoAjedrez()
        self.__juego__.tablero.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]
        self.__torre__ = Torre("blanco", 4, 4)  # Coloca la torre en la fila 4, columna 4
        self.__juego__.tablero.set_pieza(4, 4, self.__torre__)

    def test_torre_movimiento_horizontal_valido(self):
        self.assertTrue(self.__juego__.validar_destino(4, 4, 4, 6)) # Movimiento horizontal a la derecha

        self.assertTrue(self.__juego__.validar_destino(4, 4, 4, 2)) # Movimiento horizontal a la izquierda

    def test_torre_movimiento_vertical_valido(self):
        self.assertTrue(self.__juego__.validar_destino(4, 4, 2, 4))  # Movimiento vertical hacia abajo

        self.assertTrue(self.__juego__.validar_destino(4, 4, 6, 4))  # Movimiento vertical hacia arriba

    def test_torre_movimiento_diagonal_no_valido(self):
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 6, 6)  # Movimiento diagonal

        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 2, 6)  # Movimiento diagonal

    def test_torre_movimiento_bloqueado(self):
        pieza_bloqueo = Peon("blanco", 4, 5)
        pieza_bloqueo2 = Peon("blanco", 5, 4)
        self.__juego__.tablero.set_pieza(4, 5, pieza_bloqueo)
        self.__juego__.tablero.set_pieza(5, 4, pieza_bloqueo2)
        
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 4, 6)  # Movimiento horizontal bloqueado
        
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 6, 4)  # Movimiento vertical bloqueado

    def test_torre_movimiento_bloqueado_por_varias_piezas(self):
        pieza_bloqueo1 = Peon("blanco", 4, 5)
        pieza_bloqueo2 = Peon("blanco", 4, 6)
        self.__juego__.tablero.set_pieza(4, 5, pieza_bloqueo1)
        self.__juego__.tablero.set_pieza(4, 6, pieza_bloqueo2)
        
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 4, 7)  # Movimiento horizontal bloqueado por múltiples piezas

  

class TestRey(unittest.TestCase):

    def setUp(self):
        self.__juego__ = JuegoAjedrez()
        self.__juego__.tablero.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]
        self.__rey__ = Rey("blanco", 4, 4)  # Coloca el rey en la fila 4, columna 4
        self.__juego__.tablero.set_pieza(4, 4, self.__rey__)

    def test_rey_movimiento_valido(self):
        self.assertTrue(self.__juego__.validar_destino(4, 4, 4, 5))  # Movimiento hacia abajo

        self.assertTrue(self.__juego__.validar_destino(4, 4, 4, 3))  # Movimiento hacia arriba

        self.assertTrue(self.__juego__.validar_destino(4, 4, 5, 4))  # Movimiento hacia la derecha

        self.assertTrue(self.__juego__.validar_destino(4, 4, 3, 4))  # Movimiento hacia la izquierda

        self.assertTrue(self.__juego__.validar_destino(4, 4, 5, 5))  # Movimiento en diagonal hacia abajo a la derecha

        self.assertTrue(self.__juego__.validar_destino(4, 4, 5, 3))  # Movimiento en diagonal hacia abajo a la izquierda

        self.assertTrue(self.__juego__.validar_destino(4, 4, 3, 5))  # Movimiento en diagonal hacia arriba a la derecha

        self.assertTrue(self.__juego__.validar_destino(4, 4, 3, 3))  # Movimiento en diagonal hacia arriba a la izquierda

    def test_rey_movimiento_invalido(self):
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 6, 6)  # Movimiento de dos casillas en diagonal

        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 4, 6)  # Movimiento de dos casillas en la misma fila

        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 6, 4)  # Movimiento de dos casillas en la misma columna



class TestCaballo(unittest.TestCase):

    def setUp(self):
        self.__juego__ = JuegoAjedrez()
        self.__juego__.tablero.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]
        self.__caballo__ = Caballo("blanco", 4, 4)  # Coloca el caballo en la fila 4, columna 4
        self.__juego__.tablero.set_pieza(4, 4, self.__caballo__)

    def test_caballo_movimiento_valido(self):
        self.assertTrue(self.__juego__.validar_destino(4, 4, 6, 5))  # Movimiento válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 6, 3))  # Movimiento válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 5, 6))  # Movimiento válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 5, 2))  # Movimiento válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 3, 6))  # Movimiento válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 3, 2))  # Movimiento válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 2, 5))  # Movimiento válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 2, 3))  # Movimiento válido

    def test_caballo_movimiento_invalido(self):
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 5, 5)  # Movimiento inválido (no en forma de 'L')

        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 4, 6)  # Movimiento inválido (no en forma de 'L')

        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 7, 7)  # Movimiento inválido (no en forma de 'L')

 

class TestDama(unittest.TestCase):

    def setUp(self):
        self.__juego__ = JuegoAjedrez()
        self.__juego__.tablero.__cuadricula__ = [[Casilla(x=fila, y=columna) for columna in range(8)] for fila in range(8)]
        self.__dama__ = Dama("blanco", 4, 4)  # Coloca la dama en la fila 4, columna 4
        self.__juego__.tablero.set_pieza(4, 4, self.__dama__)

    def test_dama_movimiento_diagonal_valido(self):
        self.assertTrue(self.__juego__.validar_destino(4, 4, 6, 6))  # Movimiento diagonal válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 2, 2))  # Movimiento diagonal válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 5, 3))  # Movimiento diagonal válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 3, 5))  # Movimiento diagonal válido

    def test_dama_movimiento_horizontal_y_vertical_valido(self):
        self.assertTrue(self.__juego__.validar_destino(4, 4, 4, 7))  # Movimiento horizontal válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 4, 0))  # Movimiento horizontal válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 7, 4))  # Movimiento vertical válido
        self.assertTrue(self.__juego__.validar_destino(4, 4, 0, 4))  # Movimiento vertical válido

    def test_dama_movimiento_invalido(self):
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 7, 5)  # Movimiento inválido (no en línea recta)

        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 6, 3)  # Movimiento inválido (no en línea recta)

    def test_dama_movimiento_bloqueado(self):
        pieza_bloqueo = Peon("blanco", 5, 5)
        self.__juego__.tablero.set_pieza(5, 5, pieza_bloqueo)
        
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 6, 6)  # Movimiento bloqueado por una pieza
    
    def test_dama_movimiento_bloqueado2(self):
        pieza_bloqueo = Peon("blanco", 6, 6)
        self.__juego__.tablero.set_pieza(6, 6, pieza_bloqueo)
        
        with self.assertRaises(ValueError):
            self.__juego__.validar_destino(4, 4, 6, 6) # Destino bloqueado por una pieza



if __name__ == "__main__":
    unittest.main()