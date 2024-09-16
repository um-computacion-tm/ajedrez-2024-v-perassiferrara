class OppositeColorError(Exception):
    def __init__(self):
        super().__init__("No puedes seleccionar piezas de tu oponente")

class EmptyError(Exception):
    def __init__(self):
        super().__init__("No hay ninguna pieza en la casilla")

class MenuOptionError(Exception):
    def __init__(self):
        super().__init__("Opción no valida")

class CoordinatesError(Exception):
    def __init__(self):
        super().__init__("Posición no válida. Use casillas del tablero (a-h y 1-8)")

class MovementError(Exception):
    pass

class ReyMovementError(MovementError):
    def __init__(self):
        super().__init__("Movimiento inválido para el Rey")

class DamaMovementError(MovementError):
    def __init__(self):
        super().__init__("Movimiento inválido para la dama")

class PeonMovementError(MovementError):
    def __init__(self):
        super().__init__("Movimiento inválido para el peón.")

class TorreMovementError(MovementError):
    def __init__(self):
        super().__init__("Movimiento inválido para la torre")

class CaballoMovementError(MovementError):
    def __init__(self):
        super().__init__("Movimiento inválido para el Caballo")

class AlfilMovementError(MovementError):
    def __init__(self):
        super().__init__("Movimiento inválido para el alfil")

class DestinationError(Exception):
    pass

class PathError(Exception):
    def __init__(self):
        super().__init__("No se puede mover porque hay una pieza en el camino")

class SamePositionError(Exception):
    def __init__(self):
        super().__init__("No se puede mover a la misma casilla")

class OutOfBoardError(Exception):
    def __init__(self):
        super().__init__("Posición fuera del tablero")