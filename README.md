# Proyecto Ajedrez 2024

Esta es una implementación básica simplificada del juego de ajedrez en Python.

## Cómo Instalar el Juego

La manera de correr el código es utilizando docker, para lo cual se deben correr los siguientes comandos:

Para instalar docker:
```
$ sudo apt install docker
```

Para crear la imagen de docker con el juego:
```
$ sudo docker buildx build --no-cache -t ajedrez_vpf .
```

Para poder ejecutar los tests y posteriormente iniciar el juego:
```
$ sudo docker run -i ajedrez_vpf
```

## Cómo Jugar

El modo de juego es de dos jugadores humanos que se enfrentan, que mueven piezas blancas y negras, respectivamente.

La interfaz de juego ofrece la opción de seleccionar una pieza (propia del turno actual, para lo cual deberás usar notación algebraica de casillas, como A2, B7, H4, etc.). También se ofrece la posibilidad de terminar la partida en empate.

Al seleccionar una pieza, se solicita la posición de destino (escrita en la misma notación).

Tras esto, se efectúa o cancela el movimiento, dependiendo de su validez, y se verifica si un jugador ganó.

## Cómo Ganar

La única manera de ganar es capturando el rey de tu oponente, de manera directa (como capturando a cualquier otra pieza, no existen reglas de jaque ni jaque mate).

Tras una victoria, el juego regresa al menú principal, desde donde puede cerrarse o iniciar un nuevo partido.

## 
Trabajo por Valentino Perassi Ferrara (Legajo: 63252)


# Integraciones 

## CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-v-perassiferrara/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-v-perassiferrara/tree/main)

## Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/f6f57fc28e040a5fc2d9/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-v-perassiferrara/maintainability)

## Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/f6f57fc28e040a5fc2d9/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-v-perassiferrara/test_coverage)