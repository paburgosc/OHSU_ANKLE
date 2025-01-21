import pygame
import sys
sys.path.insert(0, "lib")
import vars
# ~ from pylsl import StreamInlet, resolve_stream


class calibra(object):
	def __init__(self):
		self.xm = int(vars.width/2)
		self.ym = int(vars.height/2)
		self.ypl = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
		self.textyp = "valmaxy"
		self.textyp2 = "0"
		vars.gameinit=False
		vars.gameinit2=True
		vars.font = pygame.font.SysFont('Arial', 12)
		# ~ self.Pan3 = Pane()
		# ~ self.umbral = 1
		# ~ self.basal  = 2		
		
	
	def main(self):
		# ~ print (self.xm)
		pygame.draw.line(vars.screen, (0, 0, 255), (self.xm,self.ym+80),(self.xm,self.ym-80), 2)
		pygame.draw.circle(vars.screen, (0, 0, 255), (self.xm,self.ym-int(vars.y1)), 10)	
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm-30, self.ym-160, 60, 60), 2)
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm-30, self.ym+100, 60, 60), 2)
		

		pygame.draw.line(vars.screen, (0, 0, 255), (self.xm-100,self.ym+80),(self.xm-100,self.ym-80), 2)
		pygame.draw.circle(vars.screen, (0, 0, 255), (self.xm-100,self.ym-int(vars.x1)), 10)
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm-130, self.ym-160, 60, 60), 2)
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm-130, self.ym+100, 60, 60), 2)
		
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm-180, self.ym-30, 60, 60), 2)
		pygame.draw.line(vars.screen, (0, 0, 255), (self.xm+100,self.ym+80),(self.xm+100,self.ym-80), 2)
		pygame.draw.circle(vars.screen, (0, 0, 255), (self.xm+100,self.ym-(int(vars.z1))), 10)##PB 27 12 19
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm+70, self.ym-160, 60, 60), 2)
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm+70, self.ym+100, 60, 60), 2)	
		
		vars.screen.blit(vars.font.render("Presiona i, para invertir eje z", True, (0,0,0)), (self.xm+70, self.ym-180))


		
		x = vars.xemouse
		y = vars.yemouse
		
		xrl = [self.xm-130,self.xm-30,self.xm+70,self.xm-180]
		yrl = [self.ym-160,self.ym+100,self.ym-30]
		xys = ["x","y","z","m"]

		wr = 60
		hr2 = 60
		il = 0
		jl = 0
		for il in range(len(xrl)):
			i = xrl[il]
			for jl in range(len(yrl)):
				# ~ print("listjl "+str(jl))
				j = yrl[jl]
				
				xr= i
				
				yr= j
				
				if (x >= xr and x <= xr+wr) and (y >= yr and y <= yr+hr2):
					if vars.mc:
						# ~ print("valmaxy")
						vars.eje = il
						if il ==0:
							self.ypl[jl][il] = vars.x1
						if il ==1:
							self.ypl[jl][il] = vars.y1
						if il ==2:
							self.ypl[jl][il] = vars.z1
						if il ==3:
							self.ypl[jl][il] = vars.x1
				self.textyp2= str(self.ypl[jl][il])
				
				# ~ print("lentxt "+ str(len(self.textyp2)))
				if len(self.textyp2)>6:
					self.textyp2=self.textyp2[0:6]
					
				if jl == 0:
					self.textyp = "val_max_"+xys[il]
				if jl == 1:
					self.textyp = "val_min_"+xys[il]
				if jl == 2 and il == 3:
					self.textyp = "val_med_"+xys[il]
				vars.screen.blit(vars.font.render(self.textyp, True, (0,0,0)), (xr+10, yr))
				vars.screen.blit(vars.font.render(self.textyp2, True, (0,0,0)), (xr+10, yr+20))

		#menu
		pygame.draw.rect(vars.screen, (0, 0, 0), (100, 100, 60, 60), 2)
		vars.screen.blit(vars.font.render("menu", True, (0,0,0)), (100, 100))
		
		if (x >= 100 and x <= 160) and (y >= 100 and y <= 160):
			vars.valup= self.ypl[0][vars.eje]
			vars.valdo= self.ypl[1][vars.eje]
			vars.valme= self.ypl[2][3]
			vars.gameinit2 = False
		
	def main2(self):	

		vars.valup= self.ypl[0][vars.eje]
		vars.valdo= self.ypl[1][vars.eje]
		vars.valme= self.ypl[2][3]
		vars.f0.write("juego1" +'\t'+str(vars.eje)+'\t'+str(vars.valup)+'\t'+str(vars.valme)+'\t'+str(vars.valdo)+'\n')
			
			# ~ vars.gameScreen = 'menu'
			# ~ vars.juego1 =False
			# ~ vars.screen.fill((255,255,255))	

