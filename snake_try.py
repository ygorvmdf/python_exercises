import pygame
from random import randint
import math
from time import sleep


class Rect:
    def __init__(self, x, y, width, height,):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


pygame.init()

# Screen
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Snake Game")

# Snake
snakeWidth = 10
snakeHeight = 10
snake_change = [4, 0]

# Food
foodWidth = 3
foodHeight = 3
foodX = randint(5, 885)
foodY = randint(35, 585)
hit = 0
speed = 0.08

# Edge
# top edge
topEdgeWidth = 900
topEdgeHeight = 5
topEdgeX = 0
topEdgeY = 30
# Bottom edge
botEdgeX = 0
botEdgeY = 595
# Left Edge
rightEdgeWidth = 5
rightEdgeHeight = 600
rightEdgeX = 0
rightEdgeY = 0
# Right Edge
leftEdgeX = 895
leftEdgeY = 0

# Tail
tailWidth = snakeWidth
tailHeight = snakeHeight
tail = [450, 320]
tail_change = [0, 0]
snakeBody = [[tail, tailWidth, tailHeight], [[0, 0], tailWidth, tailHeight]]
change = []

# Game over
over_font = pygame.font.Font('freesansbold.ttf', 90)
overX = 400
overY = 600

# Score
font = pygame.font.Font('freesansbold.ttf', 25)
scoreX = 10
scoreY = 5


def showGame_over(x, y):
    over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (x, y))


def sumList(list1, list2):
    return [list1[0] + list2[0], list1[1] + list2[1]]


def subList(list1, list2):
    return [list1[0] - list2[0], (list1[1] - list2[1])]


def multList(list1, num):
    return [list1[0] * num, list1[1] * num]


def createTail():
    width = 10
    height = 10
    bodyPosition = [2000, 2000]
    ret = [bodyPosition, width, height]
    snakeBody.append(ret)


def showScore(x, y):
    score = font.render("Score: " + str(hit * 25), True, (255, 255, 255))
    screen.blit(score, (x, y))


def showSpeed(x, y):
    speed = font.render("Speed: " + str(hit), True, (255, 255, 255))
    screen.blit(speed, (x, y))


game_end = False
run = True
while run:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # check if keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if snake_change[0] == 0:
                    snake_change[0] = 10
                    snake_change[1] = 0
            if event.key == pygame.K_LEFT:
                if snake_change[0] == 0:
                    snake_change[0] = -10
                    snake_change[1] = 0
            if event.key == pygame.K_UP:
                if snake_change[1] == 0:
                    snake_change[1] = -10
                    snake_change[0] = 0
            if event.key == pygame.K_DOWN:
                if snake_change[1] == 0:
                    snake_change[1] = 10
                    snake_change[0] = 0

    # Snake movement
    snakeBody[0][0] = sumList(snakeBody[0][0], snake_change)
    sleep(speed)

    # Tail movement
    for c, v in enumerate(snakeBody):
        if c == 1:
            posI = snakeBody[c][0]
            snakeBody[c][0] = subList(snakeBody[c - 1][0], snake_change)
            posF = snakeBody[c][0]
            change = subList(posF, posI)
        elif c > 1:
            posI = snakeBody[c][0]
            snakeBody[c][0] = subList(snakeBody[c - 1][0], change)
            posF = snakeBody[c][0]
            change = subList(posF, posI)

    # If the head of the snake eat(hit) the food
    distance = math.sqrt(math.pow(foodX - snakeBody[0][0][0], 2) + math.pow(foodY - snakeBody[0][0][1], 2))
    if distance < 10:
        foodX = randint(5, 885)
        foodY = randint(35, 585)
        hit += 1
        createTail()
        createTail()
        speed = (speed * 49) / 50

    # check if the head hits the edge
    if snakeBody[0][0][0] <= 0 or snakeBody[0][0][0] >= 890 or snakeBody[0][0][1] >= 590 or snakeBody[0][0][1] <= 35:
        game_end = True
        run = False

    # if the snake hits itself
    for i, bodyPiece in enumerate(snakeBody):
        if i == 0:
            pass
        else:
            if snakeBody[0][0][0] == bodyPiece[0][0] and snakeBody[0][0][1] == bodyPiece[0][1]:
                game_over = True

    # Show speed
    showSpeed(750, 5)

    # show score
    showScore(scoreX, scoreY)

    # drawing the snake
    for v in snakeBody:
        if snakeBody is None:
            pass
        else:
            pygame.draw.rect(screen, (255, 255, 255), (v[0][0], v[0][1], v[1], v[2]))

    pygame.draw.rect(screen, (255, 255, 255), (leftEdgeX, leftEdgeY, rightEdgeWidth, rightEdgeHeight))
    pygame.draw.rect(screen, (255, 255, 255), (rightEdgeX, rightEdgeY, rightEdgeWidth, rightEdgeHeight))
    pygame.draw.rect(screen, (255, 255, 255), (botEdgeX, botEdgeY, topEdgeWidth, topEdgeHeight))
    pygame.draw.rect(screen, (255, 255, 255), (topEdgeX, topEdgeY, topEdgeWidth, topEdgeHeight))
    pygame.draw.rect(screen, (255, 255, 255), (foodX, foodY, foodWidth, foodHeight))
    pygame.display.update()

    while game_end:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game_end = False

        # Initial position
        snakeBody = [[[450, 320], tailWidth, tailHeight], [[445, 320], tailWidth, tailHeight]]

        # show score and ax speed
        showScore(180, 180)
        showSpeed(600, 170)

        # Game over text
        showGame_over(170, 200)

        for value in snakeBody:
            pygame.draw.rect(screen, (255, 255, 255), (value[0][0], value[0][1], tailWidth, tailHeight))
        pygame.draw.rect(screen, (255, 255, 255), (leftEdgeX, leftEdgeY, rightEdgeWidth, rightEdgeHeight))
        pygame.draw.rect(screen, (255, 255, 255), (rightEdgeX, rightEdgeY, rightEdgeWidth, rightEdgeHeight))
        pygame.draw.rect(screen, (255, 255, 255), (botEdgeX, botEdgeY, topEdgeWidth, topEdgeHeight))
        pygame.draw.rect(screen, (255, 255, 255), (topEdgeX, topEdgeY, topEdgeWidth, topEdgeHeight))
        pygame.display.update()
