# encoding: utf-8
import pygame
import random
from classes import Score, IntroScreen, Screen, Player, Wall

pygame.init()

should_run = True

screen = Screen('FlapPyLadies')
score = Score()
clock = pygame.time.Clock()

IntroScreen(screen.obj)

while should_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Player.speed = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                Player.speed = 5

    screen.fill()

    # Logica do background
    screen.backgroung_position -= 2
    if screen.backgroung_position * -1 == screen.backgroung_limit:
        screen.backgroung_position = 0

    # Criando o jogador
    player = Player(45, 45)
    player.draw(screen.obj)

    Player.y += Player.speed

    # Criando os muros
    image_wallup = pygame.image.load('img/img_wallup.png')
    image_walldown = pygame.image.load('img/img_walldown.png')

    upper_wall = Wall(0)
    upper_wall.draw(screen.obj, image_wallup)

    bottom_wall = Wall(Wall.height + Wall.distance)
    bottom_wall.draw(screen.obj, image_walldown)

    score.draw(screen.obj)

    if Player.x == Wall.x + Wall.length:
        score.current += 1

    # Colisoes com topo e fundo da tela
    if (Player.y > Screen.bottom_limit or Player.y < Screen.upper_limit):
        Player.speed = 0
        Wall.speed = 0

    # Colisoes com os muros
    collisions = [player.obj.colliderect(upper_wall.obj),
                  player.obj.colliderect(bottom_wall.obj)]

    # Se colidir com algum dos muros pare o jogo
    if True in collisions:
        Player.speed = 0
        Wall.speed = 0

    Wall.x -= Wall.speed

    if Wall.x < -60:
        Wall.x = 700
        Wall.height = random.randint(0, 350)

    # Pygame FPS e atualizacao da tela
    pygame.display.flip()
    clock.tick(60)

# Caso saia do loop, finalize o jogo
pygame.quit()
