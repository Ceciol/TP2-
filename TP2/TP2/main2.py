import pygame
from pygamegame import PygameGame
from arrow import Arrow 
from map import Map
from red import RedSquare



class Main(PygameGame):
    def initColor(self):
        self.lightGrey = (214,214,204)
        self.blue = (99,177,192)
        self.orange = (231,171,95)
        self.red = (212,95,74)
        self.brown = (90,77,71)
        self.grey = (126,140,142)
        self.white = (241,237,218)
    
    def initImg(self):
        self.bgImg = pygame.image.load('image/bg.png')
        self.setImg = pygame.image.load('image/set.png')
        self.quitImg = pygame.image.load('image/quit.png')
        
#############################
#helper 
#############################
    def displayText(self,screen, fontSize, txt, loc):
        font = pygame.font.SysFont('Arial',fontSize)
        text = font.render(txt, True, self.white)
        screen.blit(text, loc)
    
    # cited from website
    def checkCollision(self, sprite1, sprite2):
        return pygame.sprite.collide_rect(sprite1, sprite2)
    

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
        arrow = Arrow(self.width, self.height, self.brown)
        self.arrowGroup = pygame.sprite.GroupSingle(arrow)
        map = Map(self.width, self.height, self.red)
        self.mapGroup = pygame.sprite.GroupSingle(map)
        self.control = 1
        self.percentage = 5
        self.redGroup = pygame.sprite.Group()
        for i in range(8):
            red = RedSquare(self.width, self.height, self.red)
            self.redGroup.add(red)
        self.blueGroup = pygame.sprite.Group()
    
    #### MousePressed ####
    def mousePressed(self,x,y):
        self.mousePressedMain(x,y)
    
    def mousePressedMain(self,x,y):
        if self.mode == "main":
            if self.within(self.mainBtn1[0],self.mainBtn1[1],self.mainBtn1[2],\
            self.mainBtn1[3],x,y):
                self.mode = "game"
            if self.within(self.mainBtn2[0],self.mainBtn2[1],self.mainBtn2[2],\
            self.mainBtn2[3],x,y):
                self.mode = "main"
            if self.within(self.mainBtn3[0],self.mainBtn3[1],self.mainBtn3[2],\
            self.mainBtn3[3],x,y):
                self.mode = "instructions"
        
#### MouseReleased ####
    def mouseReleased(self,x,y):
        pass
        
#### MouseMotion ####
    def mouseMotion(self, x, y):
        self.mouseMotionMain(x,y)
        self.mouseMotionGame(x,y)

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
            if self.within(self.settingBtn[0]+27,self.settingBtn[1]+27, \
            self.settingBtn[2],self.settingBtn[2],x,y):
                self.settingBtn[3]=self.grey
            else:
                self.settingBtn[3]=self.lightGrey
            if self.within(self.quitBtn[0]+25,self.quitBtn[1]+25,self.quitBtn[2],self.quitBtn[2],x,y):
                self.quitBtn[3]=self.grey
            else:
                self.quitBtn[3]=self.lightGrey
    
    def mouseMotionGame(self,x,y):
        if self.mode == "game":
            if self.control == 0:
                for arrow in self.arrowGroup:
                    arrow.mouseMove(x)

##### KeyPressed #####
    def keyPressed(self, keyCode, modifier):
        #self.gameKeyPressed(keyCode, modifier)
        pass
    
    #def gameKeyPressed(self, keyCode, modifier):
        

#### KeyReleased #####
    def keyReleased(self, keyCode, modifier):
        pass
        
#### timerFried ####
    def timerFired(self, dt):
        if self.mode == "game":
            self.arrowGroup.update(self.isKeyPressed)
            self.redGroup.update()
            for map in self.mapGroup:
                map.createMap(dt, self.percentage)
            self.mapGroup.update(5)
        #     if self.control == 1:
        #         for arrow in self.arrowGroup:
        #             arrow.keyMove(dt, self.isKeyPressed)
        # #blue = BlueSquare(self.width, self.height, self.blue)
        #     if pygame.sprite.spritecollideany(red, self.mapGroup) == False:
            
        #     #if self.checkCollision(map, blue) == False:
        #         #self.blueGroup.append(blue)
            
        
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
            self.displayText(screen, int(self.mainBtn1[3]* 2/3), "New Game", \
            (self.mainBtn1[0] * 3/2 ,self.mainBtn1[1]))
            self.displayText(screen, int(self.mainBtn2[3]* 2/3), "Adventure", \
            (self.mainBtn2[0] * 3/2 ,self.mainBtn2[1]))
            self.displayText(screen, int(self.mainBtn3[3]* 2/3), "Instruction",\
            (self.mainBtn3[0] * 3/2 ,self.mainBtn3[1]))
            
    
    def redrawSettings(self,screen):
        if self.mode == "settings":
            screen.blit(self.bgImg,(0,0))
    
    def redrawGame(self,screen):
        if self.mode == "game":
            #screen.fill(self.white)
            self.arrowGroup.draw(screen)
            self.redGroup.draw(screen)
            self.mapGroup.draw(screen)
            # for map in self.mapGroup:
            #     map.draw(screen)
            
    
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

Main(600, 600).run()