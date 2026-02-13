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

def findHorizontalLine():

        if player.angle > (3 * math.pi) / 2 or player.angle < math.pi / 2:
            #East
            i = 0
            x = tileX * 100 + TILE_SIZE * i
            y = player.y + (math.tan((player.angle)) * ((tileX * 100 + TILE_SIZE * i) - player.x))
            if x >= 800:
                x = 700
            if y <= 0:
                y = 100
            if y >= 800:
                y = 700

            while map[int(x // 100)][int(y // 100)] == 0:
                x = tileX * 100 + TILE_SIZE * (i+1)
                y = player.y + (math.tan((player.angle)) * ((tileX * 100 + TILE_SIZE * (i+1)) - player.x))

                if x >= 800:
                    break
                if x <= 0:
                    break
                if y <= 0:
                    break
                if y >= 800:
                    break


                pygame.draw.circle(screen, (255,0,0), (x, y), 5)
                i+=1


        else:
            #West
            i = 0

            x = tileX * 100 - TILE_SIZE * i
            y = player.y + (math.tan((player.angle))) * ((tileX * 100 - TILE_SIZE * i) - player.x)

            if x <= 0:
                x = 100
            if y >= 800:
                y = 700
            if y <= 0:
                y = 100

            while map[int(x // 100)][int(y // 100)] == 0:

                x = tileX * 100 - TILE_SIZE * i
                y = player.y + (math.tan((player.angle))) * ((tileX * 100 - TILE_SIZE * i) - player.x)

                if x <= 0:
                    break
                if y >= 800:
                    break
                if y <= 0:
                    break
                pygame.draw.circle(screen, (255,0,0), (x, y), 5)

                i+=1
        return x,y
def findVerticalLine():
        #North
        if player.angle < 0 or player.angle > math.pi:
            i = 0
            x = player.x - (math.tan((player.angle - ((3 * math.pi) / 2))) * ((tileY * 100 - TILE_SIZE * i) - player.y))
            y = tileY * 100 - TILE_SIZE * i
            if x > 800:
                x = 700
            if x < 0:
                x = 100
            if y <= 0:
                y = 100

            while map[int(x // 100)][int(y // 100)] == 0:
                x = player.x - (math.tan((player.angle - ((3 * math.pi) / 2))) * ((tileY * 100 - TILE_SIZE * i) - player.y))
                y = tileY * 100 - (TILE_SIZE * i)

                if x > 800:
                    break
                if x < 0:
                    break
                if y <= 0:
                    break
                pygame.draw.circle(screen, (255,0,0), (x, y), 5)

                i += 1
        else:
                i = 0
                #South
                x = player.x - (math.tan((player.angle - ((3 * math.pi) / 2))) * ((tileY * 100 + TILE_SIZE * i) - player.y))
                y = tileY * 100 + TILE_SIZE * i

                if x >= 800:
                    x = 700
                if x <= 0:
                    x = 100
                if y <= 0:
                    y = 100

                while map[int(x//100)][int(y//100)+1] == 0:
                    x = player.x - (math.tan((player.angle - ((3 * math.pi) / 2))) * ((tileY * 100 + TILE_SIZE * (i + 1)) - player.y))
                    y = tileY * 100 + TILE_SIZE * (i + 1)
                    if x >= 800:
                        break
                    if x <= 0:
                        break
                    if y <= 0:
                        break

                    pygame.draw.circle(screen, (255, 0, 0), (x, y), 5)
                    i+=1
        return x,y
def rayCast():
    HITXH,HITYH = findHorizontalLine()
    HITXV,HITYV = findVerticalLine()


    HorizontalDist = math.sqrt((abs(HITXH - player.x)*abs(HITXH - player.x)) + (abs(HITYH - player.y)*abs(HITXH - player.x)))
    VerticalDist = math.sqrt((abs(HITXV - player.x)*abs(HITXV - player.x)) + (abs(HITYV - player.y)*abs(HITXV - player.x)))

    #print("Vertical",VerticalDist, "Horizontal", HorizontalDist)

    if VerticalDist > HorizontalDist:
        #Horizontal LEFT RIGHT
        pygame.draw.line(screen, (255,0,0), (player.x, player.y), (HITXH, HITYH))
    else:
        #Vertical TOP BOTTOM
        pygame.draw.line(screen, (0,255,0), (player.x, player.y), (HITXV, HITYV))




while running:
    screen.fill((70,70,70))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Dist From First Vertical line
    #((tileX * 100 + TILE_SIZE) - player.x)
    #math.tan(360 - (player.angle * 180 / math.pi)) * ((tileX * 100 + TILE_SIZE) - player.x)

    #Dist From First Horizontal Line
    #(100 - ((tileY * 100 + TILE_SIZE) - player.y))

    drawMap()
    tileX, tileY = get_tile(player.x, player.y)
    rayCast()
    player.draw()
    player.move()

    pygame.display.flip()
    clock.tick(60)