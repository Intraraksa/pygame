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
playerX_Change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))
#Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # RGB
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# if keystroke pressed check it weather right or left
        if event.type == pygame.KEYDOWN:
            print("keystroke pressed")
            if event.key == pygame.K_LEFT:
                playerX_Change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_Change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    playerX += playerX_Change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX,playerY)
    pygame.display.update()