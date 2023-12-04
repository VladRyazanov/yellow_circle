import pygame
import random

if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                surface = pygame.Surface((500, 500))
                pygame.draw.circle(surface, (255, 255, 0), (250, 250), random.randint(1, 250))
                screen.blit(surface, (0, 0))

        pygame.display.flip()

    pygame.quit()