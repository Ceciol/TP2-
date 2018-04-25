import pygame 
import random 

# class Red(pygame.sprite.Sprite):
#     def __init__(self, w, h, color):
#         super(Red, self).__init__()
#         self.w = w
#         self.h = h
#         self.x = 0 
#         self.y = 0 
#         self.generate()
#         self.color = color
#         
# 
#     def generate(self):
#         self.x = random.randint(0, self.w)
#         self.y = random.randint(0, self.h)
#         
#     def move(self, v):
#         self.y += v
        
class RedSquare(pygame.sprite.Sprite):
    def __init__(self, w, h, color):
        super(RedSquare, self).__init__()
        self.w, self.h = w, h
        self.color = color
        self.image = pygame.Surface((20,20))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.w - self.rect.width)
        self.rect.y = -30
        self.speedy = random.randrange(6, 10)
        self.speedx = random.randrange(-3, 3)
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # if self.rect.top > self.h + 10:
        #     self.rect.x = random.randrange(self.w - self.rect.width)
        #     self.rect.y = random.randrange(-100, -40)
        #     self.speedy = random.randrange(1, 8)
 
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
# class RedRectangle(Red):
#     def __init__(self, w, h, color):
#         super().__init__(w, h, color)
#         self.width = self.w * 1/10
#         self.height = self.h * 1/20
#     
#     def draw(self, screen):
#         pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
#         