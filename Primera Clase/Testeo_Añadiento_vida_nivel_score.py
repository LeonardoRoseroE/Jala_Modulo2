import pygame

# Inicializar pygame
pygame.init()

# Configurar la ventana del juego
screen_width = 1100
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi juego en 2D")

class Game:
    def __init__(self):
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.score = 0
        self.level = 1
        self.lives = 3
        self.life_image = pygame.image.load("vida.png")
        self.life_image = pygame.transform.scale(self.life_image, (25, 25))

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

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render("Puntuación: " + str(self.score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def draw_level(self):
        font = pygame.font.Font(None, 36)
        level_text = font.render("Nivel: " + str(self.level), True, (255, 255, 255))
        screen.blit(level_text, (10, 50))

    def draw_lives(self):
        x = 10
        y = 90
        for _ in range(self.lives):
            screen.blit(self.life_image, (x, y))
            x += 50

# Crear instancia del jugador y del juego
player = Game()

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar estado del juego
    player.update()

    # Renderizar la pantalla
    screen.fill((0, 0, 0))
    player.draw()

    # Dibujar el marcador y los indicadores
    player.draw_score()
    player.draw_level()
    player.draw_lives()

    pygame.display.flip()

# Salir del juego
pygame.quit()
