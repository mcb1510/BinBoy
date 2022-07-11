import pygame
from maps import Maps

class Trash:
    TRASH = []
    TRASH1 = []
    TRASH_SIZE = 50

    def createTrash():
        for row_index,row in enumerate(Maps.LEVEL_1):
            for col_index, col in enumerate(row):
                x = col_index * Trash.TRASH_SIZE
                y = row_index * Trash.TRASH_SIZE
                if col == "T":
                    trash = pygame.Rect((x,y,50,50))
                    #print("Hello",trash[0],trash[1])
                    Trash.TRASH.append(trash)
    
    def createTrash1():
        for row_index,row in enumerate(Maps.LEVEL_1):
            for col_index, col in enumerate(row):
                x = col_index * Trash.TRASH_SIZE
                y = row_index * Trash.TRASH_SIZE
                if col == "C":
                    trash = pygame.Rect((x,y,50,50))
                    #print("Hello",trash[0],trash[1])
                    Trash.TRASH1.append(trash)