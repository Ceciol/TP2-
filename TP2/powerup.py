import pygame 
import random
from settings import * 

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, w, h):
        super(PowerUp, self).__init__()
        self.w = w 
        self.h = h 
        self.type = random.choice(["slow","color","goldCoin"])
        self.image = powerupImg[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.w - self.rect.width)
        self.rect.y = -30
        self.slow_timer = pygame.time.get_ticks()
        self.slow = False
        self.sv = 3 
    
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
        if self.rect.top > self.h:
            self.kill()
        
    def slowspeed(self):
        self.slow_timer = pygame.time.get_ticks()
        self.slow = True