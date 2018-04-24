import pygame 

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, w, h, color):
        super().__init__()
        self.w = w
        self.h = h
        self.x = 0 
        self.y = 0 
        self.width = self.w * 1/30
        self.height = self.w * 1/40
        self.color = color
    
    def generate(self):
        self.x = random.randint(0, self.w)
        self.y = random.randint(0, self.h)
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.w, self.h))