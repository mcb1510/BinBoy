import pygame
import movement
import graphics
import gameStates
from platforms import Platforms
from trash import Trash

class Collision:
    x_collision = False
    y_collision = False
    player_on_ground = False
    new_player_rect = pygame.Rect(0,0,0,0)
    heigth = 65
    width = 40

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
        
        for Collision.trash in Trash.BANANAS:
            if Collision.trash.colliderect(Collision.new_player_rect):
                Trash.BANANAS.remove(Collision.trash)
                graphics.Window.SCORE += 1
        
        for Collision.trash in Trash.BOTTLES:
            if Collision.trash.colliderect(Collision.new_player_rect):
                Trash.BOTTLES.remove(Collision.trash)
                graphics.Window.SCORE += 1
        
        for Collision.trash in Trash.PLASTICS:
            if Collision.trash.colliderect(Collision.new_player_rect):
                Trash.PLASTICS.remove(Collision.trash)
                graphics.Window.SCORE += 1
        
        for Collision.trash in Trash.NEWSPAPERS:
            if Collision.trash.colliderect(Collision.new_player_rect):
                Trash.NEWSPAPERS.remove(Collision.trash)
                graphics.Window.SCORE += 1
        
        # If we hit the goal
        for Collision.trash in Trash.GOAL:
            if Collision.trash.colliderect(Collision.new_player_rect):
                gameStates.GameState.HIT_GOAL = True
                

       
