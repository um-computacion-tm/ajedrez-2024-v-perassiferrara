from juego import JuegoAjedrez

class CLI:
    def __init__(self):
        self.__juego__ = JuegoAjedrez()
        self.__filas__ = ("8", "7", "6", "5", "4", "3", "2", "1")
        self.__columnas__ = ("A", "B", "C", "D", "E", "F", "G", "H")
        self.__posiciones__ = [columna+fila for columna in self.__columnas__ for fila in self.__filas__]

    def traducir_a_coordenadas(self, notacion_ajedrez):
        notacion_ajedrez = notacion_ajedrez.upper()

        if notacion_ajedrez == "0":
            y = 10
            x = 10
            return x, y

        elif notacion_ajedrez in self.__posiciones__:
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
            print("\nJuego de Ajedrez [Por Valentino Perassi Ferrara]")
            print("------------------------------------------------\n")
            print("Elige una opción:\n")
            print("1. Iniciar juego")
            print("2. Salir\n")

            opcion = input("--> ")
            resultado = self.__juego__.seleccionar_opcion(opcion)

            if resultado == "Opción no válida":
                print("\n" + resultado + "\n")

            elif resultado == "Cerrando juego":
                print("\n" + resultado + "\n")
                break

            elif resultado == "Juego iniciado":
                print()
                print(self.__juego__.iniciar_juego())
                self.mostrar_menu_juego()

    def mostrar_menu_juego(self):
        while True:
            print(self.__juego__.turno_actual())
            print("\n1. Seleccionar pieza (a7, b1, d3, etc.): ")
            print("2. Terminar juego en empate\n")

            print("Seleccione una opción: ")
            opcion = input("--> ")

            if opcion == "2":
                print(self.__juego__.finalizar_juego())
                break

            elif opcion == "1":
                try:
                    print("\nIndique posición a seleccionar: ")
                    
                    entrada = input("--> ")
                
                    print()
                    
                    x, y = self.traducir_a_coordenadas(entrada)
                    
                    resultado = self.__juego__.seleccionar_pieza(x, y)

                    pieza = resultado
                    print(f"\n{pieza.nombre} {pieza.color} en {self.traducir_a_posicion(x,y)}\n") 
                    print("Indique posición de destino (0 para cancelar selección):\n")
                    entrada_destino = input("--> ")
                    print()

                    x_destino, y_destino = self.traducir_a_coordenadas(entrada_destino)

                    resultado_movimiento = self.__juego__.mover_pieza(pieza, x_destino, y_destino)

                    if resultado_movimiento == "Victoria":

                        print(f"¡El jugador {self.turno} ha ganado!\n")
                        print("Tablero final:\n")
                        print(self)
                        print("------------------------------------------------")

                        self.__juego__.cambiar_turno()

                        break

                    else:

                        print(resultado_movimiento + "\n")

                        print("\nTablero actual:\n")
                        print(self.__juego__.mostrar_tablero())
                        
                        self.__juego__.cambiar_turno()

                except Exception as e:
                    print(e)
                    continue


def main():
    interfaz = CLI()
    interfaz.mostrar_menu_principal()

if __name__ == "__main__":
    main()