from turtle import width
import pygame
from pyparsing import Char
import gameStates
import graphics
from collisions import Collision
from platforms import Platforms
from trash import Trash

class Chara:
    VEL_X = 4
    VEL_Y = 10
    JUMP = False
    MOVE_L = False
    MOVE_R = False
    ACCELERATION = 0.25

    def movement(self, binboy):
    
        Chara.new_player_x = binboy.x
        Chara.new_player_y = binboy.y

        Chara.VEL_Y += Chara.ACCELERATION
        Chara.new_player_y += Chara.VEL_Y

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and binboy.x - Chara.VEL_X > 0 and binboy.x > 0:  #LEFT
            Chara.new_player_x -= Chara.VEL_X
            Chara.MOVE_L = True
            Chara.MOVE_R = False
        elif keys_pressed[pygame.K_d] and binboy.x + Chara.VEL_X < graphics.Window.WIDTH - 100: #RIGHT
            Chara.new_player_x += Chara.VEL_X
            Chara.MOVE_R = True
            Chara.MOVE_L = False
        else:
            Chara.MOVE_L = False
            Chara.MOVE_R = False
        
        Collision.checkXcolli(Chara.new_player_x, binboy)
        Collision.checkYcolli(Chara.new_player_y, binboy)
        Collision.checkTrashColli(binboy)

        if  keys_pressed[pygame.K_SPACE] and Collision.player_on_ground:
            Chara.VEL_Y = -7    

class Screen:
    SCROLL_INDEX = 0
    VEL_X = 5
    Vel_Y = 15

    def scroll(self, binboy):
        if Chara.MOVE_R and binboy.x - Chara.VEL_X > graphics.Window.WIDTH - 500 and Screen.SCROLL_INDEX != gameStates.GameState.END_OF_LEVEL:
            Screen.SCROLL_INDEX += Screen.VEL_X
            binboy.x -= Chara.VEL_X
            for plat in Platforms.PLATFORMS:
                plat.x -= Chara.VEL_X
            for trash in Trash.TRASH:
                trash.x -= Chara.VEL_X
            for trash in Trash.TRASH1:
                trash.x -= Chara.VEL_X    
        if Chara.MOVE_L and binboy.x - Chara.VEL_X < 300 and Screen.SCROLL_INDEX != gameStates.GameState.LEVEL_START:
            Screen.SCROLL_INDEX -= Screen.VEL_X
            binboy.x += Chara.VEL_X
            for plat in Platforms.PLATFORMS:
                plat.x += Chara.VEL_X
            for trash in Trash.TRASH:
                trash.x += Chara.VEL_X
            for trash in Trash.TRASH1:
                trash.x += Chara.VEL_X
