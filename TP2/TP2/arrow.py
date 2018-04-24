import pygame


class Arrow(pygame.sprite.Sprite):
    def __init__(self, w, h, color):
        super(Arrow, self).__init__()
        self.w = w
        self.h = h
        self.image = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load('image/arrow.png').convert_alpha(),
            (30, 30)), 0)
        self.rect = self.image.get_rect()
        self.rect.center = (self.w / 2, self.h * 4/5)
        self.color = color
        self.speedx = 0
    
    def update(self, keysDown):
        self.speedx = 0
        if keysDown(pygame.K_LEFT):
            self.speedx = -8
        if keysDown(pygame.K_RIGHT):
            self.speedx = 8
        self.rect.centerx += self.speedx
    
    # this function moves the arrow according to action applied
    def moveEffect(self):
        pass
    
    # def mouseMove(self, newX):
    #     self.cx = newX
    # 
    # def keyMove(self, dt, keysDown):
    #     if keysDown(pygame.K_LEFT):
    #         self.cx -= 5
    #     
    #     if keysDown(pygame.K_RIGHT):
    #         self.cx += 5
    

        
    
