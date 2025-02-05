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
		vars.pause = False
		self.WHITE      = (255, 255, 255)
		self.DARKRED    = (255,   200,   200)
		self.RED        = (255,   0,   0)
		self.BLACK      = (  0,   0,   0)
		self.GREEN      = (  0, 0,   255) ### HERE BLUE
		self.BLUE       = (  200,   200, 255) ### HERE lightBLUE

		self.BGCOLOR = self.WHITE

		self.WINDOWWIDTH = vars.width # width of the program's window, in pixels
		self.WINDOWHEIGHT = vars.height # height in pixels
		self.WIN_CENTERX = int(self.WINDOWWIDTH / 2) # the midpoint for the width of the window
		self.WIN_CENTERY = int(self.WINDOWHEIGHT / 2) # the midpoint for the height of the window

		#FPS = vars.fpsLimit # frames per second to run at
		self.data_list1 = [["game","difficulty", "amplitude", "velocity", "time","xpos","y_computer","y_human","y_error","trial","x","y","z"]]
		# ~ self.ffs1 = 1


		with open(vars.archivo) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			self.vel = []
			self.amp = []
			self.kp = []
			self.blocktimes =[0]
			for row in csv_reader:
				if line_count == 0:
					print(f'Column names are {", ".join(row)}')
					line_count += 1
				else:
					# print(f'\t{row[0]}  {row[1]} ')
					self.vel.append(float(row[0]))
					self.amp.append(float(row[1]))
					self.kp.append(float(row[2]))
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
		# ~ self.showSquare = True ### HERE

		# ~ vars.pause = False

		self.xPos = 0
		vars.stepb = 0 # the current input f
		# ~ vars.stepb2 = 0
		self.contador = 0
		self.count = 0
		self.count2 = 0
		self.contadorb = 0
		self.countb = 0
		self.count2b = 0
		self.inittime = vars.time

		vars.AMPLITUDE= self.amp[self.contador]
		vars.step = self.vel[self.contador]
		self.AMPLITUDE = vars.AMPLITUDE

		### HERE 
		self.posRecord = {'sin': [], 'square': []} # keeps track of the ball positions for drawing the waves

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
		self.yPosSquare = 0 #vars.AMPLITUDE # starting position
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

	def save_to_csv(self, data):
		# ~ with open(filename, mode='w', newline='') as file:
		writer = csv.writer(vars.f1)
		writer.writerows(data)
		print("Data saved")

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
		# ~ if self.contador >= len(self.vel)-1:
			# ~ vars.screen.fill((255,255,255))
			# ~ ## ~ vars.font2 = pygame.font.SysFont('Arial', 50)
			# ~ ## ~ vars.screen.blit(vars.font2.render("calibrar primero", True, (0,0,0)), (100, 100))
			# ~ ## ~ val50 = 0.001
			# ~ vars.gameinit = False
			# ~ vars.gameScreen = 'menu'

		vars.AMPLITUDE= self.amp[self.contador]
		vars.step = self.vel[self.contador]
		self.kpc = int(self.kp[self.contador])
		# ~ print("kpc")
		# ~ print(self.kpc)
		self.AMPLITUDE = vars.AMPLITUDE
		self.AMPLITUDE2 = 150 ##########150 up and down in 100%
		self.xPos2 = 700
		# sine wave
		val50 = (vars.valup+vars.valdo)/2.0
		valme = ((self.AMPLITUDE2*vars.factor)/abs(vars.valup -val50))*(vars.valme-val50)
		ce=self.WIN_CENTERY-int(valme)
		up=self.WIN_CENTERY-self.AMPLITUDE2
		do=self.WIN_CENTERY+self.AMPLITUDE2
		yPosup = abs(ce-up)#*(self.AMPLITUDE/100))
		yPosdo = abs(do-ce)#*(self.AMPLITUDE/100))
		
		if vars.pause:
			# ~ vars.stepb = 0
			yPos = (-1 * math.sin(0) * (self.AMPLITUDE2*(self.AMPLITUDE/100)))+ abs(ce-self.WIN_CENTERY)-1

			self.posRecord['sin'].append((int(self.xPos), int(yPos) + self.WIN_CENTERY))
			# ~ self.posRecord['sin'].append((int(self.xPos)+self.xPos2, int(yPos) + self.WIN_CENTERY))

		else:
			if vars.stepb < math.pi:
				yPos = (-1 * math.sin(vars.stepb) * (yPosup*(self.AMPLITUDE/100))) + abs(ce-self.WIN_CENTERY)
			else:
				yPos = (-1 * math.sin(vars.stepb) * (yPosdo*(self.AMPLITUDE/100))) + abs(ce-self.WIN_CENTERY)
			# ~ if vars.stepb < 1 : #PB2025
				# ~ ypos = 0
			self.posRecord['sin'].append((int(self.xPos), int(yPos) + self.WIN_CENTERY))
			# ~ self.posRecord['sin'].append((int(self.xPos)+self.xPos2, int(yPos) + self.WIN_CENTERY))
		if vars.showSine:
			# draw the sine ball and label
			pygame.draw.circle(vars.screen, self.RED, (int(self.xPos2), int(yPos) + self.WIN_CENTERY), 13)
			# ~ self.sinLabelRect.center = (int(self.xPos), int(yPos) + self.WIN_CENTERY + 20)
			# ~ vars.screen.blit(self.sinLabelSurf, self.sinLabelRect)

		# draw the waves from the previously recorded ball positions
		listsin = list(self.posRecord['sin'])
		# ~ print(listsin)
		if vars.showSine:
			for x, y in self.posRecord['sin']:
			# ~ for x, y in listsin.reverse():
				pygame.draw.circle(vars.screen, self.DARKRED, ((self.xPos2-int(self.xPos)) + x, y), 4)

		### HERE - drawing horizontal lines
		# square is the IMU
		# ~ self.posRecord['square'].append((int(self.xPos)+self.xPos2,  self.WIN_CENTERY - int(self.yPosSquare) ))
		self.posRecord['square'].append((int(self.xPos),  self.WIN_CENTERY - int(self.yPosSquare) ))
		

			
		
		if vars.showSquare:
			# draw the sine ball and label
			pygame.draw.circle(vars.screen, self.GREEN, (int(self.xPos2),  self.WIN_CENTERY-int(self.yPosSquare) ), 10)
			# ~ self.squareLabelRect.center = (int(self.xPos), int(self.yPosSquare) + self.WIN_CENTERY + 20)
			# ~ vars.screen.blit(self.squareLabelSurf, self.squareLabelRect)

		# draw the waves from the previously recorded ball positions
		if vars.showSquare:
			for x, y in self.posRecord['square']:
				pygame.draw.circle(vars.screen, self.BLUE, ((self.xPos2-int(self.xPos))+x, y), 4)

		# draw the border
		pygame.draw.rect(vars.screen, self.RED, (self.WIN_CENTERX-350,self.WIN_CENTERY+self.AMPLITUDE2,700 ,1))
		pygame.draw.rect(vars.screen, self.RED, (self.WIN_CENTERX-350,self.WIN_CENTERY-self.AMPLITUDE2,700 ,1))
		# ~ pygame.draw.rect(vars.screen, self.BLACK, (0, 0, self.WINDOWWIDTH, self.WINDOWHEIGHT), 1)

		# ~ pygame.display.update()##PB 27 12 19
		# ~ vars.clock.tick(vars.fpsLimit)

		if not vars.pause:
			self.xPos += 0.5
			
			if self.xPos > self.xPos2:
				# ~ self.delelem = 1
			# ~ if self.xPos > self.WINDOWWIDTH:

				
				#sine ### HERE
				# ~ print(vars.stepb)
				# ~ print(self.contador)
				# ~ self.xPos = 0 #PB2024
				# ~ lenposrec = len(self.posRecord['sin'])-1
				del self.posRecord['sin'][0]
				del self.posRecord['square'][0]
				# ~ self.posRecord['sin'] = self.posRecord['sin'][-lenposrec:]
