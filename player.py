import math

import pygame

class Player:
    def __init__(self):
        self.x = 200
        self.y = 200
        self.angle = 6.28
        self.screen = pygame.display.get_surface()

    def draw(self):
        pygame.draw.circle(self.screen, (255,0,0), (self.x, self.y), 5)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += math.cos(self.angle)
            self.y += math.sin(self.angle)
        if keys[pygame.K_s]:
            self.x += -math.cos(self.angle)
            self.y += -math.sin(self.angle)
        if keys[pygame.K_a]:
            self.angle += 0.03
        if keys[pygame.K_d]:
            self.angle -= 0.03

        if self.angle < 0:
            self.angle = math.tau
        elif self.angle > math.tau:
            self.angle = 0
