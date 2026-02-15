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
                pygame.draw.rect(screen, (50, 50, 50), (j * 15, i * 15, 15, 15))
            else:
                pygame.draw.rect(screen, (0,0,0), (j * 15, i * 15, 15, 15))

def get_tile(px, py):
    return px // 100, py // 100

def rayCast():
    for i in range(90):
        ANGLE = (player.angle - (player.FOV / 2)) + (i * math.pi / 180)
        ANGLE %= math.tau

        HITXV, HITYV = VerticalLines(ANGLE)
        HITXH, HITYH = HorizontalLines(ANGLE)

        HORIZONTAL_DIST = (math.sqrt((player.x - HITXH)**2 + (player.y - HITYH)**2))
        VERTICAL_DIST = (math.sqrt((player.x - HITXV)**2 + (player.y - HITYV)**2))

        #HORIZONTAL_DIST = abs(player.y - HITYH)
        #VERTICAL_DIST = abs(player.x - HITXV)

        if HORIZONTAL_DIST > VERTICAL_DIST:
            #VERTICAL_DIST = math.sqrt((VERTICAL_DIST**2) - (abs(player.y - HITYV))**2)

            #pygame.draw.line(screen, (255,255,0), (player.x, player.y), (HITXV, HITYV))
            drawSlice(i, VERTICAL_DIST, "Vertical")
        else:
            #HORIZONTAL_DIST = math.sqrt((HORIZONTAL_DIST**2)-(abs(player.x-HITXH))**2)

            #pygame.draw.line(screen, (255,255,0), (player.x, player.y), (HITXH, HITYH))
            drawSlice(i, HORIZONTAL_DIST,"Horizontal")

def drawSlice(index, dist, side):
    SLICE_WIDTH = 10
    X_POSITION = index * SLICE_WIDTH

    SLICE_HEIGHT = 600 - (dist / 4)
    Y_POSITION = math.floor(600 - SLICE_HEIGHT / 2)

    shade = dist/2.5
    print(SLICE_HEIGHT)

    colour = (0,0,0)

    if side == "Vertical":
        colour = (255-shade,0,0)
    else:
        colour = (0,0,255-shade)

    pygame.draw.rect(screen, colour,(X_POSITION,Y_POSITION,SLICE_WIDTH,SLICE_HEIGHT))
def VerticalLines(ANGLE):
    #RIGHT
    if (ANGLE * 180 / math.pi) >= 270 or (ANGLE * 180 / math.pi) <= 90:

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
    if (ANGLE * 180 / math.pi) <= 270 and (ANGLE * 180 / math.pi) >= 90:
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

def HorizontalLines(ANGLE):
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
    if (ANGLE * 180 / math.pi) >= 360 or (ANGLE * 180 / math.pi) <= 180:
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

    tileX, tileY = get_tile(player.x, player.y)
    rayCast()
    player.move()

    drawMap()
    player.draw()

    pygame.display.flip()
    clock.tick(60)