import pygame
from maps import Zone, Map, ZoneType

class Renderer:

    def __init__(self, screen):
        self.screen = screen
        self.spacing = 150
        self.center = screen.get_rect().center

    def grid_to_screen(self, x, y):
        screen_x = 200 + x * self.spacing
        screen_y = self.center[1] + y * self.spacing
        return screen_x, screen_y

    def draw_zone(self, zone):
        position = self.grid_to_screen(zone.x, zone.y)
        color = pygame.Color(zone.color or "white")

        pygame.draw.circle(self.screen, color, position, 40)

    def draw_zones(self, map_data):
        for zone in map_data.zone_list:
            self.draw_zone(zone)
