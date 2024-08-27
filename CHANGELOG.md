# Changelog

Todos los cambios notables de este proyecto se documentarán en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.8.0] - 2024-08-27 (Segunda semana de desarrollo)

### Agregado

- Tests para flujos de la interfaz.
- Tests adicionales de juego y piezas.

### Modificado

- Método __str__ en piezas para que no tenga que definirse en cada subclase de pieza.
- Break al cerrar el juego, en favor de sys.exit.
- Dividido menú principal y de juego en: menú principal, menú de juego y menú de selección de piezas / movimiento.
- Reestructurado método de check de victorias.
- Reestructuración de métodos de check de destinos y caminos de movimientos hacia clase juego.
- Modo de check de primera posición en peones para cumplir de mejor manera con SOLID.
- Manejo de returns, errores e inputs entre interfaz y juego.
- Modificados str en piezas para poder definirlos en la clase de la que heredan (Pieza).

### Solucionado

- Problema de loops al ganar un partido.

### Eliminado

- Try y Except innecesarios.
- Tests redundantes de juego.
- Método turno_actual(), ya que era innecesario.
- 

## [0.7.0] - 2024-08-19

### Modificado

- Modificada condición de victoria y actualizados tests correspondientes.
- Mejorada cobertura de tests con casos para todos los subtipos de piezas.
- Corregida lógica de checkMovimiento en la clase Dama.
- Eliminados try y except innecesarios en checkMovimiento de piezas.

## [0.6.1] - 2024-08-18

### Modificado

- Renombrada carpeta clases a juego y ajustados imports.
- Eliminado método mover() obsoleto.
- Actualizado Dockerfile para reflejar cambios.

### Agregado

- Adaptados tests a la nueva estructura; divididos en 4 archivos: tablero, juego, interfaz y pieza.
- Ajustado coveragerc para ejecutar tests correctamente.
- Transferidas funcionalidades de Tablero a Juego.

## [0.6.0] - 2024-08-17

### Modificado

- Reestructurado método mover_pieza y simplificado la lógica.
- Eliminado método seleccionarPieza() y ajustados prints para representar movimientos y errores correctamente.
- Sustituido cuadricula() por get_pieza.

### Solucionado

- Simplificados prints para no indicar capturas, ya que el tablero muestra el estado actual.

## [0.5.1] - 2024-08-16

### Solucionado

- Corregido parcialmente problema de prints al mover piezas; ahora debería funcionar correctamente.

## [0.5.0] - 2024-08-15

### Modificado

- Movidos métodos de traducción a Interfaz y eliminado archivo main.
- Ajustados métodos para usar coordenadas internas en lugar de notación algebraica.
- Simplificados prints en Interfaz y corregido sistema de turnos.
- Actualizado Dockerfile y ajustada lógica de checkMovimiento del peón.

## [0.4.0] - 2024-08-14

### Modificado

- Eliminados prints de errores en piezas, reemplazados por raises.
- Sustituidos prints de acciones por returns.
- Creada subclase de excepción SelectionCancel para cancelar selección de pieza.

### Eliminado

- Prints vacíos en Interfaz para simplificar la función.

### Solucionado

- Resuelto problema de imports en tests al agregar ipdb.

## [0.3.0] - 2024-08-06

### Agregado

- Archivos Dockerfile y configuraciones.
- Avances en implementación de clases y tests.

### Modificado

- Corregido workdir en Dockerfile.

## [0.2.0] - 2024-08-05

### Agregado

- Uso de ipdb.
- Archivos __init__ para solucionar problemas de imports en tests. 
- Actualización de requirements y simplificación de prints.

## [0.1.0] - 2024-08-13

### Agregado

- Archivos base de cada tipo de pieza, casilla, excepciones, tablero, interfaz de usuario y juego. - 
- Archivo de test base con varios tests diversos (planeado para modificar y utilizar archivos separados en cada clase).
- Archivo Dockerfile para ejecutar el proyecto en una imagen de Docker.
- Carpetas de clases y tests para organizar el proyecto.

### Modificado

- Archivo main para ejecutar la interfaz de usuario e iniciar el juego.

### Eliminado

- Archivo test de ejemplo.

## [0.0.4] - 2024-08-08

### Agregado

- Integración con CodeClimate.
- Test de ejemplo para verificar integraciones.

### Modificado

- Archivo main para utilizar una función de prueba.

## [0.0.3] - 2024-08-08

### Agregado

- Integración con CircleCI.

## [0.0.2] - 2024-08-06

### Agregado

- Licencia GPLv3.

### Modificado

- Traducción al español.

## [0.0.1] - 2024-08-06

### Agregado

- Archivo Main.
- Archivo README con información básica.
- Archivo CHANGELOG para llevar un registro de cambios. 