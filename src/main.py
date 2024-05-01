import sys
import pygame
import random
from Card import Card
from Player import p1

pygame.init()

game = False
size = width, height = 470, 530
blue = 12, 11, 43
white = (255, 255, 255)
green = 74, 112, 100
background = 69, 73, 87
position = (0, 0)
star = pygame.image.load("Star.png")
sparkle = pygame.image.load("Sparkle.png")
crew = pygame.image.load("crew.drawio.png")
DEFAULT_IMAGE_SIZE = (40, 30)
crew = pygame.transform.scale(crew, DEFAULT_IMAGE_SIZE)
fuelsym = pygame.image.load("fuel.png")
carsym = pygame.image.load("cargo.png")
badge = pygame.image.load("badge.png")
screen = pygame.display.set_mode(size)
screen.fill(blue)

pygame.display.set_caption('StarGazers')
font1 = pygame.font.Font('freesansbold.ttf', 30)
font2 = pygame.font.Font('freesansbold.ttf', 18)
font3 = pygame.font.Font('freesansbold.ttf', 20)

title = font1.render('Welcome to Star Gazers!', True, white)
titleRect = title.get_rect()
titleRect.center = (width / 2, height / 2 - 100)
sub = font3.render('Click to begin', True, white)
subRect = sub.get_rect()
subRect.center = (width / 2, height / 2)

welcomeMessage = [
    "Congratulations, Captain!",
    "After working in space shipping for years,",
    "at long last you’ve been promoted high",
    "enough to have your own ship.",
    "",
    "", ]
welcomeMessage2 = ["Welcome to ..",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "the " + p1.name]

# controls neg space of stats - inverse
moral = 20
fuel = 20
cargo = 20
lawful = 20

welc = Card(white, welcomeMessage, welcomeMessage2, font2, blue, 0, 0, 0, 0, 5,
            0, 0, 20, "What am I doing here???", "I'm so ready", False)
nextc = Card(white, "What's going on here?", "", font2, blue, 5, 10, 0,
             0, 5, 0, 0, 20, "LEFT", "RIGHT", False)

for x in range(40):
    screen.blit(star, (random.randint(0, width), random.randint(0, height)))
    x += 1
for x in range(15):
    screen.blit(sparkle, (random.randint(0, width), random.randint(0, height)))
    x += 1
screen.blit(title, titleRect)
screen.blit(sub, subRect)


def action(which, xp, yp):
    while which.on:
        which.hover(xp, yp)
        if pygame.MOUSEBUTTONDOWN:
            which.choose(xp, yp)


while True:
    position = pygame.mouse.get_pos()
    xpos = position[0]
    ypos = position[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and game is False:
            screen.fill(background)
            pygame.draw.rect(screen, green, pygame.Rect(0, 0, width, 65))
            screen.blit(crew, (40, 14))
            pygame.draw.rect(screen, blue, pygame.Rect(100, 8, 18, 45))
            pygame.draw.rect(screen, green, pygame.Rect(100, 8, 18, p1.crew))
            pygame.draw.rect(screen, blue, pygame.Rect(100, 8, 18, 45), 1)
            screen.blit(carsym, (150, 14))
            pygame.draw.rect(screen, blue, pygame.Rect(210, 8, 18, 45))
            pygame.draw.rect(screen, green, pygame.Rect(210, 8, 18, p1.fuel))
            pygame.draw.rect(screen, blue, pygame.Rect(210, 8, 18, 45), 1)
            screen.blit(fuelsym, (250, 14))
            pygame.draw.rect(screen, blue, pygame.Rect(310, 8, 18, 45))
            pygame.draw.rect(screen, green, pygame.Rect(310, 8, 18, p1.cargo))
            pygame.draw.rect(screen, blue, pygame.Rect(310, 8, 18, 45), 1)
            screen.blit(badge, (350, 14))
            pygame.draw.rect(screen, blue, pygame.Rect(410, 8, 18, 45))
            pygame.draw.rect(screen, green, pygame.Rect(410, 8, 18, p1.law))
            pygame.draw.rect(screen, blue, pygame.Rect(410, 8, 18, 45), 1)
            welc.create()
            game = True
            welc.on = True
        action(welc, xpos, ypos)
        print(welc.on)
        # welc.create()
        # print(position)
        # welc.hover(xpos, ypos)
        # if pygame.MOUSEBUTTONDOWN:
        #     welc.choose(xpos, ypos)
        #     print("next created")
        #     nextc.create()

    pygame.display.flip()
