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

def CheckRange(num, min, max):
    if num >= max:
        return True
    if num <= min:
        return True

def Clamp(num, min, max):
    if num >= max:
        num = max
    if num <= min:
        num = min
    return num




def drawMap():
    for i, row in enumerate(map):
        for j, tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(screen, (50, 50, 50), (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE-1, TILE_SIZE-1))
            else:
                pygame.draw.rect(screen, (0,0,0), (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE-1, TILE_SIZE-1))

def get_tile(px, py):
    return px // 100, py // 100

def rayCast():
    HITXV, HITYV = VerticalLines()
    HITXH, HITYH = HorizontalLines()

    HORIZONTAL_DIST = (math.sqrt((abs(player.x - HITXH))**2 + (abs(player.y - HITYH))**2))
    VERTICAL_DIST = (math.sqrt((abs(player.x - HITXV))**2 + (abs(player.y - HITYV))**2))

    if HORIZONTAL_DIST > VERTICAL_DIST:
        pygame.draw.line(screen, (255,0,0), (player.x, player.y), (HITXV, HITYV))
    else:
        pygame.draw.line(screen, (0,255,0), (player.x, player.y), (HITXH, HITYH))


def VerticalLines():
    ANGLE = player.angle
    #RIGHT
    if (ANGLE * 180 / math.pi) > 270 or (ANGLE * 180 / math.pi) < 90:

        FIRST_HIT_X = (tileX * TILE_SIZE) + TILE_SIZE
        DISTANCE_X = abs(FIRST_HIT_X - player.x)

        FIRST_HIT_Y = (math.tan(ANGLE) * DISTANCE_X) + player.y

        NEXT_HIT_X = Clamp(FIRST_HIT_X, 0, 700)
        NEXT_HIT_Y = Clamp(FIRST_HIT_Y, 0, 700)

        i = 0
        while map[int(NEXT_HIT_X // 100)][int(NEXT_HIT_Y // 100)] == 0:
            NEXT_HIT_X = FIRST_HIT_X + (TILE_SIZE * i)
            NEXT_HIT_Y = FIRST_HIT_Y + (math.tan(ANGLE) * (TILE_SIZE * i))

            if CheckRange(NEXT_HIT_X, 0, 700): break
            if CheckRange(NEXT_HIT_Y, 0, 700): break

            i += 1
        return NEXT_HIT_X, NEXT_HIT_Y

    #LEFT
    if (ANGLE * 180 / math.pi) < 270 and (ANGLE * 180 / math.pi) > 90:
        FIRST_HIT_X = (tileX * TILE_SIZE)
        DISTANCE_X = abs(player.x - FIRST_HIT_X)

        FIRST_HIT_Y = player.y - (math.tan(ANGLE) * DISTANCE_X)

        NEXT_HIT_X = Clamp(FIRST_HIT_X, 0, 700)
        NEXT_HIT_Y = Clamp(FIRST_HIT_Y, 0, 700)

        i = 0
        while map[int(NEXT_HIT_X // 100)-1][int(NEXT_HIT_Y // 100)] == 0:

            NEXT_HIT_X = FIRST_HIT_X - (TILE_SIZE * i)
            NEXT_HIT_Y = FIRST_HIT_Y - (math.tan(ANGLE) * (TILE_SIZE * i))

            if CheckRange(NEXT_HIT_X, 0, 700): break
            if CheckRange(NEXT_HIT_Y, 0, 700): break

            i += 1
        return NEXT_HIT_X, NEXT_HIT_Y

def HorizontalLines():
    ANGLE = player.angle
    #UP
    if (ANGLE * 180 / math.pi) <= 360 and (ANGLE * 180 / math.pi) >= 180:
        FIRST_HIT_Y = tileY * TILE_SIZE
        DISTANCE_Y = abs(player.y - FIRST_HIT_Y)

        FIRST_HIT_X = (math.tan(ANGLE - ((3 * math.pi) / 2)) * DISTANCE_Y) + player.x

        NEXT_HIT_X = Clamp(FIRST_HIT_X, 0, 700)
        NEXT_HIT_Y = Clamp(FIRST_HIT_Y, 0, 700)

        i = 0
        while map[int(NEXT_HIT_X // 100)][int(NEXT_HIT_Y // 100)-1] == 0:
            NEXT_HIT_Y = FIRST_HIT_Y - (TILE_SIZE * i)
            NEXT_HIT_X = FIRST_HIT_X + (math.tan(ANGLE - ((3 * math.pi) / 2)) * (TILE_SIZE * i))

            if CheckRange(NEXT_HIT_X, 0, 700): break
            if CheckRange(NEXT_HIT_Y, 0, 700): break

            i += 1
        return NEXT_HIT_X, NEXT_HIT_Y

    #DOWN
    if (ANGLE * 180 / math.pi) >= 0 or (ANGLE * 180 / math.pi) <= 180:
        FIRST_HIT_Y = tileY * TILE_SIZE + TILE_SIZE
        DISTANCE_Y = abs(player.y - FIRST_HIT_Y)

        FIRST_HIT_X = player.x - (math.tan(ANGLE - ((3 * math.pi) / 2)) * DISTANCE_Y)

        NEXT_HIT_X = Clamp(FIRST_HIT_X, 0, 700)
        NEXT_HIT_Y = Clamp(FIRST_HIT_Y, 0, 700)

        i = 0
        while map[int(NEXT_HIT_X // 100)][int(NEXT_HIT_Y // 100)] == 0:
            NEXT_HIT_Y = FIRST_HIT_Y + (TILE_SIZE * i)
            NEXT_HIT_X = FIRST_HIT_X - (math.tan(ANGLE - ((3 * math.pi) / 2)) * (TILE_SIZE * i))

            if CheckRange(NEXT_HIT_X, 0, 700): break
            if CheckRange(NEXT_HIT_Y, 0, 700): break

            i += 1
        return NEXT_HIT_X, NEXT_HIT_Y


while running:
    screen.fill((70,70,70))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawMap()
    tileX, tileY = get_tile(player.x, player.y)
    rayCast()
    player.draw()
    player.move()

    pygame.display.flip()
    clock.tick(60)