import math

import pygame
from settings import *
from player import *
#setup
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

pygame.display.set_caption("Raycaster V7 - TylerT")

running = True
player = Player()


def drawMap():
    for i, row in enumerate(map):
        for j, tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(screen, (50, 50, 50), (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE-1, TILE_SIZE-1))
            else:
                pygame.draw.rect(screen, (0,0,0), (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE-1, TILE_SIZE-1))
def get_tile(px, py):
    return px // 100, py // 100

def findHorizontalLine(i):
    pygame.draw.circle(screen, (255,0,0), (tileX * 100 + TILE_SIZE * i, player.y + ((math.tan((player.angle))) * ((tileX * 100 + TILE_SIZE * i) - player.x))), 5)

def rayCast():
    for i in range(5):
        findHorizontalLine(i + 1)

while running:
    screen.fill((70,70,70))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Dist From First Vertical line
    #((tileX * 100 + TILE_SIZE) - player.x)
    #math.tan(360 - (player.angle * 180 / math.pi)) * ((tileX * 100 + TILE_SIZE) - player.x)

    drawMap()
    tileX, tileY = get_tile(player.x, player.y)
    print((math.tan((player.angle))) * ((tileX * 100 + TILE_SIZE) - player.x) * -1)
    rayCast()
    player.draw()
    player.move()

    pygame.display.flip()
    clock.tick(60)