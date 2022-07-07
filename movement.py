from turtle import width
import pygame
from pyparsing import Char
import gameStates
import graphics
from collisions import Collision
from platforms import Platforms

class Chara:
    VEL_X = 4
    VEL_Y = 10
    JUMP = False
    MOVE_L = False
    MOVE_R = False
    ACCELERATION = 0.25
    heigth = 80
    width = 48

    def movement(self, binboy):
        
        Chara.new_player_x = binboy.x
        Chara.new_player_y = binboy.y

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and binboy.x - Chara.VEL_X > 0: #LEFT
            # binboy.x -= Chara.VEL_X
            Chara.new_player_x -= Chara.VEL_X
            Chara.MOVE_L = True
            Chara.MOVE_R = False
        elif keys_pressed[pygame.K_d] and binboy.x + Chara.VEL_X < graphics.Window.WIDTH - 100: #RIGHT
            # binboy.x += Chara.VEL_X
            Chara.new_player_x += Chara.VEL_X
            Chara.MOVE_R = True
            Chara.MOVE_L = False
        else:
            Chara.MOVE_L = False
            Chara.MOVE_R = False

        Chara.new_player_rect = pygame.Rect(Chara.new_player_x,binboy.y,Chara.width, Chara.heigth)
        Chara.x_collision = False
        for Chara.platform in Platforms.PLATFORMS:
            if Chara.platform.colliderect(Chara.new_player_rect):
                Chara.x_collision = True
                break
        if Chara.x_collision == False:
            binboy.x = Chara.new_player_x

        
        Chara.VEL_Y += Chara.ACCELERATION
        Chara.new_player_y += Chara.VEL_Y

        Chara.new_player_rect = pygame.Rect(binboy.x, Chara.new_player_y, Chara.width, Chara.heigth)
        Chara.y_collision = False
        Chara.player_on_ground = False

        for Chara.platform in Platforms.PLATFORMS:
            if Chara.platform.colliderect(Chara.new_player_rect):
                Chara.y_collision =  True
                Chara.VEL_Y  = 0
                # if the player is below the player
                if Chara.platform[1] > Chara.new_player_y:
                    # stick the player to the platform
                    binboy.y = Chara.platform[1] - Chara.heigth # 75 is player height
                    Chara.player_on_ground =  True
                break

        if Chara.y_collision == False:
            binboy.y = Chara.new_player_y


        # Collision.checkXcolli()
        # Collision.checkYcolli()

        if  keys_pressed[pygame.K_SPACE] and Chara.player_on_ground:
            Chara.VEL_Y = -7
            #Chara.JUMP = True

        # if Chara.JUMP:
        #     binboy.y -= Chara.VEL_Y
        #     Chara.VEL_Y -= 1
        #     #Collision.checkYcolli()
        #     if Chara.VEL_Y < -10:
        #         Chara.JUMP = False
        #         Chara.VEL_Y = 10


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
        if Chara.MOVE_L and binboy.x - Chara.VEL_X < 300 and Screen.SCROLL_INDEX != gameStates.GameState.LEVEL_START:
            Screen.SCROLL_INDEX -= Screen.VEL_X
            binboy.x += Chara.VEL_X
            for plat in Platforms.PLATFORMS:
                plat.x += Chara.VEL_X
