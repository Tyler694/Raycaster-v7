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
def findNextTile(tileX, tileY):
    TILE_DISTX = ((tileX + 1) * 100) - player.x

    n = 0
    s = 0
    e = 0
    w = 0
    while map[int(tileX + w)][int(tileY)] == 0:
        w += 1
        pygame.draw.circle(screen, (0, 255, 0), ((tileX + w) * 100, player.y), 5)
    while map[int(tileX - e)][int(tileY)] == 0:
        pygame.draw.circle(screen, (0, 255, 0), ((tileX - e) * 100, player.y), 5)
        e += 1
    while map[int(tileX)][int(tileY - s)] == 0:
        pygame.draw.circle(screen, (0, 255, 0), (player.x, (tileY - s) * 100), 5)
        s += 1
    while map[int(tileX)][int(tileY + n)] == 0:
        n += 1
        pygame.draw.circle(screen, (0, 255, 0), (player.x, (tileY + n) * 100), 5)

    #print(TILE_DISTX * math.tan(player.angle * (180/math.pi)))

    pygame.draw.circle(screen, (0,100,0), ((tileX + 1) * 100, player.y + (TILE_DISTX * math.tan((player.angle * 180 / math.pi) / 2))), 5)
    pygame.draw.line(screen, (0,0,255), (player.x, player.y), ((tileX + 1) * 100, player.y))

while running:
    screen.fill((70,70,70))
   #print((player.angle * 180 / math.pi) / 2)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawMap()
    tileX, tileY = get_tile(player.x, player.y)
    findNextTile(tileX, tileY)
    player.draw()
    player.move()

    pygame.display.flip()
    clock.tick(60)