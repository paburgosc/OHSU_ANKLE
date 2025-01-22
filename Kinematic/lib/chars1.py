import pygame, math, random
import vars, funcs,main
from pygame.locals import *

global axis_z
axis_z= None
i = 0
global vel
vel = 1


#Main Player

class player():
    def __init__(self):
        self.sprite = funcs.loadImage('char.png', -1)

        self.xPos = 50
        self.yPos = vars.height/2

        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.speed = 7

        self.reloadTime = 5
        self.reloadTimer = 0

        self.powerUpTime = 100
        self.powerUpTimer = 0

        self.powerUp = 'none'

#control con teclado cambiar por joystick
    def update(self):
        timer = gcwindow_trial.time1
        
	axis_x = vars.joystick.get_axis(0)
        axis_y = vars.joystick.get_axis(1)
        axis_z = vars.joystick.get_axis(3)
##        if (not self.yPos + self.height > vars.height) and axis_x < -0.2:
##            self.yPos += self.speed
##        elif (not self.yPos < 0) and axis_x > 0.2:
##            self.yPos -= self.speed
##
##        if (not self.xPos + self.width > vars.width) and axis_y < -0.2:
##            self.xPos += self.speed
##        elif (not self.xPos < 0) and axis_y > 0.2:
##            self.xPos -= self.speed


        deg = math.pi/2
        cos = math.cos(deg)
        sin = math.sin(deg)


        
        if  axis_y > 0.1:
##            self.yPos += self.speed * axis_y
            self.yPos += cos * axis_y * self.speed
            self.xPos += sin * axis_y * self.speed

            
        elif axis_y < -0.1:
##            self.yPos -= self.speed * -axis_y
            self.yPos += cos * axis_y * self.speed
            self.xPos += sin * axis_y * self.speed

        if axis_x > 0.1:
##            self.xPos -= self.speed * -axis_x         
            self.xPos += cos * axis_x * self.speed
            self.yPos -= sin * axis_x * self.speed
            
        elif axis_x < -0.1:
##            self.xPos -= self.speed * -axis_x
            self.xPos += cos * axis_x * self.speed
            self.yPos -= sin * axis_x * self.speed


        if (self.yPos + self.height > vars.height):
            self.yPos = vars.height - self.height 
        elif (self.yPos <= 0):
            self.yPos = 0
        if(self.xPos + self.width > vars.width):
            self.xPos = vars.width - self.width
        elif (self.xPos <= 0):
            self.xPos = 0


        if self.reloadTimer < self.reloadTime:
            self.reloadTimer += 1

        if not self.powerUp == 'none':
            if self.powerUpTimer < self.powerUpTime:
                self.powerUpTimer += 1
            else:
                self.powerUp = 'none'
                self.powerUpTimer = 0

        if axis_z >= -0.02 :
            self.umbral = 1
            self.reloadTimer = 0
## se crea esta condicion pasra que no caiga el juego por empezar con palanca 2 arriba

        if axis_z < -0.02 and timer<1000:
            self.umbral = 1
            self.reloadTimer = 0

        n1= -0.02;
        n2= -0.15;
        n3= -0.3;
        if vars.pathbala == 'uno':
            funcs.printText("Balas:  " + '1,2,3   '+"Puntos:  " + (str(vars.points)), 22, -1, 10, (0,255,0))
            if axis_z < n1 and axis_z > n2 and self.reloadTimer >= 20:
                if self.powerUp  == 'none' and self.umbral==1 :

                    vars.bulletList1.append(bulletSimple1(self.xPos, self.yPos + ((self.height / 2) - 1), 0))
                self.umbral=0
                self.reloadTimer = 0


            if axis_z < n2 and axis_z > n3 and self.reloadTimer >= 20:
                if self.powerUp == 'none' and self.umbral==1 :
                   
                    vars.bulletList2.append(bulletSimple2(self.xPos, self.yPos + ((self.height / 2) - 1), 0))
                self.umbral=0
                self.reloadTimer = 0



            if axis_z < n3 and self.reloadTimer >= 20:
                if self.powerUp == 'none' and self.umbral==1 :
                                     
                    vars.bulletList3.append(bulletSimple3(self.xPos, self.yPos + ((self.height / 2) - 1), 0))
                self.umbral=0
                self.reloadTimer = 0


        if vars.pathbala == 'dos':
