import math

import pygame

class Player:
    def __init__(self):
        self.x = 200
        self.y = 200
        self.angle = 0
        self.screen = pygame.display.get_surface()
        self.FOV = 90

    def draw(self):
        pygame.draw.circle(self.screen, (0,255,0), (self.x*0.15, self.y*0.15), 3)
        pygame.draw.line(self.screen,(0,255,0), (self.x*0.15,self.y*0.15), ((self.x*0.15)+math.cos(self.angle)*10,(self.y*0.15)+math.sin(self.angle)*10))
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

        self.angle %= math.tau
