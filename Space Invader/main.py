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

def player():
    screen.blit(playerImg,(playerX,playerY))
#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0)) #RGB

    player()
    pygame.display.update()