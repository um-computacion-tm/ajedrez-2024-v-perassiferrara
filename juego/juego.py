from juego.tablero import Tablero
from juego.excepciones import *
from juego.pieza import *
from juego.casilla import *
from juego.peon import *
from juego.torre import *
from juego.caballo import *
from juego.alfil import *
from juego.dama import *
from juego.rey import *



class JuegoAjedrez:
    def __init__(self):
        # Inicializa el tablero, el turno actual y el número de turno
        self.__tablero__ = Tablero()
        self.__turno__ = "blanco"
        self.__num_turno__ = 1

    # Los métodos @property (propiedades) permiten acceder a los atributos de la clase pieza desde el exterior 

    @property
    def tablero(self):
        return self.__tablero__

    @property
    def turno(self):
        return self.__turno__
    
    @property
    def num_turno(self):
        return self.__num_turno__


    def cambiar_turno(self): # Cambia el turno entre "blanco" y "negro" y avanza el contador de turnos
        self.__turno__ = "negro" if self.__turno__ == "blanco" else "blanco"
        self.__num_turno__ += 1

    def iniciar_juego(self): # Inicia o reinicia el juego, creando un nuevo tablero y reiniciando los turnos
        self.__tablero__ = Tablero()
        self.__turno__ = "blanco"
        self.__num_turno__ = 1

    def finalizar_juego(self): # Finaliza el juego, eliminando el tablero y los valores de losturnos
        self.__tablero__ = None
        self.__turno__ = None
        self.__num_turno__ = None

    def get_pieza(self, x, y): # Devuelve la pieza en la posición (x,y) del tablero
        return self.__tablero__.get_pieza(x, y)

    def checkMismaCasilla(self, x_origen, y_origen, x_destino, y_destino):
        # Verificar si la casilla de origen y destino son diferentes (deben serlo para que el movimiento sea válido)
        if x_origen == x_destino and y_origen == y_destino:
            raise ValueError("No se puede mover a la misma casilla")
        

    def checkDestino(self, x_origen, y_origen, x_destino, y_destino):

        # Verificar si la casilla de destino está dentro del tablero
        if not (0 <= x_destino <= 7 and 0 <= y_destino <= 7):
            raise ValueError("Posición no válida. Use casillas del tablero (a-h y 1-8)")
        
        pieza = self.get_pieza(x_origen, y_origen)
        pieza_destino = self.get_pieza(x_destino, y_destino)


        # Verificar si la casilla de destino está ocupada por una pieza aliada

        # Si está ocupada por una pieza aliada, lanza un error
        if isinstance(pieza_destino, Pieza) and pieza_destino.color == pieza.color: 
            raise ValueError("No se puede mover porque la casilla destino está ocupada por una pieza aliada")
        
        # Si está ocupada por una pieza oponente, devuelve True
        elif isinstance(pieza_destino, Pieza) and pieza_destino.color != pieza.color:
            return True

        # Si está vacía, devuelve False
        else:
            return False

    def validar_origen(self, x_origen, y_origen):

        # Verificar si la casilla de origen está dentro del tablero
        if x_origen < 0 or x_origen > 7 or y_origen < 0 or y_origen > 7:
            raise ValueError("Posición fuera del tablero")

        pieza = self.__tablero__.get_pieza(x_origen, y_origen)

        # Verificar si la posición seleccionada está vacía
        if isinstance(pieza, Casilla):
            raise EmptyError("No hay ninguna pieza en la casilla")

        # Verifica si la pieza pertenece al jugador que tiene el turno actual
        if pieza.color != self.__turno__:
            raise ColorError("No puedes seleccionar piezas de tu oponente")

        return pieza


    def validar_destino(self, x_origen, y_origen, x_destino, y_destino):
        # Valida si el destino es accesible según las reglas de movimiento de la pieza en el juego
        try:
            
            self.checkMismaCasilla(x_origen, y_origen, x_destino, y_destino)
            self.checkDestino(x_origen, y_origen, x_destino, y_destino)

            pieza = self.get_pieza(x_origen, y_origen)
            pieza_destino = self.get_pieza(x_destino, y_destino)

            pieza.checkMovimiento(x_destino, y_destino)


            # Verifica si el movimiento es diagonal
            if pieza.puede_mover("diagonal"):
                if x_origen != x_destino and y_origen != y_destino:
                    self.check_camino_diagonal(x_origen, y_origen, x_destino, y_destino)
            
            # Verifica si el movimiento es perpendicular (horizontal o vertical)
            elif pieza.puede_mover("perpendicular"):
                if y_origen == y_destino or x_origen == x_destino:
                    self.check_camino_perpendicular(x_origen, y_origen, x_destino, y_destino)

            # Verifica si el movimiento es de un peón (debido a que tiene restricciones particulares durante el juego)
            elif pieza.puede_mover("peon"):
                if y_origen == y_destino:
                    self.check_camino_vertical_peon(x_origen, x_destino, y_origen)
                elif y_origen != y_destino:
                    self.check_camino_diagonal_peon(x_origen, y_origen, x_destino, y_destino)

            # Verifica si la pieza tiene movimiento especial y
            # no tiene restricciones particulares de camino o movimiento (caballo y rey)
            elif pieza.puede_mover("especial"):
                pass

            else:
                raise ValueError("La pieza no tiene movimientos permitidos.")

            return True  # Si no hubo excepciones, el movimiento es válido

        except ValueError as e:
            raise e    



    def check_camino_perpendicular(self, x_origen, y_origen, x_destino, y_destino):
        # Verifica si hay alguna pieza en el camino cuando se mueve en línea recta
        if y_origen == y_destino: # Movimiento vertical
            coordenada_origen = x_origen
            coordenada_destino = x_destino
            movimiento = "vertical"

        elif x_origen == x_destino: # Movimiento horizontal
            coordenada_origen = y_origen
            coordenada_destino = y_destino
            movimiento = "horizontal"

        paso = 1 if coordenada_destino > coordenada_origen else -1

        for coordenada_comparacion in range(coordenada_origen + paso, coordenada_destino, paso):
            if movimiento == "vertical":
                if isinstance(self.get_pieza(coordenada_comparacion,y_origen), Pieza):
                    raise ValueError("No se puede mover porque hay una pieza en el camino")
            elif movimiento == "horizontal":
                if isinstance(self.get_pieza(x_origen,coordenada_comparacion), Pieza):
                    raise ValueError("No se puede mover porque hay una pieza en el camino")   

    def check_camino_diagonal(self, x_origen, y_origen, x_destino, y_destino):
        # Verifica si hay alguna pieza en el camino cuando se mueve en diagonal
        paso_x = 1 if x_destino > x_origen else -1
        paso_y = 1 if y_destino > y_origen else -1
        x_comparacion, y_comparacion = x_origen + paso_x, y_origen + paso_y

        while x_comparacion != x_destino and y_comparacion != y_destino:
            if isinstance(self.get_pieza(x_comparacion,y_comparacion), Pieza):
                raise ValueError("No se puede mover porque hay una pieza en el camino")
            x_comparacion += paso_x
            y_comparacion += paso_y
        
        return True

    def check_camino_vertical_peon(self, x_origen, x_destino, y_origen):
        # Verifica el movimiento vertical de un peón, incluyendo su movimiento inicial
        paso = 1 if x_destino > x_origen else -1

        # Movimiento normal de una casilla hacia adelante
        if x_destino == x_origen + paso:
            if isinstance(self.get_pieza(x_destino, y_origen), Pieza):
                raise ValueError("No se puede mover porque hay una pieza en el destino")
            return True

        # Movimiento inicial de dos casillas: Comprueba el atributo primera_posicion. Si es True
        # indica que el peón aun no se mueve y puede hacer un movimiento de dos casillas)
        if x_destino == x_origen + 2 * paso and self.get_pieza(x_origen, y_origen).primera_posicion:
            for x_comparacion in range(x_origen + paso, x_destino + paso, paso):
                if isinstance(self.get_pieza(x_comparacion, y_origen), Pieza):
                    raise ValueError("No se puede mover porque hay una pieza en el camino")
            return True

        raise ValueError("Movimiento inválido para el peón.")

    def check_camino_diagonal_peon(self, x_origen, y_origen, x_destino, y_destino):
        # Verifica si el peón puede capturar una pieza en diagonal
        pieza_origen = self.get_pieza(x_origen, y_origen)
        pieza_destino = self.get_pieza(x_destino, y_destino)

        # Verificar si la casilla de destino está ocupada por una pieza enemiga
        if isinstance(pieza_destino, Pieza) and pieza_destino.color != pieza_origen.color:
            return True  # Movimiento válido (captura)
        else:
            raise ValueError("Movimiento inválido para el peón: no puede moverse en diagonal sin capturar.")
        


    def mover_pieza(self, x_origen, y_origen, x_destino, y_destino):

        pieza = self.get_pieza(x_origen, y_origen)
        pieza_destino = self.get_pieza(x_destino, y_destino)

        # Actualizar coordenadas internas de la pieza
        pieza.mover(x_destino, y_destino)

        # Asignar pieza a su nueva posición en el tablero 
        self.__tablero__.set_pieza(x_destino, y_destino, pieza)

        # Asignar casilla vacía a la posición original de la pieza en el tablero
        self.__tablero__.set_pieza(x_origen, y_origen, Casilla(x_origen, y_origen))

        try:
            pieza.set_primera_posicion(False)
        except Exception:
            pass

        # Verifica el movimiento provoca una victoria
        if self.checkVictoria():
            return "Victoria"

        # Si no es victoria, indica que el movimiento fue correcto
        if isinstance(pieza_destino, Pieza):
            return "Captura"
        return True           



    def checkVictoria(self):
        # Verifica si el rey del oponente ha sido capturado. Si fue capturado, indica una victoria

        rey_oponente = "♔" if self.__turno__ == "blanco" else "♚"
        rey_oponente_vivo = True

# Busca el rey del oponente en el tablero
        for x_origen in range(8):
            for y_origen in range(8):
                pieza = self.get_pieza(x_origen, y_origen)
                
                if str(pieza) == rey_oponente:
                    rey_oponente_vivo = False
        if rey_oponente_vivo:
            return True
    
    
    def mostrar_tablero(self):
        # Devuelve la representación gráfica en forma de string del tablero actual
        return str(self.__tablero__)