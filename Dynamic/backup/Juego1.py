import sys, pygame, math
from pygame.locals import *
from time import sleep, time
from random import choice
# ~ import numpy as np
sys.path.insert(0, "lib")
import vars
import csv


	# ~ if vars.gameinit:
		# set up a bunch of constants
class gaming1(object):		
	def __init__(self):		
		
		self.WHITE      = (255, 255, 255)
		self.DARKRED    = (128,   0,   0)
		self.RED        = (255,   0,   0)
		self.BLACK      = (  0,   0,   0)
		self.GREEN      = (  0, 255,   0) ### HERE
		self.BLUE       = (  0,   0, 255) ### HERE

		self.BGCOLOR = self.WHITE

		self.WINDOWWIDTH = vars.width # width of the program's window, in pixels
		self.WINDOWHEIGHT = vars.height # height in pixels
		self.WIN_CENTERX = int(self.WINDOWWIDTH / 2) # the midpoint for the width of the window
		self.WIN_CENTERY = int(self.WINDOWHEIGHT / 2) # the midpoint for the height of the window

		#FPS = vars.fpsLimit # frames per second to run at


		with open(vars.archivo) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			self.vel = []
			self.amp = []
			self.blocktimes =[0]
			for row in csv_reader:
				if line_count == 0:
					print(f'Column names are {", ".join(row)}')
					line_count += 1
				else:
					# print(f'\t{row[0]}  {row[1]} ')
					self.vel.append(float(row[0]))
					self.amp.append(float(row[1]))
					line_count += 1
			# ~ self.vel.append=self.vel[-1]
			# ~ self.amp.append
#Oct 2023
		# ~ if vars.gameLevel == "facil": # # "medio","dificil"
			# ~ vars.AMPLITUDE = choice((80,80,80)) # how many pixels tall the waves with rise/fall.
			# ~ vars.step = choice((0.008,0.008,0.008))
		# ~ elif vars.gameLevel == "medio":
			# ~ vars.AMPLITUDE = choice((80,80,80)) # how many pixels tall the waves with rise/fall.
			# ~ vars.step = choice((0.008,0.008,0.008))
		# ~ else:
			# ~ vars.AMPLITUDE = choice((80,80,80)) # how many pixels tall the waves with rise/fall.
			# ~ vars.step = choice((0.008,0.008,0.008))
