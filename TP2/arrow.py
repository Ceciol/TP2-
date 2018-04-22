import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, w, h, color):
        super().__init__()
        self.w = w
        self.h = h
        self.cx = self.w / 2
        self.cy = self.h * 4/5
        self.sr = 13
        self.cr = self.sr / 2
        self.color = color
    
    
    def draw(self,screen):
        locLst = [ [self.cx - self.sr, self.cy + self.sr], 
                  [self.cx + self.sr, self.cy + self.sr], 
                  [self.cx, self.cy - self.sr] ]
            
        pygame.draw.polygon(screen, self.color, locLst)
        pygame.draw.circle(screen, self.color, [int(self.cx),int(self.cy + 2 * self.sr)], int(self.cr))
    
    # this function moves the arrow according to action applied
    def moveEffect(self):
        pass
    
    def mouseMove(self, newX):
        self.cx = newX
    
    def keyMove(self, dt, keysDown):
        if keysDown(pygame.K_LEFT):
            self.cx -= 5
        
        if keysDown(pygame.K_RIGHT):
            self.cx += 5
        
        
    
