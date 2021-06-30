import pygame
from random import randint
import math
from pygame import mixer

screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load("game_controller.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('background.png')

# Background sound
mixer.init()
mixer.music.load('background.wav')
mixer.music.play(-1)

# PLayer
playerImage = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(randint(5, 735))
    enemyY.append(randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImage = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 7
bulletState = 'ready'

# Score
pygame.font.init()
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bulletState
    bulletState = 'fire'
    screen.blit(bulletImage, (x + 16, y + 10))


def isCollision(ex, ey, bx, by):
    distance = math.sqrt(math.pow(ex - bx, 2) + math.pow(ey - by, 2))
    if distance < 27:
        return True
    else:
        return False


# events and interactions in the display
run = True
while run:

    # Background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('laser.wav')
                bullet_sound.play()
                if bulletState == 'ready':
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bulletState = 'ready'
            score_value += 1
            enemyX[i] = randint(5, 735)
            enemyY[i] = randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = 'ready'
    if bulletState == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