#Oct 2023
		# ~ if vars.gameLevel == "facil": # # "medio","dificil"
			# ~ vars.AMPLITUDE = choice((40,50,60)) # how many pixels tall the waves with rise/fall.
			# ~ vars.step = choice((0.004,0.005,0.006))
		# ~ elif vars.gameLevel == "medio":
			# ~ vars.AMPLITUDE = choice((70,80,90)) # how many pixels tall the waves with rise/fall.
			# ~ vars.step = choice((0.007,0.008,0.009))
		# ~ else:
			# ~ vars.AMPLITUDE = choice((100,110,120)) # how many pixels tall the waves with rise/fall.
			# ~ vars.step = choice((0.010,0.011,0.012))

		# standard pygame setup code
		# ~ pygame.init()
		# ~ FPSCLOCK = pygame.time.Clock()
		# ~ DISPLAYSURF = vars.screen #pygame.display.set_mode((WINDOWWIDTH, self.WINDOWHEIGHT))
		# ~ pygame.display.set_caption('Trig Waves')
		self.fontObj = pygame.font.Font('freesansbold.ttf', 16)

		# variables that track visibility modes
		# ~ vars.showSine = True
		self.showSquare = True ### HERE

		# ~ vars.pause = False

		self.xPos = self.WIN_CENTERX+300
		self.xPos2 = self.WIN_CENTERX+300
		self.step = 0 # the current input f
		self.contador = 0
		self.count = 0
		self.count2 = 0
		self.contadorb = 0
		self.countb = 0
		self.count2b = 0
		self.inittime = vars.time
		self.stepl=0

		vars.AMPLITUDE= self.amp[self.contador]
		vars.step = self.vel[self.contador]
		self.AMPLITUDE = vars.AMPLITUDE

		### HERE 
		self.posRecord = {'sin': [], 'square': []} # keeps track of the ball positions for drawing the waves
		self.posRecord2 = {'sin': [], 'square': []}
		# making text Surface and Rect objects for various labels

		### HERE 
		self.squareLabelSurf = self.fontObj.render(' ', True, self.BLUE, self.BGCOLOR)#square
		self.squareLabelRect = self.squareLabelSurf.get_rect()

		self.sinLabelSurf = self.fontObj.render(' ', True, self.RED, self.BGCOLOR)#sin
		self.sinLabelRect = self.sinLabelSurf.get_rect()


		self.instructionsSurf = self.fontObj.render('S oculta, P pausa, Flechas AB agrandan, FLECHAS DI aceleran, AZ offset', True, self.BLACK, self.BGCOLOR)
		self.instructionsRect = self.instructionsSurf.get_rect()
		self.instructionsRect.left = 10
		self.instructionsRect.bottom = self.WINDOWHEIGHT - 10

		### HERE
		self.yPosSquare = vars.AMPLITUDE # starting position
		self.yback =0
		self.countsin = 0
		self.countsin2 = 0
		vars.gameinit=False
		vars.gameinit2 =True




	def salir(self):        
		print('Exportando datos...')
		for sensor in self.sensores:
			sensor.device.disconnect()
			sleep(1)
		for sensor in self.sensores:
			sensor.exportarDatos('datos_%f.txt' % time())
		print('Exportacion exitosa')
		sys.exit()

	# ~ def quat2euler(q): #z y x
		# ~ #// roll (x-axis rotation)
		# ~ sinr_cosp = +2.0 * (q.w * q.x + q.y * q.z);
		# ~ cosr_cosp = +1.0 - 2.0 * (q.x * q.x + q.y * q.y);
		# ~ anglesroll = math.atan2(sinr_cosp, cosr_cosp);
		
		# ~ #// pitch (y-axis rotation)
		# ~ sinp = +2.0 * (q.w * q.y - q.z * q.x);
		# ~ if (math.fabs(sinp) >= 1):
			# ~ anglespitch = math.copysign(np.pi / 2, sinp);# // use 90 degrees if out of range
		# ~ else:
			# ~ anglespitch = math.asin(sinp);
		
		# ~ #// yaw (z-axis rotation)
		# ~ siny_cosp = +2.0 * (q.w * q.z + q.x * q.y);
		# ~ cosy_cosp = +1.0 - 2.0 * (q.y * q.y + q.z * q.z);  
		# ~ anglesyaw = math.atan2(siny_cosp, cosy_cosp);
		
		
		# ~ print('angles roll = ' +  str(np.rad2deg(anglesroll)))
		# ~ print('angles pitch = ' +  str(np.rad2deg(anglespitch)))
		# ~ print('angles yaw = ' +  str(np.rad2deg(anglesyaw)))
		
		# ~ return anglesroll,anglespitch,anglesyaw


	def main(self):
		# ~ timeg1 = vars.time-vars.timeonset
		# ~ print(timeg1)
		
			
	# ~ def main():
		# event handling loop for quit events
		# ~ for event in pygame.event.get():
			# ~ if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				# ~ pygame.quit()
				# ~ sys.exit()

			# ~ # check for key presses that toggle pausing and wave visibility
		# fill the screen to draw from a blank state
		vars.screen.fill(self.BGCOLOR)

		# draw instructions
		vars.screen.blit(self.instructionsSurf, self.instructionsRect)
		#OCt 2023
		if self.contador >= len(self.vel)-1:
			vars.screen.fill((255,255,255))
			# ~ vars.font2 = pygame.font.SysFont('Arial', 50)
			# ~ vars.screen.blit(vars.font2.render("calibrar primero", True, (0,0,0)), (100, 100))
			# ~ val50 = 0.001
			vars.gameinit = False
			vars.gameScreen = 'menu'

		vars.AMPLITUDE= self.amp[self.contador]
		vars.step = self.vel[self.contador]
		self.AMPLITUDE = vars.AMPLITUDE
		# sine wave
		self.stepl = int((2*math.pi)/vars.step)#len(list(range(0,2*math.pi,self.step)))
		# ~ stepl = len(np.arange(0,2*np.pi,self.step))
		yPos = -1 * math.sin(self.step) * vars.AMPLITUDE
		self.posRecord['sin'].append((int(self.xPos), int(yPos) + self.WIN_CENTERY))
		self.posRecord2['sin'].append((int(self.xPos2), int(yPos) + self.WIN_CENTERY))
		
		# ~ print(self.xPos2)
		
		if vars.showSine:
			# draw the sine ball and label
			pygame.draw.circle(vars.screen, self.RED, (int(self.xPos), int(yPos) + self.WIN_CENTERY), 10)
			# ~ self.sinLabelRect.center = (int(self.xPos), int(yPos) + self.WIN_CENTERY + 20)
			# ~ vars.screen.blit(self.sinLabelSurf, self.sinLabelRect)

		# draw the waves from the previously recorded ball positions
		if vars.showSine:
			for x, y in self.posRecord2['sin']:
				pygame.draw.circle(vars.screen, self.DARKRED, (x, y), 4)

		### HERE - drawing horizontal lines
		# square is the IMU
		self.posRecord['square'].append((int(self.xPos),  self.WIN_CENTERY - int(self.yPosSquare) ))
		self.posRecord2['square'].append((int(self.xPos2),  self.WIN_CENTERY - int(self.yPosSquare) ))
		if self.showSquare:
			# draw the sine ball and label
			pygame.draw.circle(vars.screen, self.GREEN, (int(self.xPos),  self.WIN_CENTERY-int(self.yPosSquare) ), 10)
			# ~ self.squareLabelRect.center = (int(self.xPos), int(self.yPosSquare) + self.WIN_CENTERY + 20)
			# ~ vars.screen.blit(self.squareLabelSurf, self.squareLabelRect)

		# draw the waves from the previously recorded ball positions
		if self.showSquare:
			for x, y in self.posRecord2['square']:
				pygame.draw.circle(vars.screen, self.BLUE, (x, y), 4)

		# draw the border
		# ~ pygame.draw.rect(vars.screen, self.BLACK, (0, 0, self.WINDOWWIDTH, self.WINDOWHEIGHT), 1)

		# ~ pygame.display.update()##PB 27 12 19
		# ~ vars.clock.tick(vars.fpsLimit)

		if not vars.pause:
			self.xPos2 -= 0.5
			self.xPos  = self.WIN_CENTERX+300
			
			# ~ if self.xPos2 < 10:
			if self.xPos2 < int((self.WIN_CENTERX+300)-(self.stepl)):
				#sine ### HERE
				print(self.step)
				self.xPos2 = self.WIN_CENTERX+300
				elf.xPos = self.WIN_CENTERX+300
				self.posRecord['sin'] = []
				self.posRecord2['sin'] = []
				self.posRecord['square'] = []
				self.posRecord2['square'] = []
			else:
				#sine ### HERE
				self.step += vars.step
				
				
				# ~ sample, timestamp = vars.inlet.pull_sample()
				# ~ print(timestamp, sample)
				# ~ e1 = sample[1]
				# ~ e1 = sensores[0].getRoll()
				
				# ~ e2 = sensores[1].getRoll()
				if vars.eje == 0:
					vars.y1b= vars.x1
				elif vars.eje == 1:	
					vars.y1b= vars.y1
				elif vars.eje == 2:	
					vars.y1b= (vars.z1)# -180,  PB 27 12 19
				elif vars.eje > 2:
					vars.eje = 0
				# ~ print(vars.y1b)	
				# ~ vars.y1b= vars.z1	
				
				val50 = (vars.valup+vars.valdo)/2.0
				
				
				if val50 == 0:
					vars.font2 = pygame.font.SysFont('Arial', 50)
					vars.screen.fill((255,255,255))
					vars.screen.blit(vars.font2.render("calibrar primero", True, (0,0,0)), (100, 100))
					val50 = 0.001
					vars.gameinit = False
					
					vars.gameScreen = 'menu'					
				
				# ~ elif val50 > 0:
					# ~ vars.y1b = vars.y1b-val50
				# ~ elif val50 < 0:
					# ~ vars.y1b = vars.y1b+val50						
				vars.y1b = vars.y1b-val50
				
				# ~ if vars.valup<vars.valdo:  ##TEST
					# ~ vars.y1b = -vars.y1b
					
				
				vars.factor = 0.75	
				if vars.y1b > -500 and vars.y1b < 500:##PB 27 12 19
					val = (self.AMPLITUDE/abs((vars.valup -val50)*vars.factor))*vars.y1b
					self.yPosSquare = int(val) + vars.offset
					self.yback = self.yPosSquare
				# ~ elif vars.y1b > 0 and vars.y1b <= 180:
					# ~ val
					# ~ self.yPosSquare = (vars.y1b * vars.factor) + vars.offset
					# ~ self.yback = self.yPosSquare					
				else:
					self.yPosSquare = self.yback
				self.posRecord['square'].append((int(self.xPos), self.WIN_CENTERY  - int(self.yPosSquare) ))
				self.posRecord2['square'].append((int(self.xPos2), self.WIN_CENTERY  - int(self.yPosSquare) ))
				# ~ print(self.yPosSquare)
				ysin = int(yPos)+self.WIN_CENTERY
				yimu = self.WIN_CENTERY  - int(self.yPosSquare)
				
				if (self.contador % 2) == 0:
					self.showSquare=1
				else:
					self.showSquare=0

				if int(self.step/(2*math.pi)) >self.contador+self.contadorb:
					self.count = 1
					if self.count-self.count2 == 1:
						self.contador += 1
						print(self.contador) 
						self.count2 = 1
						if self.contador in [10,20,30,40,50,60,70,80,90,100]:
							self.blocktimes.append((vars.time-self.inittime)/1000)
							vars.f1.write("Pausa_juego1" +'\t'+ vars.gameLevel +'\t'+ str(vars.AMPLITUDE)  +'\t'+  str(vars.step) +'\t'+(str(vars.time))+'\t'+(str(self.xPos))+'\t'+(str(ysin)) + '\t'+(str(yimu))+'\t'+(str(yimu-ysin))+'\t'+(str(self.contador))+'\t'+(str(vars.x1))+'\t'+(str(vars.y1))+'\t'+(str(vars.z1))+'\n') ##PB 27 12 19
							print(str(self.contador)+" repeticiones")
							print(str((vars.time-self.inittime)/1000)+" segundos")
							vars.pause = True
						if self.contador in [11,21,31,41,51,61,71,81,91,101]:
							self.inittime = vars.time
				else:
					self.count = 0
					self.count2 = 0
				
				# ~ if ysin == 379:
					# ~ self.count = 1
					# ~ if self.count-self.count2 == 1:
						# ~ self.contador += 1
						# ~ print(self.contador) 
						# ~ self.count2 = 1
						# ~ if self.contador in [10,20,30,40,50,60,70,80,90,100]:
							# ~ print(str(self.contador)+" repeticiones")
							# ~ print(str((vars.time-self.inittime)/1000)+" segundos")
							# ~ vars.pause = True
				# ~ else:
					# ~ self.count = 0
					# ~ self.count2 = 0
					
					
					


				
				
				if ysin == 300:
					self.countsin += 1
					
				else:
					self.countsin = 0
					
				if self.countsin == 1:		
					self.countsin2 += 1
					
				vars.f1.write("juego1" +'\t'+ vars.gameLevel +'\t'+ str(vars.AMPLITUDE)  +'\t'+  str(vars.step) +'\t'+(str(vars.time))+'\t'+(str(self.xPos))+'\t'+(str(ysin)) + '\t'+(str(yimu))+'\t'+(str(yimu-ysin))+'\t'+(str(self.contador))+'\t'+(str(vars.x1))+'\t'+(str(vars.y1))+'\t'+(str(vars.z1))+'\n') ##PB 27 12 19
					
				# ~ print(self.xPos)

				#step %= 2 * math.pi

				# square ### HERE
				# jump top and bottom every 100 pixels
				# ~ if xPos % 50 == 0:
				# ~ if xPos > 0:
								# move with imu
			
		else:
			print("tiempo "+str(((vars.time-self.inittime)/1000)-self.blocktimes[-1]))
			print("tiempo ejecutado " + str(self.blocktimes[-1]-self.blocktimes[-0]))
			self.xPos2 -= 0.5
			self.xPos  = self.WIN_CENTERX+300
			vars.font2 = pygame.font.SysFont('Arial', 50)
			vars.screen.blit(vars.font2.render("ESTAMOS EN UNA PAUSA", True, (0,0,0)), (100, 100))
			vars.screen.blit(vars.font2.render("ATENTO AL INICIO", True, (0,0,0)), (100, 300))
			if self.xPos2 < int((self.WIN_CENTERX+300)-(self.stepl)):
			# ~ if self.xPos2 < 10:#> self.WINDOWWIDTH:
				#sine ### HERE
				self.xPos2  = self.WIN_CENTERX+300
				self.xPos  = self.WIN_CENTERX+300
				self.posRecord['sin'] = []
				self.posRecord2['sin'] = []
				self.posRecord['square'] = []
				self.posRecord2['square'] = []
