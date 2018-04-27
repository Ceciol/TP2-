import pygame 
import random 

class RedSquare(pygame.sprite.Sprite):
    def __init__(self, w, h, color):
        super(RedSquare, self).__init__()
        self.w, self.h = w, h
        self.color = color
        self.image = pygame.Surface((10,10))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.w - self.rect.width)
        self.rect.y = -30
        self.speedy = random.randrange(6, 10)
        self.speedx = random.randrange(-3, 3)
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
 
# class RedBall(Red):
#     def __init__(self):
#         super().__init__(w, h, color)
#         self.r1 = self.w * 1/60
#         self.r2 = self.w * 1/10 
#         self.dr = 0 
#     
#     def generate(self):
#         super().generate()
#         self.dr = random.choice(self.r1, self.r2)
#     
#     def draw(self, screen):
#         pygame.draw.circle(screen, self.color, (self.x, self.y), self.dr)
# 
# class RedTriangle(Red):
#     def __init__(self, w, h, color):
#         super().__init__(w, h, color)
#         self.r = self.w * 1/30
#     
#     def draw(self, screen):
#         pygame.draw.polygon(screen, self.color, \
#         [(self.x, self.y + self.r),(self.x + self.r, self.y + self.r), \
#         (self.x + 1/2 * self.r, self.y)])
# 
class RedRectangle(pygame.sprite.Sprite):
    def __init__(self, w, h, color):
        super(RedRectangle, self).__init__()
        self.w, self.h = w, h
        self.color = color
        rectW = random.randrange(5, self.w/2)
        rectH = random.randrange(5, self.h/10)
        self.image = pygame.Surface((rectW, rectH))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(-300, -60)
        self.speedx = random.randrange(2, 5)
        self.dir = random.choice((-1,1))
        if self.dir == -1:
            self.rect.x = self.w
        elif self.dir == 1:
            self.rect.x = 0
        
    def update(self, v):
        self.rect.x += self.dir * self.speedx
        self.rect.y += v
        if self.rect.top > self.h:
            self.kill()
        