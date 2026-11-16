import pygame
from parsing import get_text_file
from renderer import Renderer
from menu import Menu

pygame.init()



screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
pygame.display.set_caption("Fly-In")

clock = pygame.time.Clock()

map_data = get_text_file("maps/hard/03_ultimate_challenge.txt")
renderer = Renderer(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False
    screen.fill((30, 30, 30))

    # renderer.draw_connections(map_data)
    # renderer.draw_zones(map_data)
    # print("Map :", map_data)
    # print("Zones :", len(map_data.zone_list))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
