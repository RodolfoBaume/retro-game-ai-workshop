"""
settings.py
Configuraciones globales para el videojuego "Bit-AI Shooter".
Parte del taller de Ingeniería en Sistemas - Tec de Pachuca.
"""

import pygame

# 1. Configuración de Pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TITLE = "Bit-AI Shooter: Retro Workshop"

# 2. Colores (Formato RGB)
# Útiles para fondos temporales o hitboxes de depuración
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)

# 3. Propiedades del Jugador
PLAYER_SPEED = 7
PLAYER_LIVES = 3
BULLET_SPEED = -10  # Negativo porque el eje Y se invierte en Pygame (hacia arriba es negativo)

# 4. Propiedades de los Enemigos
ENEMY_SPEED_MIN = 2
ENEMY_SPEED_MAX = 5
ENEMY_SPAWN_RATE = 40  # Cantidad de frames entre cada aparición de un enemigo nuevo

# 5. Rutas de Assets
# Organizadas para mantener limpio el repositorio y evitar errores de ruta
IMG_DIR = "../assets/images"
SND_DIR = "../assets/sounds"
FNT_DIR = "../assets/fonts"
MUS_DIR = "../assets/music"

# 6. Configuración de Texto
SCORE_FONT_SIZE = 32
GAME_OVER_FONT_SIZE = 74

BG_SPEED_SLOW = 1  # Capa de fondo (muy lejos)
BG_SPEED_FAST = 3  # Capa frontal (más cerca de la nave)