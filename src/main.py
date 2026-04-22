import pygame
import sys
from settings import *
from sprites import Player, Enemy, Bullet

# 1. Inicialización de Pygame y creación de la ventana
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# 2. Función auxiliar para dibujar texto en pantalla (UI)
def draw_text(surf, text, size, x, y, color=WHITE):
    # En un proyecto real, aquí cargarían la fuente descargada: pygame.font.Font(ruta, size)
    font = pygame.font.SysFont("arial", size, bold=True)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# 3. Función para reiniciar las variables del juego
def reset_game():
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    return all_sprites, enemies, bullets, player, 0

# 4. Variables de Estado
game_state = "START"  # Posibles estados: "START", "PLAYING", "GAME_OVER"
all_sprites, enemies, bullets, player, score = reset_game()
frame_count = 0

# 5. El Game Loop (Bucle Principal)
running = True
while running:
    # A. EVENTOS (Input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_state == "START" or game_state == "GAME_OVER":
                # Cambiar de estado con cualquier tecla
                all_sprites, enemies, bullets, player, score = reset_game()
                game_state = "PLAYING"
            elif game_state == "PLAYING" and event.key == pygame.K_SPACE:
                # Disparar
                player.shoot(bullets)
                all_sprites.add(bullets)

    # B. LÓGICA (Update)
    if game_state == "PLAYING":
        all_sprites.update()
        frame_count += 1

        # Lógica de "Spawneo" (Aparición de enemigos)
        if frame_count % ENEMY_SPAWN_RATE == 0:
            e = Enemy()
            all_sprites.add(e)
            enemies.add(e)

        # Resolución de Colisiones: Balas vs Enemigos
        # El 'True, True' indica que ambos objetos se eliminan al chocar (Garbage Collection)
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 10
            # Aquí podrían agregar explosiones visuales o reproducir el SFX

        # Resolución de Colisiones: Enemigos vs Jugador
        # 'False' para que el jugador no se elimine inmediatamente de la memoria
        crashes = pygame.sprite.spritecollide(player, enemies, False)
        if crashes:
            game_state = "GAME_OVER"

    # C. DIBUJADO (Render)
    # Llenar el fondo de negro (o aquí dibujarían el Asset del fondo espacial)
    screen.fill(BLACK)

    if game_state == "START":
        draw_text(screen, TITLE, 50, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, CYAN)
        draw_text(screen, "Presiona cualquier tecla para empezar", 22, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    elif game_state == "PLAYING":
        all_sprites.draw(screen)
        draw_text(screen, f"Score: {score}", 30, SCREEN_WIDTH // 2, 10)
    
    elif game_state == "GAME_OVER":
        draw_text(screen, "GAME OVER", 74, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, RED)
        draw_text(screen, f"Puntaje Final: {score}", 30, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        draw_text(screen, "Presiona cualquier tecla para reiniciar", 22, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 / 4)

    # Actualizar la pantalla y controlar los FPS
    pygame.display.flip()
    clock.tick(FPS)

# Salir limpiamente
pygame.quit()
sys.exit()