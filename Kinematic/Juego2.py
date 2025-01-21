import pygame
# ~ from pylsl import StreamInlet, resolve_stream
import sys
sys.path.insert(0, "lib")
import vars



class juego2(object):
	def __init__(self):
		self.xm = int(vars.width/2)
		self.ym = int(vars.height/2)
		# ~ self.ypl = [[0,0,0,],[0,0,0]]
		# ~ self.textyp = "valmaxy"
		# ~ self.textyp2 = "0"
		# ~ vars.gameinit=0
		# ~ vars.font = pygame.font.SysFont('Arial', 12)
		# ~ self.Pan3 = Pane()
		# ~ self.umbral = 1
		# ~ self.basal  = 2		
		
	
	def main(self):
		print (self.xm)
		pygame.draw.line(vars.screen, (0, 0, 255), (self.xm,self.ym+80),(self.xm,self.ym-80), 2)
		pygame.draw.circle(vars.screen, (0, 0, 255), (self.xm,self.ym+int(vars.y1)), 10)	
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm-30, self.ym-160, 60, 60), 2)
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm-30, self.ym+100, 60, 60), 2)
		

		pygame.draw.line(vars.screen, (0, 0, 255), (self.xm-100,self.ym+80),(self.xm-100,self.ym-80), 2)
		pygame.draw.circle(vars.screen, (0, 0, 255), (self.xm-100,self.ym+int(vars.x1)), 10)
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm-130, self.ym-160, 60, 60), 2)
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm-130, self.ym+100, 60, 60), 2)	
		
		pygame.draw.line(vars.screen, (0, 0, 255), (self.xm+100,self.ym+80),(self.xm+100,self.ym-80), 2)
		pygame.draw.circle(vars.screen, (0, 0, 255), (self.xm+100,self.ym+int(vars.z1)), 10)
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm+70, self.ym-160, 60, 60), 2)
		pygame.draw.rect(vars.screen, (0, 0, 0), (self.xm+70, self.ym+100, 60, 60), 2)	
		
		
		x = vars.xemouse
		y = vars.yemouse
		
		xrl = [self.xm-130,self.xm-30,self.xm+70]
		yrl = [self.ym-160,self.ym+100]
		xys = ["x","y","z"]

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
						if il ==0:
							self.ypl[jl][il] = vars.x1
						if il ==1:
							self.ypl[jl][il] = vars.y1
						if il ==2:
							self.ypl[jl][il] = vars.z1							
				self.textyp2= str(self.ypl[jl][il])
				
				# ~ print("lentxt "+ str(len(self.textyp2)))
				if len(self.textyp2)>6:
					self.textyp2=self.textyp2[0:6]
					
				if jl == 0:
					self.textyp = "val_max_"+xys[il]
				else:
					self.textyp = "val_min_"+xys[il]
						
				vars.screen.blit(vars.font.render(self.textyp, True, (0,0,0)), (xr+10, yr))
				vars.screen.blit(vars.font.render(self.textyp2, True, (0,0,0)), (xr+10, yr+20))

