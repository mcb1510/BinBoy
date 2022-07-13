import pygame
import os
import gameStates 
import graphics 
import button
pygame.init()
FPS = 60
clock = pygame.time.Clock()
game_state = gameStates.GameState()
pygame.display.set_caption("BinBoy")

def main():
  
    while True:
        clock.tick(FPS)
        game_state.state_manager()
if __name__ == "__main__":
    main()
