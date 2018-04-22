import pygame
import random




class Map(pygame.sprite.Sprite):
    def __init__(self, w, h, color):
        super().__init__()
        self.w = w
        self.h = h
        self.color = color
        self.levelspeed = 3
        self.s = self.w / 50
        self.clock = 0 
        self.mapInit()
        self.map = ["ssssssssssssssssssssss      ssssssssssssssssssssss",
                    "ssssssssssssssssssssss      ssssssssssssssssssssss",
                    "ssssssssssssssssssssss      ssssssssssssssssssssss",
                    "ssssssssssssssssssssss      ssssssssssssssssssssss",
                    "ssssssssssssssssssssss      ssssssssssssssssssssss",
                    "ssssssssssssssssssssss      ssssssssssssssssssssss",
                    "ssssssssssssssssssssss      ssssssssssssssssssssss",
                    "ssssssssssssssssssssss      ssssssssssssssssssssss",
                    "ssssssssssssssssssssss      ssssssssssssssssssssss",
                    "ssssssssssssssssssssss      ssssssssssssssssssssss"]
        self.blocks = [ ]
        self.aBlocks = [ ]
                   
    def createMap(self, dt, percentage):
        self.clock += dt 
        if self.clock % percentage == 0:
            route = random.choice([self.p1, self.p2, self.p3, self.p4, self.p5,\
            self.p6, self.p7, self.p8, self.p9, self.p10, self.p11, self.p12, \
            self.p13, self.p14, self.p15, self.p16, self.p17])
            self.map.append(route)
            super().__init__()
    
    def mapMove(self, dt):
        pass

    def draw(self, screen):
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == "s":
                    pygame.draw.rect(screen, self.color, (col * self.s, row * self.s, self.s, self.s))
    
    def mapInit(self):
        # maps
        # a total of 50 spaces for a row
        
        self.p1 = ["sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss",
                   "sssssss                                   sssssss"]
        
        self.p2 = ["sssssssssssssssssss  sssssssssssssssssssssssssss",
                    "sssssssssssssssssss  sssssssssssssssssssssssssss",
                    "sssssssssssssssssss   ssssssssssssssssssssssssss",
                    "ssssssssssssssssssss   sssssssssssssssssssssssss",
                    "ssssssssssssssssssss   sssssssssssssssssssssssss",
                    "sssssssssssssssssss  sssssssssssssssssssssssssss",
                    "ssssssssssssssssss   sssssssssssssssssssssssssss",
                    "sssssssssssssssss   ssssssssssssssssssssssssssss",
                    "ssssssssssssssssss   sssssssssssssssssssssssssss",
                    "sssssssssssssssssss   ssssssssssssssssssssssssss",
                    "ssssssssssssssssssss   sssssssssssssssssssssssss",
                    "sssssssssssssssssssss   ssssssssssssssssssssssss",
                    "ssssssssssssssssssss   sssssssssssssssssssssssss",
                    "sssssssssssssssssss  sssssssssssssssssssssssssss",
                    "ssssssssssssssssss   ssssssssssssssss sssssssssss"]
                    
        self.p3 = ["ssssssssssssssssssss     sssssssssssssssssssssssss",
                   "ssssssssssssssssssss     sssssssssssssssssssssssss",
                   "ssssssssssssssssssss     sssssssssssssssssssssssss",
                   "ssssssssssssssssssss     sssssssssssssssssssssssss",
                   "ssssssssssssssssssss     sssssssssssssssssssssssss",
                   "ssssssssssssssssssss     sssssssssssssssssssssssss",
                   "ssssssssssssssssssss     sssssssssssssssssssssssss",
                   "ssssssssssssssssssss     sssssssssssssssssssssssss",
                   "ssssssssssssssssssss     sssssssssssssssssssssssss",
                   "ssssssssssssssssssss     sssssssssssssssssssssssss",
                   "ssssssssssssssssssss     sssssssssssssssssssssssss",
                   "ssssssssssssssssssss     sssssssssssssssssssssssss",]
        
        self.p4 = ["ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss"]
        
        self.p5 = ["sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssss                sssssssssssssssssss",
                   "sssssssssssssss                  sssssssssssssssss",
                   "sssssssssssssss                    sssssssssssssss",
                   "sssssssssssssss                     ssssssssssssss",
                   "sssssssssssssss                     ssssssssssssss",
                   "ssssssssssssssss                    ssssssssssssss",
                   "sssssssssssssssss                   ssssssssssssss",
                   "sssssssssssssssssss                 ssssssssssssss",
                   "sssssssssssssssssssss               ssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss"]
        
        self.p6 = ["ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss      ssssssssssss      sssssssssssss",
                   "sssssssssssss      ssssssssssss      sssssssssssss",
                   "sssssssssssss      ssssssssssss      sssssssssssss",
                   "sssssssssssss      ssssssssssss      sssssssssssss",
                   "sssssssssssss      ssssssssssss      sssssssssssss",
                   "sssssssssssss      ssssssssssss      sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss"]
                   
        self.p7 = ["ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss          ssss          sssssssssssss",
                   "sssssssssssss          ssss          sssssssssssss",
                   "sssssssssssss      sssss  sssss      sssssssssssss",
                   "sssssssssssss      sssss  sssss      sssssssssssss",
                   "sssssssssssss          ssss          sssssssssssss",
                   "sssssssssssss          ssss          sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss"]
        
        self.p8 = ["ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss   ssss    ssss         sssssssssssss",
                   "sssssssssssss   ssss    ssss         sssssssssssss",
                   "sssssssssssss                        sssssssssssss",
                   "sssssssssssss      sssss  sssss      sssssssssssss",
                   "sssssssssssss      sssss  sssss      sssssssssssss",
                   "sssssssssssss    ssss ssss           sssssssssssss",
                   "sssssssssssss    ssss ssss           sssssssssssss",
                   "sssssssssssss                   ssss sssssssssssss",
                   "sssssssssssss                   ssss sssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss"]
        
        self.p9 = ["sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssss        sssssssssssssssssssssss",
                   "sssssssssssssssssss        sssssssssssssssssssssss",
                   "sssssssssssssssssss     ssssssssssssssssssssssssss",
                   "sssssssssssssssssss     ssssssssssssssssssssssssss",
                   "sssssssssssssssssss     ssssssssssssssssssssssssss",
                   "sssssssssssssssssss     ssssssssssssssssssssssssss",
                   "sssssssssssssssssss     ssssssssssssssssssssssssss",
                   "sssssssssssssssssss     ssssssssssssssssssssssssss",
                   "sssssssssssssssssss     ssssssssssssssssssssssssss",
                   "sssssssssssssssssss     ssssssssssssssssssssssssss",
                   "sssssssssssssssssss           ssssssssssssssssssss",
                   "sssssssssssssssssss           ssssssssssssssssssss",
                   "sssssssssssssssssssssssss     ssssssssssssssssssss",
                   "sssssssssssssssssssssssss     ssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss"]
        
        self.p10 = ["sssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss      ssssssssssssssssssssss",
                   "ssssssssssssssssssssss             sssssssssssssss",
                   "ssssssssssssssssssssss             sssssssssssssss",
                   "ssssssssssssssssssssssssssss       sssssssssssssss",
                   "ssssssssssssssssssssssssssss       sssssssssssssss",
                   "ssssssssssssssssssssssssssss       sssssssssssssss",
                   "ssssssssssssssssssssssssssss       sssssssssssssss",
                   "ssssssssssssssssssssssssssss       sssssssssssssss",
                   "ssssssssssssssssssssssssssss       sssssssssssssss",
                   "ssssssssssssssssssssssssssss       sssssssssssssss",
                   "ssssssssssssssss                   sssssssssssssss",
                   "ssssssssssssssss                   sssssssssssssss",
                   "ssssssssssssssss     sssssssssssssssssssssssssssss",
                   "ssssssssssssssss     sssssssssssssssssssssssssssss",
                   "ssssssssssssssss     sssssssssssssssssssssssssssss",
                   "ssssssssssssssss             sssssssssssssssssssss",
                   "ssssssssssssssss             sssssssssssssssssssss",
                   "sssssssssssssssssssssss     ssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss",
                   "sssssssssssssssssssssss    sssssssssssssssssssssss"]
        
        self.p11 = ["ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss",
                   "ss                                             ss"]
        
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
        
        
                   
                   
                   
        
                   
                   


        
