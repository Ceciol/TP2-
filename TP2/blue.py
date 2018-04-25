import pygame 
import random 
vec = pygame.math.Vector2

# partly insquired by code online 
class BlueSquare(pygame.sprite.Sprite):
    def __init__(self, w, h, color):
        super(BlueSquare, self).__init__()
        self.w, self.h = w, h
        self.color = color
        self.image = pygame.Surface((20,20))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.w - self.rect.width)
        self.rect.y = -30
        self.pos = vec(self.rect.x, self.rect.y)
        self.vel = vec(0,5)
        self.acc = vec(0,0)
        self.initialacc = 0.5
        self.friction = -0.12
        self.left = False
        self.right = False
        self.up = False
        self.down = False
    
    def update(self):
        self.acc = vec(0, 0.5)
        if self.right == True:
            self.acc.x = -self.initialacc
        elif self.left == True:
            self.acc.x = self.initialacc
        if self.up == True:
            self.acc.y = -self.initialacc
        elif self.down == True:
            self.acc.y = self.initialacc
            
        self.acc.x += self.vel.x * self.friction
        self.acc.y += self.vel.y * self.friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        