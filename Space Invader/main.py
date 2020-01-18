import pygame
import random

#initialize pygame
pygame.init()
#set screen
screen = pygame.display.set_mode((800,600))
#Background
background = pygame.image.load('stock-vector.jpg')

#set game caption
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_Change = 0

enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_Change = 2
enemyY_Change = 40

def player(x,y):
    screen.blit(playerImg,(x,y))

def enermy(x,y):
    screen.blit(enemyImg,(x,y))
#Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # RGB
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# if keystroke pressed check it weather right or left
        if event.type == pygame.KEYDOWN:
            print("keystroke pressed")
            if event.key == pygame.K_LEFT:
                playerX_Change = -5
            if event.key == pygame.K_RIGHT:
                playerX_Change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0
    #Boundaries of spaceship
    playerX += playerX_Change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # Boundaries of enemy
    enemyX += enemyX_Change
    if enemyX <= 0:
        enemyX_Change = 2
        enemyY += enemyY_Change
    elif enemyX >= 736:
        enemyX_Change = -2
        enemyY += enemyY_Change

    player(playerX,playerY)
    enermy(enemyX, enemyY)
    pygame.display.update()