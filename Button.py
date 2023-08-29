import pygame


class Image_Button:
    def __init__(self, screen, path, x_pos, y_pos, enabled):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.image = pygame.image.load(path).convert()
        self.image_rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.image_rect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        return left_click and self.image_rect.collidepoint(mouse_pos)


class Text_Button:
    def __init__(self, screen, text, x_pos, y_pos, enabled, font_size=18):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.screen = screen
        self.enabled = enabled
        self.font_size = font_size

    def draw(self):
        white = (24, 17, 41)  # background
        clr1 = (189, 176, 214)  # text colour
        clr2 = (24, 17, 41)  # text background
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        text_render = font.render(self.text, True, clr1, clr2)
        self.textRect = text_render.get_rect()
        self.textRect.center = (self.x_pos, self.y_pos)
        self.screen.blit(text_render, self.textRect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        return left_click and self.textRect.collidepoint(mouse_pos) and self.enabled