#				vars.stepb = 0   #PB 28 01 2020

				# square ### HERE
				# ~ self.yPosSquare = vars.AMPLITUDE
				# ~ self.posRecord['square'] = self.posRecord['square'][-lenposrec:]
			if self.xPos>=0:
				#sine ### HERE
				vars.stepb += vars.step
				
				if self.kpc:
					vars.showSquare = True
					
				else:
					if vars.stepb < (2*math.pi)*0.75:
					# ~ if vars.stepb/(2*math.pi) < 1+0.75:
						vars.showSquare = False
					
					else:
						vars.showSquare = True
				
				
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
					
				
				vars.factor = 1#self.AMPLITUDE/100#1#0.75	
				if vars.y1b > -500 and vars.y1b < 500:##PB 27 12 19
					val = ((self.AMPLITUDE2*vars.factor)/abs(vars.valup -val50))*vars.y1b
					self.yPosSquare = int(val) + vars.offset
					self.yback = self.yPosSquare
				# ~ elif vars.y1b > 0 and vars.y1b <= 180:
					# ~ val
					# ~ self.yPosSquare = (vars.y1b * vars.factor) + vars.offset
					# ~ self.yback = self.yPosSquare					
				else:
					self.yPosSquare = self.yback
				#draw middle line
				valme = ((self.AMPLITUDE2*vars.factor)/abs(vars.valup -val50))*(vars.valme-val50)
				# ~ print(valme)
				pygame.draw.rect(vars.screen, self.RED, (self.WIN_CENTERX-350,self.WIN_CENTERY-valme,700 ,1))

				# ~ self.posRecord['square'].append((int(self.xPos), self.WIN_CENTERY  - int(self.yPosSquare) )) #PB 2024
				# ~ print(self.yPosSquare)
				ysin = int(yPos)+self.WIN_CENTERY
				yimu = self.WIN_CENTERY  - int(self.yPosSquare)


				# ~ if int(vars.stepb/(2*math.pi)) >self.contador+self.contadorb:
				if vars.stepb >= (2*math.pi):
					vars.stepb=0
					self.count = 1
					if self.count-self.count2 == 1:
						# ~ self.xPos = 0  #PB 2024
						# ~ self.posRecord['sin'] = []
						# ~ self.posRecord['square'] = []
						self.contador += 1
						print(self.contador) 
						self.count2 = 1
						if self.contador in [10,20,30,40,50,60,70,80,90,100,110]:
							self.blocktimes.append((vars.time-self.inittime)/1000)
							self.data_list1.append(["Pausa_juego1",vars.gameLevel,str(vars.AMPLITUDE),str(vars.step) ,(str(vars.time)),(str(self.xPos2)),(str(ysin)),(str(yimu)),(str(yimu-ysin)),(str(-1)),(str(vars.x1)),(str(vars.y1)),(str(vars.z1))])
							self.save_to_csv(self.data_list1)
							print("saving data")
							self.data_list1 = []

							# ~ vars.f1.write("Pausa_juego1" +'\t'+ vars.gameLevel +'\t'+ str(vars.AMPLITUDE)  +'\t'+  str(vars.step) +'\t'+(str(vars.time))+'\t'+(str(self.xPos2))+'\t'+(str(ysin)) + '\t'+(str(yimu))+'\t'+(str(yimu-ysin))+'\t'+(str(self.contador))+'\t'+(str(vars.x1))+'\t'+(str(vars.y1))+'\t'+(str(vars.z1))+'\n') ##PB 27 12 19
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
				self.data_list1.append(["juego1" , vars.gameLevel , str(vars.AMPLITUDE)  ,  str(vars.step) ,(str(vars.time)),(str(self.xPos2)),(str(ysin)) ,(str(yimu)),(str(yimu-ysin)),(str(self.contador)),(str(vars.x1)),(str(vars.y1)),(str(vars.z1))])
				# ~ vars.f1.write("juego1" +'\t'+ vars.gameLevel +'\t'+ str(vars.AMPLITUDE)  +'\t'+  str(vars.step) +'\t'+(str(vars.time))+'\t'+(str(self.xPos2))+'\t'+(str(ysin)) + '\t'+(str(yimu))+'\t'+(str(yimu-ysin))+'\t'+(str(self.contador))+'\t'+(str(vars.x1))+'\t'+(str(vars.y1))+'\t'+(str(vars.z1))+'\n') ##PB 27 12 19
					
				# ~ print(self.xPos)

				#step %= 2 * math.pi

				# square ### HERE
				# jump top and bottom every 100 pixels
				# ~ if xPos % 50 == 0:
				# ~ if xPos > 0:
								# move with imu
			
		else:

			self.xPos += 0.5
			vars.font2 = pygame.font.SysFont('Arial', 50)
			
			if self.contador<len(self.vel)-1:
				vars.screen.blit(vars.font2.render("THIS IS A PAUSE", True, (0,0,0)), (100, 100))
				vars.screen.blit(vars.font2.render("READY FOR THE NEXT ONE?", True, (0,0,0)), (100, 300))
			
			else:
				# ~ vars.screen.fill((white))
				vars.screen.blit(vars.font2.render("THIS IS THE END OF THIS BLOCK", True, (0,0,0)), (100, 100))
				vars.screen.blit(vars.font2.render("THANKS A LOT", True, (0,0,0)), (100, 300))
				# ~ vars.screen.fill((white))
				# ~ vars.gameScreen = 'menu'
				# ~ vars.gameinit = False
				# ~ vars.screen.fill((white))
			if self.xPos > self.xPos2:
				print("tiempo "+str(((vars.time-self.inittime)/1000)-self.blocktimes[-1]))
				print("tiempo ejecutado " + str(self.blocktimes[-1]-self.blocktimes[-0]))
				# ~ print(vars.stepb)
				del self.posRecord['sin'][0]
				del self.posRecord['square'][0]
				#sine ### HERE
				# ~ self.xPos = 0
				# ~ self.posRecord['sin'] = []
