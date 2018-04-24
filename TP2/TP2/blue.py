import pygame 
import random 

class Blue(pygame.sprite.Sprite):
    def __init__(self, w, h, color):
        super().__init__()
        self.w = w
        self.h = h
        self.x = 0 
        self.y = 0 
        self.generate()
        self.color = color

    def generate(self):
        self.x = random.randint(0, self.w)
        self.y = random.randint(0, self.h)
        
    def move(self, v):
        self.y += v
        
class BlueSquare(Blue):
    def __init__(self):
        self.r = self.w * 1/60
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.r, self.r))

class BlueBall(Blue):
    def __init__(self):
        self.r1 = self.w * 1/60
        self.r2 = self.w * 1/10 
        self.dr = 0 
    
    def generate(self):
        super().generate()
        self.dr = random.choice(self.r1, self.r2)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.dr)

class BlueTriangle(Blue):
    def __init__(self):
        self.r = self.w * 1/30
    
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, \
        [(self.x, self.y + self.r),(self.x + self.r, self.y + self.r), \
        (self.x + 1/2 * self.r, self.y)])

class BlueRectangle(Blue):
    def __init__(self):
        self.width = self.w * 1/10
        self.height = self.h * 1/20
    
    def draw(self, screen):
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))