##            funcs.printText("Balas:  " + 'vars.pathbala' + '\t' +"Puntos:  " + vars.points, 22, -1, 10, (0,255,0))
            funcs.printText("Balas:  " + '2,3,1   ' +"Puntos:  " + (str(vars.points)), 22, -1, 10, (0,255,0))

            if axis_z < n1 and axis_z > n2 and self.reloadTimer >= 20:         
                if self.powerUp  == 'none' and self.umbral==1 :
                                     
                    vars.bulletList2.append(bulletSimple2(self.xPos, self.yPos + ((self.height / 2) - 1), 0))
                self.umbral=0
                self.reloadTimer = 0

            if axis_z < n2 and axis_z > n3 and self.reloadTimer >= 20:
                if self.powerUp == 'none' and self.umbral==1 :
                                      
                    vars.bulletList3.append(bulletSimple3(self.xPos, self.yPos + ((self.height / 2) - 1), 0))
                self.umbral=0
                self.reloadTimer = 0


            if axis_z < n3 and self.reloadTimer >= 20:
                if self.powerUp == 'none' and self.umbral==1 :
                       
                    vars.bulletList1.append(bulletSimple1(self.xPos, self.yPos + ((self.height / 2) - 1), 0))
                self.umbral=0
                self.reloadTimer = 0


        if vars.pathbala == 'tres':
##            funcs.printText("Balas:  " + 'vars.pathbala' + '\t' +"Puntos:  " + vars.points , 22, -1, 10, (0,255,0))
            funcs.printText("Balas:  " + '3,1,2   ' +"Puntos:  " + (str(vars.points)), 22, -1, 10, (0,255,0))
            if axis_z < n1 and axis_z > n2 and self.reloadTimer >= 20:         
                if self.powerUp  == 'none' and self.umbral==1 :
                          
                    vars.bulletList3.append(bulletSimple3(self.xPos, self.yPos + ((self.height / 2) - 1), 0))
                self.umbral=0
                self.reloadTimer = 0

            if axis_z < n2 and axis_z > n3 and self.reloadTimer >= 20:
                if self.powerUp == 'none' and self.umbral==1 :
                                
                    vars.bulletList1.append(bulletSimple1(self.xPos, self.yPos + ((self.height / 2) - 1), 0))
                self.umbral=0
                self.reloadTimer = 0


            if axis_z < n3 and self.reloadTimer >= 20:
                if self.powerUp == 'none' and self.umbral==1 :
                            
                    vars.bulletList2.append(bulletSimple2(self.xPos, self.yPos + ((self.height / 2) - 1), 0))
                self.umbral=0
                self.reloadTimer = 0
            

    def draw(self):
        vars.screen.blit(self.sprite, (self.xPos,  self.yPos))


#Bullet Types


class enemyBulletSimple():
    def __init__(self, inputX, inputY):
        self.sprite = funcs.loadImage('bullet2.png', -1)

        self.xPos = inputX
        self.yPos = inputY

        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.speed = 11
        self.lives = 10

    def update(self):
        self.xPos -= self.speed

    def draw(self):
        vars.screen.blit(self.sprite, (self.xPos,  self.yPos))

    def checkState(self):
        if self.xPos < 0 - self.width:
            return 'delete'


#Powerups

class powerupMultishot():
    def __init__(self, inputX, inputY):
        self.sprite = funcs.loadImage('powerup.png', -1)

        self.xPos = inputX
        self.yPos = inputY

        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

        self.speed = 5

    def update(self):
        self.xPos -= self.speed

    def draw(self):
        vars.screen.blit(self.sprite, (self.xPos,  self.yPos))

    def checkState(self):
        if self.xPos < 0 - self.width:
            return 'delete'

