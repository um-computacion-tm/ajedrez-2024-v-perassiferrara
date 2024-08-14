from clases.juego import JuegoAjedrez

class CLI:
    def __init__(self):
        self.juego = JuegoAjedrez()

    def mostrar_menu_principal(self):
        while True:
            print()
            print("Juego de Ajedrez [Por Valentino Perassi Ferrara]")
            print("------------------------------------------------")
            print()
            print("Elige una opción:")
            print()
            print("1. Iniciar juego")
            print("2. Salir")
            print()

            opcion = input("--> ")
            resultado = self.juego.seleccionar_opcion(opcion)

            if resultado == "Opción no válida":
                print()
                print(resultado)
                print()
                continue

            elif resultado == "Juego terminado: Empate":
                print()
                print(resultado)
                print()
                break

            elif resultado == "Juego iniciado":
                print()
                print(self.juego.iniciar_juego())
                self.mostrar_menu_juego()

    def mostrar_menu_juego(self):
        while True:
            print(self.juego.turno_actual())
            print()
            print("1. Seleccionar pieza (a7, b1, d3, etc.): ")
            print("2. Terminar juego en empate")
            print()

            print("Seleccione una opción: ")
            opcion = input("--> ")

            if opcion == "2":
                print()
                print(self.juego.finalizar_juego())
                print()
                break

            elif opcion == "1":
                print()
                print("Indique posición a seleccionar: ")
                entrada = input("--> ")
                print()
                resultado = self.juego.seleccionar_pieza(entrada)

                if isinstance(resultado, tuple):
                    pieza, posicion = resultado
                    print()
                    print(f"{pieza.nombre} {pieza.color} en {posicion}\n") 
                    print()
                    print("Indique posición de destino (0 para cancelar selección): ")
                    print()
                    entrada_destino = input("--> ")
                    print()

                    resultado_movimiento = self.juego.mover_pieza(pieza, entrada_destino)

                    if resultado_movimiento == "Victoria":

                        print(f"¡El jugador {self.turno} ha ganado!")
                        print("------------------------------------------------")
                        print("Tablero final:\n")
                        print(self)
                        print("------------------------------------------------")

                        self.tablero.cambiarTurno()

                        break

                    elif resultado_movimiento == "Movimiento exitoso":

                        print()
                        print("Tablero actual:\n")
                        print(self.juego.mostrar_tablero())
                        
                        continue

                    else:
                        print(resultado_movimiento)
                        print()
                else:
                    print(resultado)
                    print()