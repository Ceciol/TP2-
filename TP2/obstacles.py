    import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, image, radius, color):
        super(Obstacle,self).__init__()
        self.x, self.y, self.image, self.radius = x, y, image, radius
        self.baseImage = image.copy
        w, h = image.get_size()
        self.color = color 
