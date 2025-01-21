import pygame
from random import choice
# ~ from pylsl import StreamInlet, resolve_stream
import sys,os
sys.path.insert(0, "lib")
sys.path.insert(0, "sounds")
import vars

class game3(object):
	def __init__(self):
		self.xm = int(vars.width/2)
		self.ym = int(vars.height/2)
		self.ypl = [[0,0,0,],[0,0,0]]
		self.textyp = "valmaxy"
		self.textyp2 = "0"
		# ~ vars.gameinit=0
		vars.font = pygame.font.SysFont('Arial', 12)
		self.font2 = pygame.font.SysFont('Arial', 30)
		self.xmov = True
		self.ymov = False
		self.zmov = False
		self.poss = 4
		self.veloc= [0,0]
		self.boton = -1
		
		pygame.mixer.init()
		self.flag = True
		self.cum =0
		vars.AMPLITUDE= 360
		vars.vision = "pa" #"ec"
		# ~ self.Pan3 = Pane()
		# ~ self.umbral = 1
		# ~ self.basal  = 2		
		vars.gameinit =False
		vars.gameinit2 =True
		self.libsounds ={}
		self.libsounds["original"] = ["do.wav","mi.wav","sol.wav","si.wav","si.wav"]
		self.libsounds["smoke"] = ["sow1.wav","sow2.wav","sow3.wav","sow4.wav","sow4.wav"]
		self.libsounds["letitbe"] = ["lib1.wav","lib4.wav","lib2.wav","lib3.wav","lib3.wav"]
		self.libsounds["money"] = ["Mfn1.wav","Mfn2.wav","Mfn3.wav","Mfn3.wav","Mfn3.wav"]
		self.libsounds["estrella"] = ["Ede1.wav","Ede2.wav","Ede3.wav","Ede3.wav","Ede3.wav"]
		self.libsounds["piensa"] = ["pem1.wav","pem2.wav","pem3.wav","pem4.wav","pem5.wav"]
		self.libsounds["back"] = ["Bib1.wav","Bib2.wav","Bib3.wav","Bib4.wav","Bib5.wav"]
		# ~ self.self.selso = choice(("original","original"))
		# ~ self.selso = choice(("smoke","smoke"))
		if vars.gameLevel == "facil": # # "medio","dificil"
			# ~ self.selso = "original"
			self.selso = choice(("estrella","money"))
		elif vars.gameLevel == "medio":
			self.selso = choice(("letitbe","smoke"))
		else:
			self.selso = choice(("piensa","back"))
			

		if self.selso == "estrella":
			self.sequence = "1 1 2 2 3 3 2"
		elif self.selso == "money":
			self.sequence = "1 2 3 1 1 2 2"
		elif self.selso == "letitbe":
			self.sequence = "1 1 3 3 4 4 3 2 4 4 3 3 2 2 1"
		elif self.selso == "smoke":
			self.sequence = "1 2 3 1 2 4 3 1 2 3 2 1"
		elif self.selso == "piensa":
			self.sequence = "1 2 3 4 4 4 3 2 3 3 3 2 1 2 2 2 1 5 1"
		elif self.selso == "back":
			self.sequence = "1 2 3 2 3 1 2 3 2 3 4 5 3 2 3"
		else:
			print("error selso")
		
		
		
		
		
		
		self.sounds=self.libsounds[self.selso]
		self.colorsquare=[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
		self.possquare=[-200,-100,0,100,200]
		self.fs = 0
		self.yback =0
				
	
	def main(self):

		
		if vars.flagPres:
			self.colorsquare=[(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
			self.poss=4
			self.sf =0
			self.sf +=1
			if self.sf<1:	
				rch= choice([0,1,2,3])
				# ~ print("rch "+str(rch))
				self.sounds[rch]					
				self.colorsquare[rch] = (255,0,0)
				self.poss = rch



				
			
		# ~ print (self.xm)
		# ~ e2 = sensores[1].getRoll()
		if vars.eje == 0:
			vars.y1b= vars.x1
		elif vars.eje == 1:	
			vars.y1b= vars.y1
		elif vars.eje == 2:	
			vars.y1b= vars.z1
		elif vars.eje > 2:
			vars.eje = 0
		# ~ print(vars.eje)	
		# ~ vars.y1b= vars.z1	
		
		val50 = (vars.valup-vars.valdo)/2.0
		# ~ val=0.1
		# ~ try:

		if val50 == 0:
			vars.screen.fill((255,255,255))
			vars.screen.blit(vars.font.render("calibrar primero", True, (0,0,0)), (100, 100))
			val50 = 0.001
			vars.gameinit = False
			
			vars.gameScreen = 'menu'			
		

		vars.factor = 1.5#0.75
		
		if vars.y1b > -500 and vars.y1b < 500:
			# ~ val1 = int(((vars.AMPLITUDE/2)/val50)*vars.y1b)
			val1 = (self.xm/(abs(val50)*vars.factor))*(vars.y1b-(vars.valup -val50))
			
			#val= self.xm-val1 # PB 20 01 2020
			val2 = int((val1 +vars.offset))
			val = self.xm+val2
			# ~ print (self.xm)
			# ~ print ((vars.y1b-(vars.valup -val50)))
			# ~ print (self.xm/abs(val50))
			# ~ print(val2)
			# ~ print(vars.valup)
			# ~ print(vars.y1b)
			# ~ print ((vars.y1b-(vars.valup -val50)))
			self.yback = val
			self.veloc[0] = self.veloc[1] 
			self.veloc[1] = vars.y1b
			
			
		else:
			val = self.yback
			
		self.difvel = self.veloc[1]-self.veloc[0]
		print(self.difvel)
		# ~ if self.xmov:
			# ~ pygame.draw.line(vars.screen, (0, 0, 255), (self.xm,self.ym+80),(self.xm,self.ym-80), 2)
		pygame.draw.circle(vars.screen, (0, 0, 255), (val,self.ym+20), 10)	
		pygame.draw.rect(vars.screen, self.colorsquare[0], (self.xm+self.possquare[0], self.ym, 60, 60), 2)
		pygame.draw.rect(vars.screen, self.colorsquare[1], (self.xm+self.possquare[1], self.ym, 60, 60), 2)
		pygame.draw.rect(vars.screen, self.colorsquare[2], (self.xm+self.possquare[2], self.ym, 60, 60), 2)
		if vars.gameLevel == "medio" or vars.gameLevel == "dificil":
			pygame.draw.rect(vars.screen, self.colorsquare[3], (self.xm+self.possquare[3], self.ym, 60, 60), 2)
		if vars.gameLevel == "dificil":
			pygame.draw.rect(vars.screen, self.colorsquare[4], (self.xm+self.possquare[4], self.ym, 60, 60), 2)
		# ~ val = self.xm-(int(vars.x1)*2)
		# ~ print(self.flag)
		# ~ print(self.cum)
		# ~ cf = 12
		vf = 0.03
		if (val >self.xm+self.possquare[0] and val< self.xm+self.possquare[0]+60) or self.poss==0:
			self.cum +=1 
			if self.flag:
				
				# ~ if self.cum >=cf:
				if abs(self.difvel) < vf:
					fileLocation = "./sounds/"+ self.sounds[0]   #os.path.join('res', self.sounds[0])
					pygame.mixer.music.load(fileLocation)
					pygame.mixer.music.play()
					self.cum=0
					self.boton = 0
					self.flag = False
		elif (val >self.xm+self.possquare[1] and val< self.xm+self.possquare[1]+60) or self.poss ==1:
			self.cum +=1
			if self.flag:
				 
				# ~ if self.cum >=cf:
				if abs(self.difvel) < vf:
					fileLocation = "./sounds/"+ self.sounds[1] #os.path.join('res', self.sounds[1])
					pygame.mixer.music.load(fileLocation)
					pygame.mixer.music.play()
					self.cum=0
					self.boton = 1
					self.flag = False
		elif (val >self.xm+self.possquare[2] and val < self.xm+self.possquare[2]+60) or self.poss==2:
			self.cum +=1 
			if self.flag:
				
				# ~ if self.cum>=cf:
				if abs(self.difvel) < vf:
					fileLocation = "./sounds/"+ self.sounds[2] #os.path.join('res', self.sounds[2])
					pygame.mixer.music.load(fileLocation)
					pygame.mixer.music.play()
					self.cum=2
					self.boton = 0
					self.flag = False
		elif (val >self.xm+self.possquare[3] and val< self.xm+self.possquare[3]+60) or self.poss==3:
			self.cum +=1
			if self.flag and (vars.gameLevel == "medio" or vars.gameLevel == "dificil"):
				 
				# ~ if self.cum >=cf:
				if abs(self.difvel) < vf:
					fileLocation = "./sounds/"+ self.sounds[3] #os.path.join('res', self.sounds[3])
					pygame.mixer.music.load(fileLocation)
					pygame.mixer.music.play()
					self.cum=0
					self.boton = 3
					self.flag = False
		elif (val >self.xm+self.possquare[4] and val< self.xm+self.possquare[4]+60) or self.poss==3:
			self.cum +=1
			if self.flag and vars.gameLevel == "dificil":
				 
				# ~ if self.cum >=cf:
				if abs(self.difvel) < vf:
					fileLocation = "./sounds/"+ self.sounds[4] #os.path.join('res', self.sounds[3])
					pygame.mixer.music.load(fileLocation)
					pygame.mixer.music.play()
					self.cum=0
					self.boton = 4
					self.flag = False
		else:
			self.flag = True
			self.cum = 0									
		x = vars.xemouse
		y = vars.yemouse
		
		xrl = [self.xm-130,self.xm-30,self.xm+70]
		yrl = [self.ym-160,self.ym+100]
		xys = ["x","y","z"]

		wr = 60
		hr2 = 60
		il = 0
		jl = 0
	
	

		#menu
		pygame.draw.rect(vars.screen, (0, 0, 0), (100, 100, 60, 60), 2)
		vars.screen.blit(vars.font.render("menu", True, (0,0,0)), (100, 100))
		
				#ojo abierto
		pygame.draw.rect(vars.screen, (0, 0, 0), (200, 100, 60, 60), 2)
		vars.screen.blit(vars.font.render("ojos", True, (0,0,0)), (200, 100))
		vars.screen.blit(vars.font.render("abiertos", True, (0,0,0)), (200, 120))
		
		
				#ojo cerrado
		pygame.draw.rect(vars.screen, (0, 0, 0), (300, 100, 60, 60), 2)
		vars.screen.blit(vars.font.render("ojos", True, (0,0,0)), (300, 100))
		vars.screen.blit(vars.font.render("cerrados", True, (0,0,0)), (300, 120))
		
		#pausa
		pygame.draw.rect(vars.screen, (0, 0, 0), (400, 100, 60, 60), 2)
		vars.screen.blit(vars.font.render("pausa", True, (0,0,0)), (400, 100))

		vars.screen.blit(self.font2.render("secuencia = "+self.sequence, True, (0,0,0)), (250, 200))

		
		if (x >= 100 and x <= 160) and (y >= 100 and y <= 160):
			# ~ vars.gameScreen = 'menu'
			vars.gameinit2 = False
			
		elif (x >= 200 and x <= 260) and (y >= 100 and y <= 160):
			 #ojo abierto
			vars.vision = "eo"
		elif (x >= 300 and x <= 360) and (y >= 100 and y <= 160):
			# ojo cerrado
			vars.vision = "ec"
		elif (x >= 400 and x <= 460) and (y >= 100 and y <= 160):
			# ojo cerrado
			vars.vision = "pa"
			
		vars.f3.write("juego3" +'\t'+ vars.gameLevel +'\t'+ self.selso + '\t'+ str(vars.vision) + '\t'+ str(vars.time)+'\t'+ str(self.xm)+'\t'+ str(self.boton) + '\t'+ str(vars.x1)+'\t'+ str(vars.y1) +'\t'+ str(vars.z1)+'\n') ##PB 27 12 19

			# ~ vars.screen.fill((255,255,255))	
		# ~ except:
			# ~ vars.screen.blit(vars.font.render("calibrar primero", True, (0,0,0)), (100, 100))
			
			# ~ vars.gameScreen = 'menu'