# ~ #				vars.stepb = 0   #PB 28 01 2020

				# ~ # square ### HERE
				# ~ #self.yPosSquare = vars.AMPLITUDE
				# ~ self.posRecord['square'] = []
			if self.xPos >=0:
				#sine ### HERE
				# ~ vars.stepb = 0 #PB2025
				vars.stepb += vars.step
				
				
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
					
				
				vars.factor = 1	
				if vars.y1b > -500 and vars.y1b < 500:##PB 27 12 19
					# ~ val = (self.AMPLITUDE/abs((vars.valup -val50)*vars.factor))*vars.y1b
					val = ((self.AMPLITUDE2*vars.factor)/abs(vars.valup -val50))*vars.y1b
					self.yPosSquare = int(val) + vars.offset
					self.yback = self.yPosSquare
				# ~ elif vars.y1b > 0 and vars.y1b <= 180:
					# ~ val
					# ~ self.yPosSquare = (vars.y1b * vars.factor) + vars.offset
					# ~ self.yback = self.yPosSquare					
				else:
					self.yPosSquare = self.yback
				# ~ self.posRecord['square'].append((int(self.xPos), self.WIN_CENTERY  - int(self.yPosSquare) ))		
				# ~ print(self.yPosSquare)
				valme = ((self.AMPLITUDE2*vars.factor)/abs(vars.valup -val50))*(vars.valme-val50)
				# ~ print(valme)
				pygame.draw.rect(vars.screen, self.RED, (self.WIN_CENTERX-350,self.WIN_CENTERY-valme,700 ,1))
				
				
				ysin = int(yPos)+self.WIN_CENTERY
				yimu = self.WIN_CENTERY  - int(self.yPosSquare)
				
				# ~ if int(vars.stepb/(2*math.pi)) >self.contadorb+self.contador:
				if vars.stepb>=(2*math.pi):
					self.countb = 1
					vars.stepb = 0
					if self.countb-self.count2b == 1:
						self.contadorb += 1
						# ~ print(self.contadorb) 
						self.count2b = 1
						# ~ self.xPos = 0  #PB 2024
						# ~ self.posRecord['sin'] = []
						# ~ self.posRecord['square'] = []
						# ~ if self.contador in [10,20,30,40,50,60,70,80,90,100]:
							# ~ print(str(self.contador)+" repeticiones")
							# ~ print(str((vars.time-self.inittime)/1000)+" segundos")
							# ~ vars.pause = True
				else:
					self.countb = 0
					self.count2b = 0


