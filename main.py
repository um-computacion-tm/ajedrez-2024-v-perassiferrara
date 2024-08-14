from clases.excepciones import *
from clases.tablero import Tablero
from clases.juego import JuegoAjedrez
from clases.interfaz import CLI

def main():
    interfaz = CLI()
    interfaz.mostrar_menu_principal()

if __name__ == "__main__":
    main()