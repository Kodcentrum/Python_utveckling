import pygame, sys

from swedish_key_mapper import SwedishKeyMapper as KM

#kvar snyggare bild, obs bör vara rund för att fungera med koden.
#mållinje, finns, men varvräknare skulle kanske vara kul.
#fixa knapparna


pygame.init()

size = width, height = 600,600
green = (34,139,34)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)

# Startposition
x = 300
y = 100

radius_car = 10
tracksize = 150
outercircle_radius = 280
innercircle_radius = outercircle_radius-tracksize

#draws background with the car at the starting position. Technically redundant code, but probably useful to show.
screen = pygame.display.set_mode(size)
screen.fill(green)
outercircle = pygame.draw.circle(screen,black,(300,300),outercircle_radius, tracksize)
finish_line = pygame.draw.line(screen, white, (285, 170), (285, 20),3)

class Bil(pygame.sprite.Sprite):
    def __init__(self, surface, x_pos, y_pos):
        super().__init__()

        self.image = surface
        self.rect = surface.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class Rörese:
    def ändra_x_för(self, obj, x):
        if hasattr(obj, 'rect'):
            obj.rect.x += x

    def ändra_y_för(self, obj, y):
        if hasattr(obj, 'rect'):
            obj.rect.y += y


all_sprites = pygame.sprite.Group()
ball_surface = pygame.image.load("bilder/ball.png")
bil = Bil(ball_surface, x, y)
all_sprites.add(bil)
rörelse = Rörese()

while 1:
    for event in pygame.event.get():
        # Closes window and program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Tracks which keys are pressed in a given frame
        # Not working, hold down buttons. Fix later...
        trycka = KM(pygame.key.get_pressed())

        if trycka.på("vänsterpil"):
            rörelse.ändra_x_för(bil, -5)
        if trycka.på("högerpil"):
            rörelse.ändra_x_för(bil, 5)
        if trycka.på("nedåtpil"):
            rörelse.ändra_y_för(bil, 5)
        if trycka.på("uppåtpil"):
             rörelse.ändra_y_för(bil, -5)

        # Recreates background,grass, tracks without the cars previous position
        screen.fill(green)
        outercircle = pygame.draw.circle(screen, black, (300, 300), outercircle_radius, tracksize)
        finish_line = pygame.draw.line(screen, white, (285, 170), (285, 20),3)
        # Redraws the car on our new "clean" background with it's new coordinates!
        all_sprites.draw(screen)
        pygame.display.update()
        # Checks if the car goes off the track, if yez then the race starts over.
        if (innercircle_radius > (abs(x-300)**2+abs(y-300)**2)**0.5) or (outercircle_radius < (abs(x-300)**2+abs(y-300)**2)**0.5):
            x=300
            y=100
