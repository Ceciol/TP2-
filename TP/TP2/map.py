import pygame
import random
from settings import * 



# def findBoundary(lst):
#     points = [ ]
#     count = 0 
#     for row in range(len(lst)):
#         a = lst[row].count(" ")
#         for col in range(len(lst[row])):
#             if lst[row][col] == " ": 
#                 points.append((col, col+a, row))
#                 break
#     return points
#             

class Map(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super(Map, self).__init__()
        self.color = color
        self.image = pygame.Surface((30,30))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.slow = False
        self.sv = 3
        self.slow_timer = pygame.time.get_ticks()

    
    def update(self, v):
        if self.slow == False:
            self.rect.y += v 
        if self.sv >= v or pygame.time.get_ticks() - self.slow_timer > poweruptime:
            self.slow = False
            self.sv = 3
            self.slow_timer = pygame.time.get_ticks()
        if self.slow == True and self.sv < v:
                self.sv += 0.001
                self.rect.y += self.sv
        # if self.rect.y > self.w + 20:
        #     self.kill()
    
    def slowspeed(self):
        self.slow_timer = pygame.time.get_ticks()
        self.slow = True

            

        
