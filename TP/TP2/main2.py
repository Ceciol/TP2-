import pygame
from pygamegame import PygameGame
from arrow import Arrow 
from map import Map
from red import * 
from blue import * 
from powerup import * 
from maplib import * 
import random 
import string


class Main(PygameGame):
    def initColor(self):
        self.lightGrey = (214,214,204)
        self.blue = (99,177,192)
        self.orange = (231,171,95)
        self.red = (212,95,74)
        self.brown = (90,77,71)
        self.grey = (126,140,142)
        self.white = (241,237,218)
    
    # cited from online
    def initImg(self):
        self.bgImg = pygame.image.load('image/bg.png')
        self.setImg = pygame.image.load('image/set.png')
        self.quitImg = pygame.image.load('image/quit.png')
        self.pauseImg = pygame.image.load('image/pause.png')
        
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
    
    def gamePauseBtn(self):
        w = 300 
        h = 100 
        self.backBtn = [150, 100, w, h, self.lightGrey]
    
    def gameOverBtn(self):
        w = 300 
        h = 100 
        self.overBtn = [150, 100, w, h, self.lightGrey]
        
    def btns(self):
        self.mainbuttons()
        self.gameBtn()
        self.gamePauseBtn()
        self.gameOverBtn()
    
#########################
### Main Framework ######
#########################

    def init(self):
        self.initColor()
        self.initImg()
        self.mode = "main"
        self.modeLst = ["main","settings","game","gamePause","gameOver","instructions","creation","multiplayer","?"]
        self.btns()
        arrow = Arrow(self.width, self.height)
        self.arrowGroup = pygame.sprite.GroupSingle(arrow)
        self.mapGroup = pygame.sprite.Group()
        self.clock = 0 
        route = random.choice([p1, p2, p3])
        for row in range(len(route)):
            for col in range(len(route[row])):
                if route[row][col] == "s":
                    map = Map(col * 30, -row * 30, self.red)
                    self.mapGroup.add(map)
        self.tempGroup = pygame.sprite.Group()
        self.control = 1
        self.percentage = 5
        self.redGroup = pygame.sprite.Group()
        # for i in range(8):
        #     red = RedSquare(self.width, self.height, self.red)
        #     self.redGroup.add(red)
        self.blueGroup = pygame.sprite.Group()
        self.build = ""
        self.hit = {}
        self.h = {}
        self.powerupGroup = pygame.sprite.Group()
        self.v = 6
        self.score = 0
        self.pause = False
        self.over = False
        self.newType = [ ]
        self.tempType = [ ]
        self.redRectGroup = pygame.sprite.Group()
    
    
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
        self.gameMouseReleased(x, y)
        self.gamePauseMouseReleased(x,y)
        self.gameOverMouseReleased(x,y)

    
    def gameMouseReleased(self, x, y):
        if self.mode == "game":
            if self.within(self.stopBtn[0], self.stopBtn[1], self.stopBtn[2],\
                self.stopBtn[3],x,y):
                self.pause = True
                self.mode = "gamePause"
    
    def gamePauseMouseReleased(self, x, y):
        if self.mode == "gamePause":
            if self.within(self.backBtn[0], self.backBtn[1], self.backBtn[2],\
                self.backBtn[3],x,y):
                self.pause = False
                self.mode = "game"
        
    def gameOverMouseReleased(self, x, y):
        if self.mode == "gameOver":
            if self.within(self.overBtn[0], self.overBtn[1], self.overBtn[2],\
                self.overBtn[3],x,y):
                self.over = True
                self.mode = "game"
    
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
            if self.over == True:
                self.init()
                self.over = False
            if self.pause == False:
                self.clock += dt
                if self.clock % 10 == 0:
                    self.score += 1
                for arrow in self.arrowGroup:
                    if arrow.c == 0 and len(self.hit) != 0:
                        self.mode = "gameOver"
                    elif arrow.c == 1 and len(self.h) != 0:
                        self.mode = "gameOver"
                self.redTimerFired()
                self.mapTimerFired()
                self.arrowTimerFired()
                #self.blueTimerFired(dt)
                self.powerUpTimerFired()
                if self.clock % 2000 == 0:
                    self.v += 1
    
    def redTimerFired(self):
        for arrow in self.arrowGroup:
            if arrow.c == 0:
                # collision detect for red objects 
                self.hit.update(pygame.sprite.groupcollide(self.redGroup, self.arrowGroup, False, False))
                self.hit.update(pygame.sprite.groupcollide(self.redRectGroup, self.arrowGroup, False, False))
                
        if len(self.redGroup) < 3:
            r = RedSquare(self.width, self.height, self.red)
            b = pygame.sprite.spritecollideany(r, self.mapGroup)
            temp = pygame.sprite.spritecollideany(r, self.tempGroup)
            if b == None and temp == None:
                self.redGroup.add(r)
        for red in self.redGroup:
            if red.rect.y > self.height + 20:
                red.kill()
            coll = pygame.sprite.spritecollideany(red, self.mapGroup)
            col = pygame.sprite.spritecollideany(red, self.tempGroup)
            if coll != None:
                if red.rect.x > coll.rect.x: red.speedx = abs(red.speedx)
                if red.rect.bottom > coll.rect.top: red.speedy = abs(red.speedy)
                if red.rect.x < coll.rect.x: red.speedx = -abs(red.speedx)
                if red.rect.bottom < coll.rect.top + 5: 
                    red.speedy = -abs(red.speedy)
            if col != None:
                if red.rect.left > col.rect.left: red.speedx = abs(red.speedx)
                if red.rect.bottom > col.rect.top: red.speedy = abs(red.speedy)
                if red.rect.left < col.rect.left: red.speedx = -abs(red.speedx)
                if red.rect.bottom < col.rect.top + 5: red.speedy = -abs(red.speedy)
        self.redGroup.update()
        self.redRectGroup.update(self.v)
    
    def blueTimerFired(self, dt):
        for arrow in self.arrowGroup:
            if arrow.c == 1:
                # collision detect for blue object 
                self.h.update(pygame.sprite.groupcollide(self.blueGroup, self.arrowGroup, False, False))
        if self.clock % 1 == 0:
            num = random.randint(1,3)
            for i in range(num):
                b = BlueSquare(self.width, self.height, self.blue)
                cm = pygame.sprite.spritecollideany(b, self.mapGroup)
                ctemp = pygame.sprite.spritecollideany(b, self.tempGroup)
                if cm == None and ctemp == None:
                    self.blueGroup.add(b)
            for blue in self.blueGroup:
                if blue.rect.y > self.height + 20:
                    blue.kill()
                collide = pygame.sprite.spritecollideany(blue, self.arrowGroup)
                if collide != None:
                    if blue.rect.x > collide.rect.x: 
                        blue.right = True
                    if blue.rect.bottom > collide.rect.top:
                        blue.up = True
                    if blue.rect.x < collide.rect.x:
                        blue.left = True 
                    if blue.rect.bottom < collide.rect.top + 5:
                        blue.down = True
        self.blueGroup.update()
        
    def powerUpTimerFired(self):
        self.powerupGroup.update(self.v)
        # collision detect for powerups 
        hits = pygame.sprite.groupcollide(self.powerupGroup, self.arrowGroup, True, False)
        for hit in hits:
            if hit.type == "slow":
                for map in self.mapGroup:
                    map.slowspeed()
                for map in self.tempGroup:
                    map.slowspeed()
                for powerup in self.powerupGroup:
                    powerup.slowspeed()
            if hit.type == "color":
                for arrow in self.arrowGroup:
                    arrow.changeColor()
            if hit.type == "goldCoin":
                self.score += 10
    
    def arrowTimerFired(self):
        self.arrowGroup.update(self.isKeyPressed)
        
    def mapTimerFired(self):
        self.mapGroup.update(self.v)
        self.tempGroup.update(self.v)
        if len(self.mapGroup) != 0:
            for arrow in self.arrowGroup:
                if arrow.c == 0:
                    # collision detect for red object 
                    self.hit.update(pygame.sprite.groupcollide(self.mapGroup, self.arrowGroup, False, False))
            count = 0 
            for map in self.mapGroup:
                if map.rect.y > 0: 
                    count += 1
                if map.rect.y > self.height + 30: 
                    self.mapGroup.remove(map)
                if count == len(self.mapGroup): 
                    self.build = "temp"
            
        if len(self.tempGroup) != 0:
            for arrow in self.arrowGroup:
                if arrow.c == 0:
                    # collision detect for red object 
                    self.hit.update(pygame.sprite.groupcollide(self.tempGroup, self.arrowGroup, False, False))
            count1 = 0 
            for m in self.tempGroup:
                if m.rect.y > 0: count1 += 1
                if m.rect.y > self.height + 30: self.tempGroup.remove(m)
                if count1 == len(self.tempGroup): 
                    self.build = "new"

        
        if self.build == "new" and len(self.mapGroup) == 0:
            self.newType = [ ] 
            route1 = random.choice([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]) +\
                random.choice([[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]])
            for row in range(len(route1)):
                for col in range(len(route1[row])):
                    if route1[row][col] == "s":
                        map = Map(col * 30, -row * 30, red)
                        self.mapGroup.add(map)
                    elif route1[row][col] in string.digits:
                        self.newType.append(route1[row][col])
            for i in range(8):
                p = PowerUp(self.width, self.height)
                mapC = pygame.sprite.spritecollideany(p, self.mapGroup)
                tempC = pygame.sprite.spritecollideany(p, self.tempGroup)
                if mapC == None and tempC == None:
                    self.powerupGroup.add(p)
            for new in self.newType:
                print(new)
                if new == "1":
                    for j in range(random.randint(1,3)):
                        rec = RedRectangle(self.width, self.height, red)
                        self.redRectGroup.add(rec)
                
            
        
        if self.build == "temp" and len(self.tempGroup) == 0:
            route2 = random.choice([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]) + \
                random.choice([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14])
            self.tempType = [ ] 
            for row in range(len(route2)):
                for col in range(len(route2[row])):
                    if route2[row][col] == "s":
                        map = Map(col * 30, -row * 30, self.red)
                        self.tempGroup.add(map)
                    elif route2[row][col] in string.digits:
                        self.tempType.append(route2[row][col])
            for i in range(8):
                p = PowerUp(self.width, self.height)
                mapC = pygame.sprite.spritecollideany(p, self.mapGroup)
                tempC = pygame.sprite.spritecollideany(p, self.tempGroup)
                if mapC == None and tempC == None:
                    self.powerupGroup.add(p)
            for new in self.newType:
                print(new)
                if new == "1":
                    for j in range(random.randint(1,3)):
                        rec = RedRectangle(self.width, self.height, red)
                        self.redRectGroup.add(rec)

            # while len(self.mapGroup) < 200:
            #     route = random.choice([self.p1, self.p2, self.p3]) + random.choice([self.p1, self.p2, self.p3])
            #     for row in range(len(route)):
            #         for col in range(len(route[row])):
            #             if route[row][col] == "s":
            #                 map = Map(col * 30, -row * 30, self.red)
            #                 self.mapGroup = pygame.sprite.Group.add(map)
                    
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
        pygame.draw.rect(screen, self.stopBtn[4], self.stopBtn[:4])
    
    def drawBackBtn(self,screen):
        pygame.draw.rect(screen, self.backBtn[4], self.backBtn[:4])
    
    def drawOverBtn(self,screen):
        pygame.draw.rect(screen, self.overBtn[4], self.overBtn[:4])

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
            screen.fill(self.white)
            self.arrowGroup.draw(screen)
            self.redGroup.draw(screen)
            self.blueGroup.draw(screen)
            self.powerupGroup.draw(screen)
            self.redRectGroup.draw(screen)
            if len(self.mapGroup) != 0:
                self.mapGroup.draw(screen)
            if len(self.tempGroup) != 0:
                self.tempGroup.draw(screen)
            self.displayText(screen, 30, str(self.score), (20,20))
            self.drawStopBtn(screen)
            

    
    def redrawGamePause(self,screen):
        if self.mode == "gamePause":
            screen.fill(self.white)
            self.drawBackBtn(screen)
    
    def redrawGameOver(self,screen):
        if self.mode == "gameOver":
            screen.fill(self.white)
            self.drawOverBtn(screen)
    
    def redrawInstructions(self,screen):
        if self.mode == "instructions":
            pass
        
    def redrawMultiplayer(self,screen):
        if self.mode == "multiplayer":
            pass
    
    def redrawCreation(self, screen):
        if self.mode == "creation":
            pass
            
    def redrawQuestion(self,screen):
        if self.mode == "?":
            pass
        
    def redrawAll(self, screen):
        self.redrawMain(screen)
        self.redrawSettings(screen)
        self.redrawGame(screen)
        self.redrawGamePause(screen)
        self.redrawGameOver(screen)
        self.redrawInstructions(screen)
        self.redrawMultiplayer(screen)
        self.redrawCreation(screen)
        self.redrawQuestion(screen)


Main(600, 600).run()
