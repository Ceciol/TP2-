import pygame
from pygamegame import PygameGame


class Main(PygameGame):
    def initColor(self):
        self.grey = (184,184,173)
        self.purple = (129,132,179)
        self.orange = (231,159,114)
        self.lightGrey = (214,214,204)
    
    def initImg(self):
        self.bgImg = pygame.image.load('image/bg.png')
        self.setImg = pygame.image.load('image/set.png')
        self.quitImg = pygame.image.load('image/quit.png')
        

#############################
#all button
#############################
    def mainbuttons(self):
        r = 30
        w2 = 300
        h2 = 50
        self.settingBtn = [520,20,r,self.lightGrey]
        self.quitBtn = [520,530,r,self.lightGrey]
        self.mainBtn1=[70,200,w2,h2,self.lightGrey]
        self.mainBtn2=[70,300,w2,h2,self.lightGrey]
        self.mainBtn3=[70,400,w2,h2,self.lightGrey]
    
    def gameBtn(self):
        w = 70
        h = 50
        self.stopBtn = [500,40,w,h,self.lightGrey]
    
    def btns(self):
        self.mainbuttons()
        self.gameBtn()
    
#########################
### Main Framework ######
#########################

    def init(self):
        self.initColor()
        self.initImg()
        self.mode = "main"
        self.modeLst = ["main","settings","game","gamePause","gameOver","instructions"]
        self.btns()
        
    
    #### MousePressed ####
    def mousePressed(self,x,y):
        pass
        
#### MouseReleased ####
    def mousePressed(self,x,y):
        pass
        
#### MouseMotion ####
    # cited from my hack112 project
    def within(self,left,down,width,height,x,y):
        return left < x < left+width and down < y < down +height
        
    def mouseMotionMain(self,x,y):
        if self.mode == "main":
            for btn in [self.mainBtn1,self.mainBtn2,self.mainBtn3]:
                if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                    btn[4]=self.grey
                else:
                    btn[4]=self.lightGrey
            if self.within(self.settingBtn[0]+27,self.settingBtn[1]+27,self.settingBtn[2],self.settingBtn[2],x,y):
                self.settingBtn[3]=self.grey
            else:
                self.settingBtn[3]=self.lightGrey
            if self.within(self.quitBtn[0]+25,self.quitBtn[1]+25,self.quitBtn[2],self.quitBtn[2],x,y):
                self.quitBtn[3]=self.grey
            else:
                self.quitBtn[3]=self.lightGrey
        
    def mouseMotion(self, x, y):
        self.mouseMotionMain(x,y)
        
#### timerFried ####
    def timerFired(self, dt):
        pass
        
###########################
#draw
###########################
    def drawSettingBtn(self,screen):
        pygame.draw.circle(screen,self.settingBtn[3],(self.settingBtn[0]+27,self.settingBtn[1]+27),self.settingBtn[2])
        screen.blit(self.setImg, (self.settingBtn[0],self.settingBtn[1]))
        
    def drawQuitBtn(self,screen):
        pygame.draw.circle(screen,self.quitBtn[3],(self.quitBtn[0]+25,self.quitBtn[1]+25),self.quitBtn[2])
        screen.blit(self.quitImg, (self.quitBtn[0],self.quitBtn[1]))
    
    def drawStopBtn(self,screen):
        pass

    # cited from pygame website
    def AAfilledRoundedRect(surface,rect,color,radius=0.4):
    
        rect         = Rect(rect)
        color        = Color(*color)
        alpha        = color.a
        color.a      = 0
        pos          = rect.topleft
        rect.topleft = 0,0
        rectangle    = Surface(rect.size,SRCALPHA)
    
        circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
        draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
        circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)
    
        radius              = rectangle.blit(circle,(0,0))
        radius.bottomright  = rect.bottomright
        rectangle.blit(circle,radius)
        radius.topright     = rect.topright
        rectangle.blit(circle,radius)
        radius.bottomleft   = rect.bottomleft
        rectangle.blit(circle,radius)
    
        rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
        rectangle.fill((0,0,0),rect.inflate(0,-radius.h))
    
        rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
        rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)
    
        return surface.blit(rectangle,pos)
        
    


############### redraw ####
    def redrawMain(self,screen):
        if self.mode == "main":
            screen.blit(self.bgImg,(0,0))
            self.drawSettingBtn(screen)
            self.drawQuitBtn(screen)
            pygame.draw.rect(screen,self.mainBtn1[4],self.mainBtn1[:4])    
            pygame.draw.rect(screen,self.mainBtn2[4],self.mainBtn2[:4])  
            pygame.draw.rect(screen,self.mainBtn3[4],self.mainBtn3[:4])  
    
    def redrawSettings(self,screen):
        if self.mode == "settings":
            screen.blit(self.bgImg,(0,0))
    
    def redrawGame(self,screen):
        if self.mode == "game":
            pass
    
    def redrawGamePause(self,screen):
        if self.mode == "gamePause":
            pass
    
    def redrawGameOver(self,screen):
        if self.mode == "gameOver":
            pass
    
    def redrawInstructions(self,screen):
        if self.mode == "instructions":
            pass
        
    def redrawAll(self, screen):
        self.redrawMain(screen)
        self.redrawSettings(screen)
        self.redrawGame(screen)
        self.redrawGamePause(screen)
        self.redrawGameOver(screen)
        self.redrawInstructions(screen)

Main(800, 500).run()
    
