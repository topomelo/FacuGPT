import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_SPACE

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Player settings
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_COLOR = (255, 0, 0)

# Ground
GROUND_HEIGHT = SCREEN_HEIGHT - 50

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.bottom = GROUND_HEIGHT
        self.speed_x = 0
        self.vel_y = 0
        self.on_ground = True

    def update(self):
        self.rect.x += self.speed_x
        self.vel_y += 1  # gravity
        self.rect.y += self.vel_y
        if self.rect.bottom >= GROUND_HEIGHT:
            self.rect.bottom = GROUND_HEIGHT
            self.on_ground = True
            self.vel_y = 0
        else:
            self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.vel_y = -20
            self.on_ground = False


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Simple Mario Clone')
    clock = pygame.time.Clock()

    player = Player()
    all_sprites = pygame.sprite.Group(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player.speed_x = -5
                elif event.key == K_RIGHT:
                    player.speed_x = 5
                elif event.key == K_SPACE:
                    player.jump()
            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_RIGHT):
                    player.speed_x = 0

        all_sprites.update()

        screen.fill((135, 206, 235))  # sky blue
        pygame.draw.rect(screen, (0, 255, 0), (0, GROUND_HEIGHT, SCREEN_WIDTH, 50))  # ground
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