#Enemies


class enemyRock():
    def __init__(self, inputX, inputY):
        self.sprite1 = funcs.loadImage('enemy1.png', -1)
        self.width = self.sprite1.get_width()
        self.height = self.sprite1.get_height()
        self.xPos = inputX
        self.yPos = inputY

        self.speed = 5
        self.lives = 1

    def update(self):
        self.xPos -= self.speed

    def draw(self):
        if self.lives == 1:
            vars.screen.blit(self.sprite1, (self.xPos,  self.yPos))
            
    def checkState(self):
        if self.xPos < 0 - self.width:
            return 'delete'

class enemyUFO():
    def __init__(self, inputX, inputY):
        self.sprite = funcs.loadImage('enemy2.png', -1)
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.xPos = inputX
        self.yPos = inputY
        self.originalYPos = inputY

        self.speed = 5
        self.lives = 1

    def update(self):
        self.xPos -= self.speed
        self.yPos = 60*math.sin(0.03*self.xPos)+ self.originalYPos

    def draw(self):
        vars.screen.blit(self.sprite, (self.xPos,  self.yPos))

    def checkState(self):
        if self.xPos < 0 - self.width:
            return 'delete'

class enemyRubble():
    def __init__(self, inputX, inputY):
        self.sprite = funcs.loadImage('enemy3.png', -1)
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.xPos = inputX
        self.yPos = inputY

        self.speed = 5
        self.lives = 50

    def update(self):
        self.xPos -= self.speed

    def draw(self):
        vars.screen.blit(self.sprite, (self.xPos,  self.yPos))

    def checkState(self):

        if self.xPos < 0 - self.width:
            return 'delete'

class enemyShooter():
    def __init__(self, inputX, inputY):
        self.sprite = funcs.loadImage('enemy4.png', -1)
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.xPos = inputX
        self.yPos = inputY
        self.originalYPos = inputY

        self.speed = 5
        self.lives = 1

        self.bulletTimer = 0
        self.bulletTime = 17

    def update(self):
        self.xPos -= self.speed
        self.yPos = 100*math.sin(0.02*self.xPos)+ self.originalYPos
        self.bulletTimer += 1
        if self.bulletTimer >= self.bulletTime:
            self.bulletTimer = 0
            vars.enemyList3.append(enemyBulletSimple(self.xPos, self.yPos + ((self.height / 2) - 1)))

    def draw(self):
        vars.screen.blit(self.sprite, (self.xPos,  self.yPos))

    def checkState(self):
        if self.xPos < 0 - self.width:
            return 'delete'

class enemyBoss():
    def __init__(self, inputX, inputY):
        self.sprite1 = funcs.loadImage('enemy5.png', 0)
        self.sprite2 = funcs.loadImage('enemy5_2.png', 0)
        self.sprite3 = funcs.loadImage('enemy5_3.png', 0)
        self.width = self.sprite1.get_width()
        self.height = self.sprite1.get_height()
        self.xPos = inputX
        self.yPos = inputY

        random.seed()

        self.speed = 0.5
        self.lives = 150

        self.bulletTimer = 0
        self.bulletTime = 7

    def update(self):
        self.xPos -= self.speed
        self.bulletTimer += 1

        if self.lives == 130:
            self.bulletTime = 5
        elif self.lives == 40:
            self.bulletTime = 4            
        
        if self.bulletTimer >= self.bulletTime:
            self.bulletTimer = 0
            bulletY = random.randint(1, 450)
            vars.enemyList3.append(enemyBulletSimple(self.xPos - 10, bulletY))

    def draw(self):
        if self.lives > 130:
            vars.screen.blit(self.sprite1, (self.xPos,  self.yPos))
        elif self.lives > 40:
            vars.screen.blit(self.sprite2, (self.xPos,  self.yPos))
        else:
            vars.screen.blit(self.sprite3, (self.xPos,  self.yPos))


    def checkState(self):
        if self.xPos < 0 - self.width:
            return 'delete'
        
    def __del__(self):
        vars.gameScreen = 'win'
