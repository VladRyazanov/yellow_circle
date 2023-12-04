import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    has_a_circle = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                has_a_circle = True

        screen.fill((0, 0, 255))
        if has_a_circle:
            pygame.draw.circle(screen, (255, 255, 0), (250, 250), 100)
        pygame.display.flip()

    pygame.quit()