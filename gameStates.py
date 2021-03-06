import platform
import graphics
import movement
from platforms import Platforms
from trash import Trash
import pygame
import sys
import menu
import maps

screen = pygame.display.set_mode((graphics.Window.WIDTH,graphics.Window.HEIGHT))

class GameState():
    HIT_GOAL = False
    CREATE = 0
    GOAL = 1230 #graphics.Window.WIDTH - (graphics.Window.WIDTH/30) * 2
    END_OF_LEVEL = 0
    LEVEL_START = 0
    LEVEL_2_DONE = False  #this variable tells us how far the level will scroll and can be changed.
                      #Zero means it will now scroll

    def __init__(self):
        self.state = "main_menu"

    # Run the main Menu
    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.blit(menu.background,(0,0))
        if menu.start_button.draw(screen):
            print("START")
            self.state = "first_message"
        if menu.exit_button.draw(screen):
            print("EXIT")
            pygame.quit()
            sys.exit()
        
        pygame.display.update()
    
    # Run the first Message
    def first_message(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.blit(menu.first_message,(0,0))
        if menu.continue_button.draw(screen):
            print("Continue")
            self.state = "second_message"
        
        pygame.display.update()
    
    # Run the seccond Message
    def second_message(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.blit(menu.second_message,(0,0))
        if menu.continue_button.draw(screen):
            
            print("Continue")
            self.state = "third_message"
     
        pygame.display.update()
    
    # Run the third Message
    def third_message(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(menu.third_message,(0,0))
        if menu.letsgo_button.draw(screen):
            print("letsgO")
            self.state = "level_1"
            
     
        pygame.display.update()

    def fourth_message(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(menu.fourth_message,(0,0))
        if menu.tips_button.draw(screen):
            print("4th")
            self.state = "level_2"
            
     
        pygame.display.update()
    
    
    # Run level 1
    def level_1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        GameState.END_OF_LEVEL = graphics.Window.WIDTH
        
        # We create everything for level 1
        if (len(Platforms.PLATFORMS) == 0):
            Platforms.createPlatforme()
        if (len(Trash.BANANAS) == 0 and len(Trash.BOTTLES) == 0 and len(Trash.NEWSPAPERS) == 0 
        and len(Trash.PLASTICS) == 0 and GameState.CREATE == 0):
            Trash.createBanana()
            Trash.createBottle()
            Trash.createNewspaper()
            Trash.createPlastic()
            Trash.createGoal()
            GameState.CREATE = 1
      
        graphics.Window.draw_level_1(graphics.Window, movement.Screen.SCROLL_INDEX)
        movement.Chara.movement(movement.Chara, graphics.Binboy.BINBOY_POS)
        movement.Screen.scroll(movement.Screen, graphics.Binboy.BINBOY_POS)
        
        # If we get to the goal we clear everything and give binboy a start position for mext
        if (GameState.HIT_GOAL == True):
        # if (graphics.Binboy.BINBOY_POS.x >= GameState.GOAL):

             Platforms.PLATFORMS.clear()
             Trash.BANANAS.clear()
             Trash.BOTTLES.clear()
             Trash.NEWSPAPERS.clear()
             Trash.PLASTICS.clear()
             Trash.GOAL.clear()
             GameState.CREATE = 0
             GameState.BONUS = True
             graphics.Binboy.BINBOY_POS.x = 0
             graphics.Binboy.BINBOY_POS.y = 650
             movement.Screen.SCROLL_INDEX = 0
             #graphics.Window.SCORE = 0
             self.state = "bonus_level"
             GameState.HIT_GOAL = False

        pygame.display.update()

    
    
    # Run level 2
    def level_2(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        GameState.END_OF_LEVEL = graphics.Window.WIDTH
        GameState.CREATE = 0
        maps.Maps.LEVEL_1 = maps.Maps.LEVEL_2

        if (len(Platforms.PLATFORMS) == 0):
            Platforms.createPlatforme()
        #if len(Trash.BANANAS) == 0 and GameState.CREATE == 0:
        if (len(Trash.BANANAS) == 0 and len(Trash.BOTTLES) == 0 and len(Trash.NEWSPAPERS) == 0 
        and len(Trash.PLASTICS) == 0 and GameState.CREATE == 0):
            Trash.createBanana()
            Trash.createBottle()
            Trash.createNewspaper()
            Trash.createPlastic()
            Trash.createGoal()
            GameState.CREATE = 1
      
        graphics.Window.draw_level_2(graphics.Window, movement.Screen.SCROLL_INDEX)
        movement.Chara.movement(movement.Chara, graphics.Binboy.BINBOY_POS)
        movement.Screen.scroll(movement.Screen, graphics.Binboy.BINBOY_POS)

        if (GameState.HIT_GOAL == True):
            GameState.LEVEL_2_DONE = True
            Platforms.PLATFORMS.clear()
            Trash.BANANAS.clear()
            Trash.BOTTLES.clear()
            Trash.NEWSPAPERS.clear()
            Trash.PLASTICS.clear()
            Trash.GOAL.clear()
            #GameState.CREATE = 0
            movement.Screen.SCROLL_INDEX = 0
            self.state = "bonus_level"

        pygame.display.update()

      
     # Run bonus level   
    def bonus_level(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GameState.LEVEL_2_DONE == False:
                    self.state = "fourth_message" 
                elif GameState.LEVEL_2_DONE == True:    
                    self.state = "first_message"

        graphics.Window.draw_bonus_level(graphics.Window)
        movement.Selection.hover()

    
    # Manage what is happening when is the different states are called
    def state_manager(self):
        if self.state == "main_menu":
            self.main_menu()
        if self.state == "level_1":
            self.level_1()
        if self.state == "level_2":
            self.level_2()
        if self.state == "bonus_level":
            self.bonus_level()
        if self.state == "first_message":
            self.first_message()
        if self.state == "second_message":
            self.second_message()
        if self.state == "third_message":
            self.third_message()
        if self.state == "fourth_message":
            self.fourth_message()



























   
