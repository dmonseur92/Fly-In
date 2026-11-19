import pygame
from parsing import get_text_file
from renderer import Renderer
from menu import Menu

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
pygame.display.set_caption("FLY_IN 🐈")

clock = pygame.time.Clock()
renderer = Renderer(screen)
menu = Menu(screen)

playing = False
map_data = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if playing and event.type == pygame.MOUSEBUTTONDOWN:
            if renderer.back_button.collidepoint(event.pos):
                playing = False
                menu.show_difficulties()
        
        if not playing:
            selected_map = menu.handle_event(event)
            if selected_map:
                map_data = get_text_file(str(selected_map))
                playing = True

    screen.fill((30, 30, 30))

    if playing:
        renderer.draw_connections(map_data)
        renderer.draw_zones(map_data)
        renderer.draw_back_button()
    else:
        menu.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
