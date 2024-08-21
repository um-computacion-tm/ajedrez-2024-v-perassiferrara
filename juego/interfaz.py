from juego.juego import JuegoAjedrez
import sys
from juego.excepciones import *

class CLI:
    def __init__(self):
        self.__juego__ = JuegoAjedrez()
        self.__filas__ = ("8", "7", "6", "5", "4", "3", "2", "1")
        self.__columnas__ = ("A", "B", "C", "D", "E", "F", "G", "H")
        self.__posiciones__ = [columna+fila for columna in self.__columnas__ for fila in self.__filas__]

    def traducir_a_coordenadas(self, notacion_ajedrez):
        notacion_ajedrez = notacion_ajedrez.upper()

        if notacion_ajedrez in self.__posiciones__:
            # Si la posicion dada existe en el tablero, devuelve las coordenadas
            y = self.__columnas__.index(notacion_ajedrez[0].upper())
            x = self.__filas__.index(notacion_ajedrez[1])
            return x, y
        else:
            raise ValueError("Posición no válida. Use casillas del tablero (a-h y 1-8)")

    def traducir_a_posicion(self, fila, columna):
        return self.__columnas__[columna] + self.__filas__[fila]



    def mostrar_menu_principal(self):
        while True:
            print(("\nJuego de Ajedrez [Por Valentino Perassi Ferrara]\n") + \
            ("------------------------------------------------\n") + \
            ("\nElige una opción:\n") + \
            ("\n1. Iniciar juego\n") + \
            ("2. Salir\n"))

            opcion = input("--> ")
            try:
                resultado = self.__juego__.seleccionar_opcion(opcion)

                if resultado == "Cerrando juego":
                    print("\n" + resultado + "\n")
                    sys.exit()

                elif resultado == "Juego iniciado":
                    print(("\n") + (self.__juego__.iniciar_juego()))
                    self.mostrar_menu_juego()
            
            except SelectionError as e:
                print("\n" + str(e) + "\n")

    def mostrar_menu_juego(self):
        while True:
            print((self.__juego__.turno_actual()) + "\n" + \
            ("\n1. Seleccionar pieza (a7, b1, d3, etc.): ") + \
            ("\n2. Terminar juego en empate\n"))

            opcion = input("--> ")

            if opcion == "2":
                self.__juego__.finalizar_juego
                print("\nJuego terminado: Empate\n")
                break

            elif opcion == "1":
                self.mostrar_menu_seleccion()
                
    def mostrar_menu_seleccion(self):
        while True:
            try:
                print("\nIndique posición a seleccionar: ")
                
                entrada = input("--> ")
                print()

                x_origen, y_origen = self.traducir_a_coordenadas(entrada)
                
                pieza = self.__juego__.validar_origen(x_origen, y_origen)

                print(f"\n{pieza.nombre} {pieza.color} en {self.traducir_a_posicion(x_origen,y_origen)}\n") 
                


                entrada_destino = input("--> ")
                print()

                x_destino, y_destino = self.traducir_a_coordenadas(entrada_destino)

                pieza_destino = self.__juego__.validar_destino(x_origen, y_origen, x_destino, y_destino)
                
                resultado_movimiento = self.__juego__.mover_pieza(x_origen, y_origen, x_destino, y_destino)

                
                if resultado_movimiento == "Victoria":

                    print(f"¡El jugador {self.__juego__.turno} ha ganado!\n")
                    print("Tablero final:\n")
                    print(self.__juego__.mostrar_tablero())
                    print("------------------------------------------------")

                    self.__juego__.finalizar_juego()

                    self.mostrar_menu_principal()
                    
                else:
                    if resultado_movimiento == True: # Si el movimiento fue correcto, resultado_movimiento es True
                        print(f"{pieza.nombre} {pieza.color} {self.traducir_a_posicion(x_origen,y_origen)} se mueve a {self.traducir_a_posicion(x_destino,y_destino)}\n")

                    print("\nTablero actual:\n")
                    print(self.__juego__.mostrar_tablero())
                    
                    self.__juego__.cambiar_turno()
                    break

            except Exception as e:
                print(f"{e}\n")
                break


def main():
    interfaz = CLI()
    interfaz.mostrar_menu_principal()

if __name__ == "__main__":
    main()