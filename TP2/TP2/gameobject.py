import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, radius, color, lst):
        super().__init__()
        self.x, self.y, self.image, self.radius = x, y, image, radius
        self.baseImage = image.copy
        w, h = image.get_size()
        self.color = color 
        self.lst = lst
    
    def scroll(self, dy):
        for l in self.lst:
            l.y += dy
    
    def deletePast(self):
        if self.y > self.h + 10:
            
            
    
    # all objects within -10 to self.h + 10 are drawn
    def draw(self, screen):
        pass
