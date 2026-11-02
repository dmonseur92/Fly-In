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
        font = pygame.font.SysFont(None, 36)
        text = font. render(f"0 / {zone.max_drones}", True, "white")
        position = self.grid_to_screen(zone.x - 0.15, zone.y + 0.25)
        self.screen.blit(text, position)

    def draw_zones(self, map_data):
        for zone in map_data.zone_list:
            self.draw_zone(zone)

    def draw_connections(self, map_data):
        zones = {zone.name: zone for zone in map_data.zone_list}

        for connection in map_data.connexion_list:
            start, end = connection.split("-")

            zone1 = zones[start]
            zone2 = zones[end]

            pos1 = self.grid_to_screen(zone1.x, zone1.y)
            pos2 = self.grid_to_screen(zone2.x, zone2.y)

            pygame.draw.line(self.screen, "white", pos1, pos2, 3)
