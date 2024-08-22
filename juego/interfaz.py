from juego.juego import JuegoAjedrez
import sys
from juego.excepciones import *

class CLI:
    def __init__(self):
        # Inicializa el juego y las variables que mapean las filas y columnas del tablero en la interfaz
        self.__juego__ = JuegoAjedrez()
        self.__filas__ = ("8", "7", "6", "5", "4", "3", "2", "1")
        self.__columnas__ = ("A", "B", "C", "D", "E", "F", "G", "H")
        self.__posiciones__ = [columna+fila for columna in self.__columnas__ for fila in self.__filas__]

    def traducir_a_coordenadas(self, notacion_ajedrez):
        # Convierte notación algebraica (a2, h8, etc.) a coordenadas (x,y) de la matriz del tablero   

        notacion_ajedrez = notacion_ajedrez.upper() # Convierte a mayúsculas la entrada

        if notacion_ajedrez in self.__posiciones__:
            # Encuentra la columna y fila en el tablero y las devuelve como coordenadas (x, y)
            y = self.__columnas__.index(notacion_ajedrez[0].upper())
            x = self.__filas__.index(notacion_ajedrez[1])
            return x, y
        else:
            # Si la posición no es válida, lanza un error
            raise ValueError("Posición no válida. Use casillas del tablero (a-h y 1-8)")

    def traducir_a_posicion(self, fila, columna):
        # Convierte coordenadas (x, y) de la matriz del tablero a notación algebraica (a2, h8, etc.)
        return self.__columnas__[columna] + self.__filas__[fila]



    def mostrar_menu_principal(self):
        # Muestra el menú principal del juego
        while True:
            print(("\nJuego de Ajedrez [Por Valentino Perassi Ferrara]\n") + \
            ("------------------------------------------------\n") + \
            ("\nElige una opción:\n") + \
            ("\n1. Iniciar juego\n") + \
            ("2. Salir\n"))

            opcion = (input("--> ")).strip() # Obtiene la opción ingresada por el usuario, eliminando espacios en blanco
            try:
                if opcion not in ("1", "2"): # Lanza un error si la opción no es válida
                    raise SelectionError("Opcion no valida")

                elif opcion == "2": # Cierra el juego si se selecciona la opción 2
                    print("\n" + "Cerrando juego" + "\n")
                    sys.exit()

                elif opcion == "1": # Inicia un nuevo partido si se selecciona la opción 1
                    self.__juego__.iniciar_juego()
                    print("\n" + "Juego Iniciado" + "\n" + "\n" + \
                        "Tablero Inicial:\n\n" + self.__juego__.mostrar_tablero())
                        
                    self.mostrar_menu_juego()
            
            except SelectionError as e: # Captura y muestra el error si la opción no es válida
                print("\n" + str(e) + "\n")

    def mostrar_menu_juego(self):
        # Muestra el menú del juego
        while True:
            print((f"Turno {self.__juego__.num_turno}: {self.__juego__.turno}") + "\n" + \
            ("\n1. Seleccionar pieza (a7, b1, d3, etc.): ") + \
            ("\n2. Terminar juego en empate\n"))

            opcion = input("--> ").strip() # Obtiene la opción ingresada por el usuario, eliminando espacios en blanco

            if opcion == "2": # Si se selecciona terminar en empate, finaliza el juego y vuelve al menú principal
                self.__juego__.finalizar_juego()
                print("\nJuego terminado: Empate\n")
                break

            elif opcion == "1": # Si se elige la opción de seleccionar una pieza, muestra el menú de selección
                self.mostrar_menu_seleccion()
                
    def mostrar_menu_seleccion(self):
        # Muestra el menú de selección y movimiento de piezas
        while True:
            try:
                print("\nIndique posición a seleccionar: ")
                
                entrada = (input("--> ")).strip() # Obtiene la entrada ingresada por el usuario, eliminando espacios en blanco
                print()

                x_origen, y_origen = self.traducir_a_coordenadas(entrada) # Convierte la entrada a coordenadas (x,y)
                
                pieza = self.__juego__.validar_origen(x_origen, y_origen) # Valida la posición de origen seleccionada

                print(f"\n{pieza.nombre} {pieza.color} en {self.traducir_a_posicion(x_origen,y_origen)}\n") 
                # Indica la pieza seleccionada y su posición en el tablero
                
                entrada_destino = (input("--> ")).strip() # Obtiene la entrada ingresada por el usuario, eliminando espacios en blanco
                print()

                x_destino, y_destino = self.traducir_a_coordenadas(entrada_destino) # Convierte la entrada a coordenadas (x,y)

                self.__juego__.validar_destino(x_origen, y_origen, x_destino, y_destino) # Valida la posición de destino indicada
                
                pieza_destino = self.__juego__.get_pieza(x_destino, y_destino) # Obtiene la pieza en la posición de destino

                resultado_movimiento = self.__juego__.mover_pieza(x_origen, y_origen, x_destino, y_destino)
                # Realiza el movimiento de la pieza seleccionada, y almacena su resultado

                
                if resultado_movimiento == "Victoria": # Si el movimiento fue correcto, indica que el jugador ha ganado

                    print(f"¡El jugador {self.__juego__.turno} ha ganado!\n") 
                    print("Tablero final:\n")
                    print(self.__juego__.mostrar_tablero())
                    print("------------------------------------------------")

                    self.__juego__.finalizar_juego() # Finaliza el juego

                    self.mostrar_menu_principal() # Vuelve al menú principal
                    
                else:
                    if resultado_movimiento == True: # Si el movimiento fue correcto, su resultado es True
                        print(f"{pieza.nombre} {pieza.color} {self.traducir_a_posicion(x_origen,y_origen)} se mueve a {self.traducir_a_posicion(x_destino,y_destino)}\n")
                        # Indica el movimiento de la pieza seleccionada


                    elif resultado_movimiento == "Captura":
                        print(f"{pieza.nombre} {pieza.color} {self.traducir_a_posicion(x_origen,y_origen)} captura a {pieza_destino.nombre} {pieza_destino.color} en {self.traducir_a_posicion(x_destino,y_destino)}\n")
                        # Indica la captura de la pieza enemiga

                    print("\nTablero actual:\n")
                    print(self.__juego__.mostrar_tablero()) # Muestra el estado actual del tablero
                    
                    self.__juego__.cambiar_turno() # Cambia el turno
                    break # Retorna al menú de juego, para el siguiente turno

            except Exception as e: # Captura y muestra el error si ocurre algún problema
                print(f"{e}\n")
                break


def main(): # Función principal del programa
    interfaz = CLI() # Crea una instancia de la clase CLI (interfaz)
    interfaz.mostrar_menu_principal() # Muestra el menú principal

if __name__ == "__main__": 
    main() # Ejecuta la función principal del programa