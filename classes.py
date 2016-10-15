# encoding: utf-8
import pygame
import random


class Score(object):
    def __init__(self):
        self.current = 0
        self.gameover = False

    def draw(self, screen):
        font = pygame.font.Font('fonts/geo.ttf', 55)
        text = font.render(str(self.current), True, [255, 255, 255])
        screen.blit(text, [350, 20])


class IntroScreen(object):
    start_image = pygame.image.load('img/start.png')
    logo_image = pygame.image.load('img/logoPython.png')

    def __init__(self, screen):
        screen.fill([255, 255, 255])
        screen.blit(self.logo_image, [40, 300])
        screen.blit(self.start_image, [170, 50])

        pygame.display.update()
        pygame.time.wait(2000)


class GameoverScreen(object):
    image = pygame.image.load('img/gameover.png')

    def draw(self, screen, points):
        screen.fill([255, 255, 255])
        screen.blit(self.image, (175, 20))
        font = pygame.font.Font('fonts/geo.ttf', 40)
        text = font.render(str(points), True, [238, 37, 79])
        screen.blit(text, [410, 43])
        pygame.display.flip()


class Screen(object):
    upper_limit = 0
    bottom_limit = 450
    resolution = (700, 497)
    backgroung_limit = 1320
    backgroung_position = 0
    main_image = pygame.image.load('img/bg.jpg')
    aux_image = pygame.image.load('img/bg.jpg')

    def __init__(self, display_name):
        self.obj = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption(display_name)

    def fill(self):
        self.obj.blit(self.main_image, (self.backgroung_position, 0))
        self.obj.blit(self.aux_image, (self.backgroung_position +
                                       self.backgroung_limit, 0))


class Wall(object):
    x = 700
    height = random.randint(0, 350)
    length = 70
    distance = 150
    speed = 4

    def __init__(self, y_position):
        if y_position != 0:
            self.height += 500

        self.y = y_position
        self.obj = pygame.Rect(self.x, y_position,
                               self.length, self.height)

    def draw(self, screen, image):
        if self.y == 0:
            self.y = self.height - 500

        screen.blit(image, [self.x, self.y])


class Player(object):
    x = 350
    y = 250
    speed = 0
    image = pygame.image.load('img/player.png')

    def __init__(self, length, height):
        self.obj = pygame.Rect(self.x, self.y, length, height)

    def draw(self, screen):
        return screen.blit(self.image, [self.x, self.y])

    def collide_with(self, rectangle):
        self.obj.colliderect(rectangle)
