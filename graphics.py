from platform import platform
from tokenize import PseudoToken
from turtle import width
import pygame
import os
import movement
import platforms
import trash
import random
from pygame import mixer


pygame.init()

class Binboy:
    binboy_height = 100#80
    binboy_width = 50#48
    posX = platforms.Platforms.setPlayerPosition()
    posY = platforms.Platforms.setPlayerPositionY()
    #BINBOY_POS = pygame.Rect(100, 438 - 70, 50, 75)
    BINBOY_POS = pygame.Rect(posX,posY, binboy_width, binboy_height)
    RUN_FRAME = 0

    #Set the movement.Chara character image
    BINBOY_IDOL = pygame.image.load(os.path.join('assets', 'binboyTEST1.png'))
    BINBOY_IDOL = pygame.transform.scale(BINBOY_IDOL, (binboy_width, binboy_height))

    #The character images when moving right
    BINBOY_RIGHT = [None]*10
    for rightIndex in range(1, 11):
        BINBOY_RIGHT[rightIndex - 1] = pygame.image.load(os.path.join('assets', 'binboy_right_' + str(rightIndex) + '.png'))
        rightIndex += 1
    for rightIndex in range(1, 11):
        BINBOY_RIGHT[rightIndex - 1] = pygame.transform.scale(BINBOY_RIGHT[rightIndex - 1], (binboy_width, binboy_height))
        rightIndex += 1

    #The character images when moving left
    BINBOY_LEFT = [None]*10
    for leftIndex in range(1, 11):
        BINBOY_LEFT[leftIndex - 1] = pygame.image.load(os.path.join('assets', 'binboy_left_' + str(leftIndex) + '.png'))
        leftIndex += 1
    for leftIndex in range(1, 11):
        BINBOY_LEFT[leftIndex - 1] = pygame.transform.scale(BINBOY_LEFT[leftIndex - 1], (binboy_width, binboy_height))
        leftIndex += 1

    def draw_binboy(self):
        if Binboy.RUN_FRAME > 54: 
            Binboy.RUN_FRAME = 0
        if movement.Chara.JUMP:
            if movement.Chara.MOVE_R:
                Window.WIN.blit(Binboy.BINBOY_RIGHT[4], (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
            if movement.Chara.MOVE_L:
                Window.WIN.blit(Binboy.BINBOY_LEFT[4], (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
            else:
                Window.WIN.blit(Binboy.BINBOY_RIGHT[4], (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
        elif movement.Chara.MOVE_R:
            Window.WIN.blit(Binboy.BINBOY_RIGHT[Binboy.RUN_FRAME//6], (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
            Binboy.RUN_FRAME += 1
        elif movement.Chara.MOVE_L:
            Window.WIN.blit(Binboy.BINBOY_LEFT[Binboy.RUN_FRAME//6], (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
            Binboy.RUN_FRAME += 1
        else:
            Window.WIN.blit(Binboy.BINBOY_IDOL, (Binboy.BINBOY_POS.x, Binboy.BINBOY_POS.y))
            Binboy.RUN_FRAME = 0

class Window:
    pygame.display.set_caption("Binboy")
    WIDTH, HEIGHT = 1600,900
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    BEACH = pygame.image.load(os.path.join('assets', 'beach.png')).convert_alpha()
    SKY = (180, 180, 255)
    GRASS = (100, 200, 100)
    SAND = (248,200,129)
    GROUND = pygame.Rect(0, HEIGHT - HEIGHT/8, WIDTH, 200)
    BACKGROUND = (245, 66, 152)
    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 32)
    TRASH = pygame.image.load(os.path.join('assets', 'colo_cup_1.png'))
    TRASH = pygame.transform.scale(TRASH, (50, 50))
    TRASH1 = pygame.image.load(os.path.join('assets', 'trash_can.png'))
    TRASH1 = pygame.transform.scale(TRASH1, (50, 50))
    TRASH2 = pygame.image.load(os.path.join('assets', 'plastic_bin_open.png'))
    TRASH2 = pygame.transform.scale(TRASH2, (50, 50))
    SCORE = 0
    mixer.music.load("theme.mp3")
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)

    def draw_level_1(self, SCROLL_INDEX):
        score = str(Window.SCORE)
        text = Window.font.render(f'Score {score}', True,  Window.white)
        textRect = text.get_rect()
        textRect.center = (60, 20)
        #Window.WIN.fill(Window.SKY)
        Window.WIN.blit(Window.BEACH,(0 - SCROLL_INDEX,0))
        #pygame.draw.rect(Window.WIN, Window.BACKGROUND, pygame.Rect(Window.WIDTH - SCROLL_INDEX, 0, Window.WIDTH, Window.HEIGHT))
        Window.WIN.blit(text, textRect)
       # pygame.draw.rect(Window.WIN, Window.GRASS, Window.GROUND)

        Binboy.draw_binboy(Binboy)
        for plat in platforms.Platforms.PLATFORMS:
            pygame.draw.rect(Window.WIN, Window.SAND, plat)
        
        for t in trash.Trash.TRASH:
                Window.WIN.blit(Window.TRASH, (t.x, t.y))
        for t in trash.Trash.TRASH1:
                Window.WIN.blit(Window.TRASH1, (t.x, t.y))

        pygame.display.update()
    
    def draw_bonus_level(self):
        ground = Window.GROUND
        ground.y = Window.HEIGHT - Window.HEIGHT/3
        Window.WIN.fill(Window.SKY)
        pygame.draw.rect(Window.WIN, Window.GRASS, ground)
        Cans.draw_cans()

        pygame.display.update()

class Cans:
    TRASH_CAN_OPEN = pygame.image.load(os.path.join('assets', 'trash_can_open.png'))
    TRASH_CAN_OPEN = pygame.transform.scale(TRASH_CAN_OPEN, (200, 250))

    PLASTIC_CAN_OPEN = pygame.image.load(os.path.join('assets', 'plastic_bin_open.png'))
    PLASTIC_CAN_OPEN = pygame.transform.scale(PLASTIC_CAN_OPEN, (200, 250))

    PAPER_CAN_OPEN = pygame.image.load(os.path.join('assets', 'paper_bin_open.png'))
    PAPER_CAN_OPEN = pygame.transform.scale(PAPER_CAN_OPEN, (200, 250))

    GLASS_CAN_OPEN = pygame.image.load(os.path.join('assets', 'glass_bin_open.png'))
    GLASS_CAN_OPEN = pygame.transform.scale(GLASS_CAN_OPEN, (200, 250))

    TRASH_CAN_CLOSED = pygame.image.load(os.path.join('assets', 'trash_can_closed.png'))
    TRASH_CAN_CLOSED = pygame.transform.scale(TRASH_CAN_CLOSED, (200, 250))

    PLASTIC_CAN_CLOSED = pygame.image.load(os.path.join('assets', 'plastic_bin_closed.png'))
    PLASTIC_CAN_CLOSED = pygame.transform.scale(PLASTIC_CAN_CLOSED, (200, 250))

    PAPER_CAN_CLOSED = pygame.image.load(os.path.join('assets', 'paper_bin_closed.png'))
    PAPER_CAN_CLOSED = pygame.transform.scale(PAPER_CAN_CLOSED, (200, 250))

    GLASS_CAN_CLOSED = pygame.image.load(os.path.join('assets', 'glass_bin_closed.png'))
    GLASS_CAN_CLOSED = pygame.transform.scale(GLASS_CAN_CLOSED, (200, 250))


    CAN1 = pygame.Rect(Window.WIDTH/5 - 100, Window.HEIGHT/2 - 100, 200, 250)
    CAN2 = pygame.Rect((Window.WIDTH/5)*2 - 100, Window.HEIGHT/2 - 100, 200, 250)
    CAN3 = pygame.Rect((Window.WIDTH/5)*3 - 100, Window.HEIGHT/2 - 100, 200, 250)
    CAN4 = pygame.Rect((Window.WIDTH/5)*4 - 100, Window.HEIGHT/2 - 100, 200, 250)

    def draw_cans():
        Window.WIN.blit(Cans.TRASH_CAN_CLOSED, (Cans.CAN1.x, Cans.CAN1.y))
        Window.WIN.blit(Cans.PLASTIC_CAN_CLOSED, (Cans.CAN2.x, Cans.CAN2.y))
        Window.WIN.blit(Cans.PAPER_CAN_CLOSED, (Cans.CAN3.x, Cans.CAN3.y))
        Window.WIN.blit(Cans.GLASS_CAN_CLOSED, (Cans.CAN4.x, Cans.CAN4.y))