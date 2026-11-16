import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 60)

        self.difficulties = ["easy", "medium", "hard"]
        self.buttons = []
        for i, difficulty in enumerate(self.difficulties):
            button = pygame.Rect(100, 100 + i * 100, 300, 70)
            self.buttons.append((button, difficulty))

    def draw(self):
        self.screen.fill((30, 30, 30))

        for button, difficulty in self.buttons:
            pygame.draw.rect(self.screen, "white", button, 2)

            text = self.font.render(difficulty.upper(), True, "white")
            text_rect = text.get_rect(center = button.center)

            self.screen.blit(text, text_rect)
