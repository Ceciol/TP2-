import pygame
import random
from settings import * 

white = (241,237,218)

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
        # self.levelspeed = 3
        # self.s = self.w / 20
        # self.r = self.h / self.s 
        # self.clock = 0 
        # self.temp = [ ]
        # self.new = [ ] 
        # self.empty = [ ]
        # self.mapInit()
        # self.newB = [ ]
        # self.tempB = [ ]
        # self.redLst = [ ] 
        # self.mode = "new"
        # map = ["ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss",
        #             "ssssssss    ssssssss"]
        # self.blocks = [ ]
        # for row in range(len(map)):
        #     for col in range(len(map[0])):
        #         if map[row][col] == 's':
        #             self.blocks.append(pygame.Rect(col * self.s, (self.r-row) * self.s, \
        #                 self.s, self.s))
        #self.map = [ ]
                   
    # def createMap(self, dt, percentage):
    #     self.clock += dt 
    #     if self.mode == "new":
    #         route1 = random.choice([self.p1, self.p2, self.p3]) + random.choice([self.p1, self.p2, self.p3])
    #         for row in range(len(route1)):
    #             for col in range(len(route1[row])):
    #                 if route1[row][col] == "s":
    #                     self.new.append(pygame.Rect(col * self.s,-row * self.s,\
    #                     self.s, self.s))
    #                 if route1[row][col] == " ":
    #                     self.newB.append(pygame.Rect(col * self.s,-row * self.s,\
    #                     self.s, self.s))
                        
        # if self.mode == "temp" and len(self.temp) == 0:
        #     route2 = random.choice([self.p1, self.p2, self.p3]) + random.choice([self.p1, self.p2, self.p3])
        #     for row in range(len(route2)):
        #         for col in range(len(route2[row])):
        #             if route2[row][col] == "s":
        #                 self.temp.append(pygame.Rect(col * self.s,-row * self.s,\
        #                 self.s, self.s))
        #             if route2[row][col] == " ":
        #                 self.tempB.append(pygame.Rect(col * self.s,-row * self.s,\
        #                 self.s, self.s))                
            
        
    # def update(self, v):
    #     #count = 0 
    #     count1 = 0 
    #     # for block in self.blocks:
    #     #     block.move_ip(0, v)
    #     # if len(self.temp) != 0:
    #     #     for block in self.temp:
    #     #         block.move_ip(0, v)
    #     #         if block.y > 0: count += 1
    #     #         if block.y > (self.h + self.s): self.temp.remove(block)
    #     #     if count == len(self.temp): self.mode = "new"
    #     
    #     if len(self.new) != 0:
    #         for block1 in self.new:
    #             block1.move_ip(0, v)
    #         #if block1.y > 0: count1 += 1
    #     #     if block1.y > (self.h + self.s): self.new.remove(block1)
    #     # if count1 == len(self.new): self.mode = "temp"
    
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
    
    def slowspeed(self):
        self.slow_timer = pygame.time.get_ticks()
        self.slow = True

            

        
