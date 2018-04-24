import pygame
import random

white = (241,237,218)
# cited from course website
import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

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
    def __init__(self, w, h, color):
        super(Map, self).__init__()
        self.w = w
        self.h = h
        self.color = color
        self.image = pygame.Surface((600, 1200))
        self.image.fill = white
        self.rect = self.image.get_rect()
        self.levelspeed = 3
        self.s = self.w / 20
        self.r = self.h / self.s 
        self.clock = 0 
        self.temp = [ ]
        self.new = [ ] 
        self.empty = [ ]
        self.mapInit()
        self.newB = [ ]
        self.tempB = [ ]
        self.redLst = [ ] 
        self.mode = "new"
        map = ["ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss"]
        # self.blocks = [ ]
        # for row in range(len(map)):
        #     for col in range(len(map[0])):
        #         if map[row][col] == 's':
        #             self.blocks.append(pygame.Rect(col * self.s, (self.r-row) * self.s, \
        #                 self.s, self.s))
        #self.map = [ ]
                   
    def createMap(self, dt, percentage):
        self.clock += dt 
        if self.mode == "new" and len(self.new) == 0:
            route1 = random.choice([self.p1, self.p2, self.p3]) + random.choice([self.p1, self.p2, self.p3])
            for row in range(len(route1)):
                for col in range(len(route1[row])):
                    if route1[row][col] == "s":
                        self.new.append(pygame.Rect(col * self.s,-row * self.s,\
                        self.s, self.s))
                    if route1[row][col] == " ":
                        self.newB.append(pygame.Rect(col * self.s,-row * self.s,\
                        self.s, self.s))
                        
        if self.mode == "temp" and len(self.temp) == 0:
            route2 = random.choice([self.p1, self.p2, self.p3]) + random.choice([self.p1, self.p2, self.p3])
            for row in range(len(route2)):
                for col in range(len(route2[row])):
                    if route2[row][col] == "s":
                        self.temp.append(pygame.Rect(col * self.s,-row * self.s,\
                        self.s, self.s))
                    if route2[row][col] == " ":
                        self.tempB.append(pygame.Rect(col * self.s,-row * self.s,\
                        self.s, self.s))                
            
        
    def update(self, v):
        count = 0 
        count1 = 0 
        # for block in self.blocks:
        #     block.move_ip(0, v)
        if len(self.temp) != 0:
            for block in self.temp:
                block.move_ip(0, v)
                if block.y > 0: count += 1
                if block.y > (self.h + self.s): self.temp.remove(block)
            if count == len(self.temp): self.mode = "new"
        
        if len(self.new) != 0:
            for block1 in self.new:
                block1.move_ip(0, v)
                if block1.y > 0: count1 += 1
                if block1.y > (self.h + self.s): self.new.remove(block1)
            if count1 == len(self.new): self.mode = "temp"
                

    
    def mapInit(self):
        # maps
        # a total of 20 spaces for a row
        
        self.p1 = ["ssss            ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss            ssss"]
        
        
        self.p2 = [ "sssssssss   ssssssss",
                    "sssssssss   ssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss    ssssssss",
                    "sssssssss    sssssss",
                    "sssssssss    sssssss",
                    "sssssssss    sssssss",
                    "sssssssss   ssssssss",
                    "sssssssss   ssssssss",
                    "ssssssss   sssssssss",
                    "ssssssss   sssssssss",
                    "ssssss     sssssssss",
                    "ssssss     sssssssss",
                    "ssssssss    ssssssss",
                    "ssssssss     sssssss",
                    "ssssssssss     sssss",
                    "ssssssssss      ssss",
                    "sssssssssss      sss",
                    "ssssssssss     sssss",
                    "sssssssss   ssssssss",
                    "ssssssss   sssssssss",
                    "ssssssss   sssssssss",
                    "ssssssss   sssssssss"]
        
                    
        self.p3 = ["sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss"]
        
        
        self.p4 = ["ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss"]
        
        
        self.p5 = ["ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "sss          sssssss",
                   "sss           ssssss",
                   "sss            sssss",
                   "sss             ssss",
                   "sss              sss",
                   "sss              sss",
                   "ssss             sss",
                   "sssss            sss",
                   "ssssss           sss",
                   "sssssss          sss",
                   "ssssssss         sss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss"]
        
        
        self.p6 = ["sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss   ssssss   ssss",
                   "ssss   ssssss   ssss",
                   "ssss   ssssss   ssss",
                   "ssss   ssssss   ssss",
                   "ssss   ssssss   ssss",
                   "ssss   ssssss   ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss"]
        
                   
        self.p7 = ["sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "ssss     ss     ssss",
                   "ssss     ss     ssss",
                   "ssss   ss  ss   ssss",
                   "ssss   ss  ss   ssss",
                   "ssss     ss     ssss",
                   "ssss     ss     ssss",
                   "ssss            ssss",
                   "ssss            ssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss"]
        
        
        self.p8 = ["ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssss            ssss",
                   "ssss  ss        ssss",
                   "ssss  ss ss     ssss",
                   "ssss     ss     ssss",
                   "ssss       ss   ssss",
                   "ssss  ss   ss   ssss",
                   "ssss  ss        ssss",
                   "ssss    ss   ss ssss",
                   "ssss    ss   ss ssss",
                   "ssss            ssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss",
                   "sssssssss   ssssssss"]
        
        
        self.p9 = ["sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss",
                   "sssssss       ssssss",
                   "sssssss       ssssss",
                   "sssssssss     ssssss",
                   "sssssssss     ssssss",
                   "sssssssss     ssssss",
                   "ssssssssss   sssssss",
                   "ssssssssss   sssssss",
                   "ssssssssss   sssssss",
                   "ssssssssss   sssssss",
                   "sssssssss     ssssss",
                   "sssssssss     ssssss",
                   "sssssssss         ss",
                   "sssssssss         ss",
                   "sssssssssssss     ss",
                   "sssssssssssss     ss",
                   "sssssss           ss",
                   "sssssss           ss",
                   "sssssss    sssssssss",
                   "sssssss    sssssssss"]
        
        self.p10 =["ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss",
                   "ssssssss    ssssssss"
                   "ssss        ssssssss",
                   "ssss        ssssssss",
                   "ssss    ssssssssssss",
                   "ssss    ssssssssssss",
                   "ssss    ssssssssssss",
                   "ssss    ssssssssssss",
                   "ssss    ssssssssssss",
                   "ssss    ssssssssssss",
                   "ssss    ssssssssssss",
                   "ssss    ssssssssssss",
                   "ss      ssssssssssss",
                   "ss      ssssssssssss",
                   "ss    ssssssssssssss",
                   "ss    ssssssssssssss",
                   "ssss    ssssssssssss",
                   "ssss    ssssssssssss",
                   "ssssss    ssssssssss",
                   "ssssss    ssssssssss",]
        
        self.p11 = ["ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss",
                    "ss                ss"]
        
        self.p12 = ["ssssssssssssssssssssss     sssssssssssssssssssssss",
                    "ssssssssssssssssssssss     sssssssssssssssssssssss",
                    "sssssssssssssss            sssssssssssssssssssssss",
                    "sssssssssssssss            sssssssssssssssssssssss",
                    "sssssssssssssss      sssssssssssssssssssssssssssss",
                    "sssssssssssssss      sssssssssssssssssssssssssssss",
                    "sssssssssssssss      sssssssssssssssssssssssssssss",
                    "sssssssssssssss      sssssssssssssssssssssssssssss",
                    "sssssssssssssss      sssssssssssssssssssssssssssss",
                    "sssssssssssssss      sssssssssssssssssssssssssssss",
                    "sssssssssssssss                      sssssssssssss",
                    "sssssssssssssss                      sssssssssssss",
                    "ssssssssssssssssssssssssssssssss     sssssssssssss",
                    "ssssssssssssssssssssssssssssssss     sssssssssssss",
                    "ssssssssssssssssssssssssssssssss     sssssssssssss",
                    "ssssssssssssssssssssssssssssssss     sssssssssssss",
                    "ssssssssssssssssssssssssssssssss     sssssssssssss",
                    "sssssssssssssssssssssss              sssssssssssss",
                    "sssssssssssssssssssssss              sssssssssssss",
                    "sssssssssssssssssssssss    sssssssssssssssssssssss",
                    "sssssssssssssssssssssss    sssssssssssssssssssssss",
                    "sssssssssssssssssssssss    sssssssssssssssssssssss",
                    "sssssssssssssssssssssss    sssssssssssssssssssssss"]
                    
        self.p13 = ["sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssss                  sssssssssssssssssssssss",
                   "sssssssss                  sssssssssssssssssssssss",
                   "sssssssss    sssssssssssssssssssssssssssssssssssss",
                   "sssssssss    sssssssssssssssssssssssssssssssssssss",
                   "sssssssss    sssssssssssssssssssssssssssssssssssss",
                   "sssssssss    sssssssssssssssssssssssssssssssssssss",
                   "sssssssss    sssssssssssssssssssssssssssssssssssss",
                   "sssssssss                  sssssssssssssssssssssss",
                   "sssssssss                  sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss"]
                   
        self.p14 = ["ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss"]
        
        self.p15 = ["ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss",
                   "ssssssssssssss                     ssssssssssssss"]
        
        self.p14 = ["ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssss                  ssssssssssssssss",
                   "ssssssssssssssss                  ssssssssssssssss",
                   "ssssssssssssssss                  ssssssssssssssss",
                   "ssssssssssssssss                  ssssssssssssssss",
                   "ssssssssssssssss                  ssssssssssssssss",
                   "ssssssssssssssss                  ssssssssssssssss",
                   "ssssssssssssssss                  ssssssssssssssss",
                   "ssssssssssssssss                  ssssssssssssssss",
                   "ssssssssssssssss                  ssssssssssssssss",
                   "ssssssssssssssss                  ssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss"]
        
        self.p15 = ["sssssssssssssssssss     sssssssssssssssssssssssss",
                    "sssssssssssssssssss     sssssssssssssssssssssssss",
                    "ssssssssssssssssssss    sssssssssssssssssssssssss",
                    "sssssssssssssssssssss   sssssssssssssssssssssssss",
                    "ssssssssssssssssssss   ssssssssssssssssssssssssss",
                    "sssssssssssssssssss    ssssssssssssssssssssssssss",
                    "ssssssssssssssssss      sssssssssssssssssssssssss",
                    "sssssssssssssssss        ssssssssssssssssssssssss",
                    "ssssssssssssssssss      sssssssssssssssssssssssss",
                    "sssssssssssssssssss   sssssssssssssssssssssssssss",
                    "ssssssssssssssssssss   ssssssssssssssssssssssssss",
                    "sssssssssssssssssssss   sssssssssssssssssssssssss",
                    "ssssssssssssssssssss   ssssssssssssssssssssssssss",
                    "ssssssssssssssssssss     ssssssssssssssssssssssss",
                    "sssssssssssssssssssss     sssssssssssssssssssssss"]
                    
        self.p16 = ["sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssssss    sssssssssssssssssssss",
                   "ssssssssssssssssssssssssss    ssssssssssssssssssss",
                   "sssssssssssssssssssssssssss    sssssssssssssssssss",
                   "ssssssssssssssssssssssssss    ssssssssssssssssssss",
                   "sssssssssssssssssssssssss    sssssssssssssssssssss",
                   "ssssssssssssssssssssssss    ssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssss    sssssssssssssssssssssssss",
                   "ssssssssssssssssssssss    ssssssssssssssssssssssss",
                   "ssssssssssssssssssssssss    ssssssssssssssssssssss",
                   "ssssssssssssssssssssssssss    ssssssssssssssssssss",
                   "sssssssssssssssssssssssss    sssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss"]
        
        self.p17 = ["sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssssss    sssssssssssssssssssss",
                   "sssssssssssssssssssssssssss    sssssssssssssssssss",
                   "ssssssssssssssssssssssssssss    ssssssssssssssssss",
                   "sssssssssssssssssssssssss         ssssssssssssssss",
                   "ssssssssssssssssssssssss            ssssssssssssss",
                   "sssssssssssssssssssssss      s       sssssssssssss",
                   "sssssssssssssssssssss       sss      sssssssssssss",
                   "ssssssssssssssssssssss       s      ssssssssssssss",
                   "ssssssssssssssssssssssss          ssssssssssssssss",
                   "ssssssssssssssssssssssssss       sssssssssssssssss",
                   "sssssssssssssssssssssssss      sssssssssssssssssss",
                   "sssssssssssssssssssssss      sssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss"]
        
        
                   
                   
                   
        
                   
                   


        
