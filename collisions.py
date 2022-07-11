import pygame
import movement
import graphics
from platforms import Platforms
from trash import Trash

class Collision:
    x_collision = False
    y_collision = False
    player_on_ground = False
    new_player_rect = pygame.Rect(0,0,0,0)
    heigth = 100
    width = 50

    def checkXcolli(new_player_x, binboy):
        Collision.new_player_rect = pygame.Rect(new_player_x,binboy.y,Collision.width, Collision.heigth)
        Collision.x_collision = False
        for Collision.platform in Platforms.PLATFORMS:
            if Collision.platform.colliderect(Collision.new_player_rect):
                Collision.x_collision = True
                break
        if Collision.x_collision == False:
            binboy.x = new_player_x

    def checkYcolli(new_player_y, binboy):
        Collision.new_player_rect = pygame.Rect(binboy.x,new_player_y,Collision.width, Collision.heigth)
        Collision.y_collision = False
        Collision.player_on_ground = False

        for Collision.platform in Platforms.PLATFORMS:
            if Collision.platform.colliderect(Collision.new_player_rect):
                Collision.y_collision = True
                movement.Chara.VEL_Y = 0
                if Collision.platform[1] > new_player_y:
                    binboy.y = Collision.platform[1] - Collision.heigth
                    Collision.player_on_ground = True
                break
        if Collision.y_collision == False:
            binboy.y = new_player_y

    def checkTrashColli(binboy):
        Collision.new_player_rect = pygame.Rect(binboy.x, binboy.y, Collision.width, Collision.heigth)
        for Collision.trash in Trash.TRASH:
            if Collision.trash.colliderect(Collision.new_player_rect):
                Trash.TRASH.remove(Collision.trash)
                graphics.Window.SCORE += 1
        for Collision.trash in Trash.TRASH1:
            if Collision.trash.colliderect(Collision.new_player_rect):
                Trash.TRASH1.remove(Collision.trash)
                graphics.Window.SCORE += 1
    
