import pygame

# Inicializar pygame
pygame.init()

# Configurar la ventana del juego
screen_width = 1100
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi juego en 2D")

class game:
    def __init__(self):
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)

    def update(self):
        # Lógica de actualización del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:  # Tecla A para moverse a la izquierda
            self.rect.x -= 1
        if keys[pygame.K_d] and self.rect.right < screen_width:  # Tecla D para moverse a la derecha
            self.rect.x += 1
        if keys[pygame.K_w] and self.rect.top > 0:  # Tecla W para moverse hacia arriba
            self.rect.y -= 1
        if keys[pygame.K_s] and self.rect.bottom < screen_height:  # Tecla S para moverse hacia abajo
            self.rect.y += 1

    def draw(self):
        # Dibujar la nave del jugador en la pantalla
        screen.blit(self.image, self.rect)

# Crear instancia del jugador
Game = game()

# Bucle principal del juego
Scena = True
while Scena:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Scena = False

    # Actualizar estado del juego
    Game.update()

    # Renderizar la pantalla
    screen.fill((0, 0, 0))
    Game.draw()
    pygame.display.flip()

# Salir del juego
pygame.quit()
