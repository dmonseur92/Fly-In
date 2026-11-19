import pygame
from pathlib import Path

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 60)
        self.center_x = screen.get_width() // 2
        self.center_y = screen.get_height() // 2
        self.difficulties = ["easy", "medium", "hard", "challenger"]
        self.chosen_difficulty = None
        self.buttons = []
        self.maps = []

        self.show_difficulties()

    def show_difficulties(self):
        self.chosen_difficulty = None
        self.buttons.clear()

        for i, difficulty in enumerate(self.difficulties):
            button = pygame.Rect(0, 0, 300, 70)
            button.center = (self.center_x, self.center_y + (i - 1) * 100)
            self.buttons.append((button, difficulty))

    def show_maps(self):
        self.maps = self.get_maps()
        self.buttons.clear()

        for i, map_file in enumerate(self.maps):
            button = pygame.Rect(0, 0, 300, 70)
            button.center = (self.center_x, self.center_y + (i - 1) * 100)
            self.buttons.append((button, map_file))

        # Bouton BACK
        back_button = pygame.Rect(0, 0, 300, 70)
        back_button.center = (self.center_x, self.center_y + (len(self.maps) + 1) * 100)
        self.buttons.append((back_button, "BACK"))

    def draw(self):
        self.screen.fill((30, 30, 30))

        for i, (button, item) in enumerate(self.buttons):
            if isinstance(item, Path):
                label = item.stem.upper()
            else:
                label = item.upper()

            text = self.font.render(label, True, "white")
            text_rect = text.get_rect()

            button.width = text_rect.width + 60
            button.height = text_rect.height + 30
            button.center = (self.center_x, button.centery)

            pygame.draw.rect(self.screen, "white", button, 2)
            text_rect.center = button.center
            self.screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button, item in self.buttons:
                if button.collidepoint(event.pos):
                    if item == "BACK":
                        self.show_difficulties()
                    elif isinstance(item, Path):
                        return item
                    else:
                        self.chosen_difficulty = item
                        self.show_maps()
                    return

    def get_maps(self):
        folder = Path("maps") / self.chosen_difficulty
        return sorted(folder.glob("*.txt"))

