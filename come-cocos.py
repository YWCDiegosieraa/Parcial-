import pygame  # Importa la biblioteca pygame para manejar gráficos y eventos del juego
import random  # Se usa para generar valores aleatorios, aunque en este fragmento no se usa
import sys  # Se usa para manejar la salida del programa
import tkinter as tk  # Se usa para la ventana emergente de mensajes
from tkinter import messagebox  # Importa la función para mostrar mensajes emergentes

# Inicializar pygame
pygame.init()  # Inicia todas las funciones de pygame

# Definir constantes
MAPA_ANCHO = 20  # Número de celdas en el eje X del mapa
MAPA_ALTO = 9  # Número de celdas en el eje Y del mapa
ANCHO, ALTO = 1200, 800  # Tamaño de la pantalla en píxeles

# Calcular el tamaño de cada celda en función del tamaño de la ventana y el número de celdas
TAMANO_CELDA = min(ANCHO // MAPA_ANCHO, ALTO // MAPA_ALTO)

# Crear la ventana del juego con el tamaño adecuado
pantalla = pygame.display.set_mode((MAPA_ANCHO * TAMANO_CELDA, MAPA_ALTO * TAMANO_CELDA))
pygame.display.set_caption("Comecocos")  # Establece el título de la ventana

# Definir colores en formato RGB
NEGRO = (0, 0, 0)  # Color negro
AZUL = (0, 0, 255)  # Color azul
AMARILLO = (255, 255, 0)  # Color amarillo
BLANCO = (255, 255, 255)  # Color blanco
ROJO = (255, 0, 0)  # Color rojo

# Definir variables del juego
pac_x, pac_y = 1, 1  # Posición inicial del Pac-Man (fila, columna)
fan_x, fan_y = 10, 5 # Posición inicial del fantasma (fila, columna)
puntos = 0  # Contador de puntos obtenidos por el jugador
velocidad = 150  # Velocidad de actualización del juego (en milisegundos)

def reiniciar_juego():
    """Restablece el estado del juego a sus valores iniciales."""
    global pac_x, pac_y, puntos, fan_x, fan_y, mapa  # Declarar las variables globales para modificarlas

    # Restablecer la posición de Pac-Man y el fantasma
    pac_x, pac_y = 1, 1  
    fan_x, fan_y = 10, 5  
    puntos = 0  # Reiniciar el contador de puntos

    # Restaurar el mapa con su configuración inicial (1: pared, 2: punto, 3: camino)
    mapa = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 3, 3, 3, 3, 2, 3, 1, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 1],
        [1, 3, 1, 1, 3, 1, 3, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 3, 1],
        [1, 3, 3, 1, 3, 3, 3, 1, 3, 3, 3, 1, 3, 3, 2, 1, 3, 1, 3, 1],
        [1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 3, 1, 3, 1],
        [1, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
        [1, 3, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 3, 1],
        [1, 3, 3, 3, 3, 2, 3, 1, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    # Restaurar los puntos en las posiciones donde deben estar (2 representa puntos blancos)
    for y in range(MAPA_ALTO):  # Recorre las filas del mapa
        for x in range(MAPA_ANCHO):  # Recorre las columnas del mapa
            if mapa[y][x] == 3:  # Si encuentra un camino (3)
                mapa[y][x] = 2  # Lo convierte en un punto (2)

    # Mapa del juego, representado como una lista bidimensional
# 1 = muro, 2 = puntos que Pacman puede comer, 3 = camino sin puntos
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 3, 3, 3, 2, 3, 1, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 1],
    [1, 3, 1, 1, 3, 1, 3, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 3, 1],
    [1, 3, 3, 1, 3, 3, 3, 1, 3, 3, 3, 1, 3, 3, 2, 1, 3, 1, 3, 1],
    [1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 3, 1, 3, 1],
    [1, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 3, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 3, 1],
    [1, 3, 3, 3, 3, 2, 3, 1, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Reemplazar los puntos (2) por caminos (3) en el mapa
for y in range(MAPA_ALTO):
    for x in range(MAPA_ANCHO):
        if mapa[y][x] == 3:
            mapa[y][x] = 2

# Función para mover al personaje Pacman
def mover_pacman(dx, dy): #dx y dy representan la posicion actual de pacman en el eje x y y 
    global pac_x, pac_y, puntos  # Usamos las variables globales pac_x, pac_y y puntos
    nuevo_x = pac_x + dx  # Calcular la nueva posición horizontal de Pacman
    nuevo_y = pac_y + dy  # Calcular la nueva posición vertical de Pacman

    # Verificar si el nuevo movimiento es válido (dentro de los límites y no sobre un muro)
    if 0 <= nuevo_x < MAPA_ANCHO and 0 <= nuevo_y < MAPA_ALTO and mapa[nuevo_y][nuevo_x] != 1:
        pac_x, pac_y = nuevo_x, nuevo_y  # Actualizar la posición de Pacman

        # Si el nuevo lugar tiene un punto (2), sumamos 5 puntos y lo eliminamos
        if mapa[pac_y][pac_x] == 2:
            puntos += 5
            mapa[pac_y][pac_x] = 0  # Eliminar el punto comido, cuando se toman los puntos se quitan 

# Función para mover al fantasma
def mover_fantasma(): # representan la posicion actual del fantasma en el eje x y y 
    global fan_x, fan_y
    distancia_x = pac_x - fan_x  # Calcular la distancia horizontal entre el fantasma y Pacman
    distancia_y = pac_y - fan_y  # Calcular la distancia vertical entre el fantasma y Pacman

    # Si el fantasma está cerca de Pacman (distancia menor o igual a 5), lo sigue
    if abs(distancia_x) + abs(distancia_y) <= 5: #abs signifaca valor absoluto ejemplo print(abs(_10)) resultado es 10 
        if abs(distancia_x) > abs(distancia_y):  # Si la distancia horizontal es mayor
            if distancia_x > 0 and mapa[fan_y][fan_x + 1] != 1:  # Si el fantasma puede moverse a la derecha
                fan_x += 1 # Si el valor en esa celda NO es 1, significa que no hay una pared y el fantasma puede moverse.
            elif distancia_x < 0 and mapa[fan_y][fan_x - 1] != 1:  # Si el fantasma puede moverse a la izquierda
                fan_x -= 1
        else:  # Si la distancia vertical es mayor
            if distancia_y > 0 and mapa[fan_y + 1][fan_x] != 1:  # Si el fantasma puede moverse hacia abajo
                fan_y += 1
            elif distancia_y < 0 and mapa[fan_y - 1][fan_x] != 1:  # Si el fantasma puede moverse hacia arriba
                fan_y -= 1
    else:  # Si el fantasma está lejos, se mueve aleatoriamente
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Posibles movimientos
        random.shuffle(movimientos)  # Mezclar los movimientos aleatoriamente
        for dx, dy in movimientos:  # Intentar un movimiento aleatorio
            nuevo_x = fan_x + dx # Calcular la nueva posición en el eje X.  
            nuevo_y = fan_y + dy # Calcular la nueva posición en el eje Y.

             # Verificar si la nueva posición está dentro de los límites del mapa y no es una pared (representada por 1).
            if 0 <= nuevo_x < MAPA_ANCHO and 0 <= nuevo_y < MAPA_ALTO and mapa[nuevo_y][nuevo_x] != 1: 
                fan_x, fan_y = nuevo_x, nuevo_y  # Actualizar la posición del fantasma Si es válido, actualizar la posición del fantasma.
                break # Salir del bucle después de mover al fantasma exitosamente.

# Función para mostrar el mensaje de "Game Over"
def mostrar_game_over(mensaje):
    pantalla.fill(NEGRO)  # Rellenar la pantalla de negro
    font = pygame.font.Font(None, 74)  # Crear una fuente con tamaño 74
    texto = font.render(mensaje, True, ROJO)  # Crear el texto con el mensaje
    pantalla.blit(texto, (ANCHO // 2 - 100, ALTO // 2 - 50))  # Dibujar el texto en el centro
    pygame.display.flip()  # Actualizar la pantalla y mostrar cambios hechos 
    pygame.time.delay(2000)  # Esperar 2 segundos
    preguntar_volver_a_jugar("¿Quieres jugar de nuevo?")  # Preguntar si quiere reiniciar el juego

# Función que pregunta al usuario si quiere volver a jugar
def preguntar_volver_a_jugar(mensaje):
    root = tk.Tk()  # Crear una ventana de tkinter, interfaz grafica
    root.withdraw()  # Ocultar la ventana principal
    respuesta = messagebox.askyesno("Fin del juego", mensaje)  # Mostrar un cuadro de diálogo con sí/no
    if respuesta:
        reiniciar_juego()  # Si el jugador quiere volver a jugar, reiniciar el juego
    else:
        pygame.quit()  # Si no quiere jugar, cerrar el juego
        sys.exit()  # Salir del programa

# Función para dibujar el puntaje actual en la pantalla
def dibujar_puntaje():
    font = pygame.font.Font(None, 36)  # Crear una fuente con tamaño 36
    texto = font.render(f"Puntos: {puntos}", True, BLANCO)  # Crear el texto con el puntaje
    pantalla.blit(texto, (10, 10))  # Dibujar el texto en la parte superior izquierda

# Función para comprobar si el jugador ha ganado
def comprobar_ganador():
    if all(celda != 2 for fila in mapa for celda in fila):  # Si no hay más puntos en el mapa
        pantalla.fill(NEGRO)  # Rellenar la pantalla de negro
        font = pygame.font.Font(None, 74)  # Crear una fuente con tamaño 74
        texto = font.render("WINNER!", True, AMARILLO)  # Crear el texto de ganador
        texto_rect = texto.get_rect(center=(MAPA_ANCHO * TAMANO_CELDA // 2, MAPA_ALTO * TAMANO_CELDA // 2))  # Centrar el texto
        pantalla.blit(texto, texto_rect)  # Dibujar el texto en el centro
        pygame.display.flip()  # Actualizar la pantalla
        pygame.time.delay(2000)  # Esperar 2 segundos
        preguntar_volver_a_jugar("¡Ganaste! ¿Quieres jugar de nuevo?")  # Preguntar si quiere jugar de nuevo

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():  # Revisar eventos del juego
        if evento.type == pygame.QUIT:
            ejecutando = False  # Si el jugador cierra la ventana, detener el juego

    teclas = pygame.key.get_pressed()  # Obtener las teclas presionadas
    # Mover a Pacman según las teclas presionadas
    if teclas[pygame.K_LEFT]:
        mover_pacman(-1, 0)
    if teclas[pygame.K_RIGHT]:
        mover_pacman(1, 0)
    if teclas[pygame.K_UP]:
        mover_pacman(0, -1)
    if teclas[pygame.K_DOWN]:
        mover_pacman(0, 1)
    
    mover_fantasma()  # Mover al fantasma

    # Verificar si Pacman colisiona con el fantasma
    if (pac_x, pac_y) == (fan_x, fan_y):
        mostrar_game_over("GAME OVER")  # Mostrar mensaje de fin del juego

    # Comprobar si el jugador ha ganado
    if comprobar_ganador():
        mostrar_game_over("¡YOU WIN!")  # Mostrar mensaje de victoria

    # Dibujar el mapa
    pantalla.fill(NEGRO)  # Rellenar la pantalla de negro
    for y in range(MAPA_ALTO):
        for x in range(MAPA_ANCHO):
            if mapa[y][x] == 1:  # Si es un muro
                pygame.draw.rect(pantalla, AZUL, (x * TAMANO_CELDA, y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
            elif mapa[y][x] == 2:  # Si es un punto
                pygame.draw.circle(pantalla, BLANCO, (x * TAMANO_CELDA + TAMANO_CELDA // 2, y * TAMANO_CELDA + TAMANO_CELDA // 2), TAMANO_CELDA // 4)

    # Dibujar Pacman y el fantasma
    pygame.draw.circle(pantalla, AMARILLO, (pac_x * TAMANO_CELDA + TAMANO_CELDA // 2, pac_y * TAMANO_CELDA + TAMANO_CELDA // 2), TAMANO_CELDA // 2)
    pygame.draw.circle(pantalla, ROJO, (fan_x * TAMANO_CELDA + TAMANO_CELDA // 2, fan_y * TAMANO_CELDA + TAMANO_CELDA // 2), TAMANO_CELDA // 2)

    dibujar_puntaje()  # Dibujar el puntaje

    pygame.display.flip()  # Actualizar la pantalla
    pygame.time.delay(velocidad)  # Controlar la velocidad del juego