#				self.step = 0   #PB 28 01 2020

				# square ### HERE
				# ~ self.yPosSquare = vars.AMPLITUDE

			else:
				#sine ### HERE
				self.step += vars.step
				
				
				# ~ sample, timestamp = vars.inlet.pull_sample()
				# ~ print(timestamp, sample)
				# ~ e1 = sample[1]
				# ~ e1 = sensores[0].getRoll()
				
				# ~ e2 = sensores[1].getRoll()
				if vars.eje == 0:
					vars.y1b= vars.x1
				elif vars.eje == 1:	
					vars.y1b= vars.y1
				elif vars.eje == 2:	
					vars.y1b= (vars.z1)# -180,  PB 27 12 19
				elif vars.eje > 2:
					vars.eje = 0
				# ~ print(vars.y1b)	
				# ~ vars.y1b= vars.z1	
				
				val50 = (vars.valup+vars.valdo)/2.0
				
				
				if val50 == 0:
					vars.screen.fill((255,255,255))
					vars.font2 = pygame.font.SysFont('Arial', 50)
					vars.screen.blit(vars.font2.render("calibrar primero", True, (0,0,0)), (100, 100))
					val50 = 0.001
					vars.gameinit = False
					
					vars.gameScreen = 'menu'					
				
				# ~ elif val50 > 0:
					# ~ vars.y1b = vars.y1b-val50
				# ~ elif val50 < 0:
					# ~ vars.y1b = vars.y1b+val50						
				vars.y1b = vars.y1b-val50
				
				# ~ if vars.valup<vars.valdo:  ##TEST
					# ~ vars.y1b = -vars.y1b
					
				
				vars.factor = 0.75	
				if vars.y1b > -500 and vars.y1b < 500:##PB 27 12 19
					val = (self.AMPLITUDE/abs((vars.valup -val50)*vars.factor))*vars.y1b
					self.yPosSquare = int(val) + vars.offset
					self.yback = self.yPosSquare
				# ~ elif vars.y1b > 0 and vars.y1b <= 180:
					# ~ val
					# ~ self.yPosSquare = (vars.y1b * vars.factor) + vars.offset
					# ~ self.yback = self.yPosSquare					
				else:
					self.yPosSquare = self.yback
				self.posRecord['square'].append((int(self.xPos), self.WIN_CENTERY  - int(self.yPosSquare) ))
				self.posRecord2['square'].append((int(self.xPos2), self.WIN_CENTERY  - int(self.yPosSquare) ))
				# ~ print(self.yPosSquare)
				ysin = int(yPos)+self.WIN_CENTERY
				yimu = self.WIN_CENTERY  - int(self.yPosSquare)
				
				if int(self.step/(2*math.pi)) >self.contadorb+self.contador:
					self.countb = 1
					if self.countb-self.count2b == 1:
						self.contadorb += 1
						print(self.contadorb) 
						self.count2b = 1
						# ~ if self.contador in [10,20,30,40,50,60,70,80,90,100]:
							# ~ print(str(self.contador)+" repeticiones")
							# ~ print(str((vars.time-self.inittime)/1000)+" segundos")
							# ~ vars.pause = True
				else:
					self.countb = 0
					self.count2b = 0


