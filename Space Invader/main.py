import pygame

#initialize pygame
pygame.init()
#set screen
screen = pygame.display.set_mode((800,600))
#set game caption
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480

def player(x,y):
    screen.blit(playerImg,(x,y))
#Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # RGB
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    playerX += 0.1
    player(playerX,playerY)
    pygame.display.update()