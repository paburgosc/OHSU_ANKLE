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
		self.BLUE      = (  0, 0,   255) ### HERE BLUE
		self.LBLUE       = (  200,   200, 255) ### HERE lightBLUE
		self.GREEN      = (  0, 255,   0) ### HERE BLUE

		self.BGCOLOR = self.WHITE

		self.WINDOWWIDTH = vars.width # width of the program's window, in pixels
		self.WINDOWHEIGHT = vars.height # height in pixels
		self.WIN_CENTERX = int(self.WINDOWWIDTH / 2) # the midpoint for the width of the window
		self.WIN_CENTERY = int(self.WINDOWHEIGHT / 2) # the midpoint for the height of the window
		self.data_list3 = [["game","difficulty", "amplitude", "velocity", "time","xpos","y_computer","y_human","y_error","trial","x","y","z"]]

		#FPS = vars.fpsLimit # frames per second to run at


		with open(vars.archivo2) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			self.vel = []
			self.amp = []
			self.amp2= []
			self.kp  = []
			self.blocktimes =[0]
			for row in csv_reader:
				if line_count == 0:
					print(f'Column names are {", ".join(row)}')
					line_count += 1
				else:
					# print(f'\t{row[0]}  {row[1]} ')
					self.vel.append(float(row[0]))
					self.amp.append(float(row[1]))
					self.amp2.append(float(row[2]))
					self.kp.append(int(row[3]))
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


		# ~ vars.pause = False

		self.xPos = 0
		self.step = 0 # the current input f
		self.contador = 0
		self.count = 0
		self.count2 = 0
		self.contadorb = 0
		self.countb = 0
		self.count2b = 0
		self.inittime = vars.time
		self.inittime2 = vars.time

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


		self.instructionsSurf = self.fontObj.render('Esc menu, P pause', True, self.BLACK, self.BGCOLOR)
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
		
		self.showSquare2 = False




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
		writer = csv.writer(vars.f3)
		writer.writerows(data)
		print("Data saved")

	def main(self):

		vars.screen.fill(self.BGCOLOR)

		# draw instructions
		vars.screen.blit(self.instructionsSurf, self.instructionsRect)
		#OCt 2023
		# ~ if self.contador >= len(self.vel)-1:
			# ~ vars.screen.fill((255,255,255))
			# ~ vars.gameinit = False
			# ~ vars.gameScreen = 'menu'

		vars.AMPLITUDE= self.amp[self.contador]
		vars.AMPLITUDE2= self.amp2[self.contador]
		self.kpc = self.kp[self.contador]
		vars.step = self.vel[self.contador]
		self.AMPLITUDE = vars.AMPLITUDE
		self.AMPLITUDE2 = 150
		self.xPos2 = 400
		# sine wave
		# ~ yPos = -1 * math.sin(self.step) * vars.AMPLITUDE

		
		yPos = -1  * (self.AMPLITUDE2*(self.AMPLITUDE/100))
		yPos2 = 0

		# ~ yPos2 = -1  * vars.AMPLITUDE2

		# draw the border
		pygame.draw.rect(vars.screen, self.RED, (self.WIN_CENTERX-350,self.WIN_CENTERY+self.AMPLITUDE2,700 ,1))
		pygame.draw.rect(vars.screen, self.RED, (self.WIN_CENTERX-350,self.WIN_CENTERY-self.AMPLITUDE2,700 ,1))





		if not vars.pause:

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
			
			
			#####SHOW OR NOT
			if self.kpc:
				vars.showSquare = True
				self.showSquare2 = False
			else:
				if vars.time - self.inittime2 < 1500:
					vars.showSquare = False
					self.showSquare2 = False
				
				else:
					vars.showSquare = True
					self.showSquare2 = True
				
				
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
			ran = abs((vars.valup -val50))

			
			
			# ~ pygame.draw.rect(vars.screen, self.BLUE, (self.WIN_CENTERX-50, int(yPos) + self.WIN_CENTERY-10,100 ,20), 2)
			# ~ pygame.draw.rect(vars.screen, self.RED, (self.WIN_CENTERX-50,self.WIN_CENTERY,100 ,1))

				

			vars.factor = 1#0.75	
			# ~ if vars.y1b > -500 and vars.y1b < 500:##PB 27 12 19
			val = vars.y1b
			# ~ val = (self.AMPLITUDE/abs((vars.valup -val50)*vars.factor))*vars.y1b
			val = ((self.AMPLITUDE2*vars.factor)/abs(vars.valup -val50))*vars.y1b

			self.yPosSquare = int(val) + vars.offset
			
			self.posRecord['square'].append((int(self.WIN_CENTERX),  self.WIN_CENTERY - int(self.yPosSquare) ))
			

			
			valme = ((self.AMPLITUDE2*vars.factor)/abs(vars.valup -val50))*(vars.valme-val50)
			ce=self.WIN_CENTERY-int(valme)
			up=self.WIN_CENTERY-self.AMPLITUDE2
			do=self.WIN_CENTERY+self.AMPLITUDE2
			yPosup = ((ce-up)*(self.AMPLITUDE/100))
			yPosdo = ((do-ce)*(self.AMPLITUDE/100))
			# ~ print(yPosup)
			# ~ print(yPosdo)
			if vars.AMPLITUDE == 0:
				pygame.draw.rect(vars.screen, self.BLUE, (self.WIN_CENTERX-50, self.WIN_CENTERY - int(valme) -10,100 ,20), 2)
				yPos2 = self.WIN_CENTERY - int(valme)
				# ~ pygame.draw.rect(vars.screen, self.RED, (self.WIN_CENTERX-50,self.WIN_CENTERY,100 ,1)) 
			if vars.AMPLITUDE >0:
				pygame.draw.rect(vars.screen, self.BLUE, (self.WIN_CENTERX-50, self.WIN_CENTERY-int(abs(yPosup)) -int(valme) -10,100 ,20), 2)
				yPos2 = self.WIN_CENTERY-int(abs(yPosup)) -int(valme)
			if vars.AMPLITUDE <0:
				pygame.draw.rect(vars.screen, self.BLUE, (self.WIN_CENTERX-50, self.WIN_CENTERY+int(abs(yPosdo)) -int(valme) -10,100 ,20), 2)
				yPos2 = self.WIN_CENTERY+int(abs(yPosdo)) -int(valme)
				# ~ pygame.draw.rect(vars.screen, self.RED, (self.WIN_CENTERX-50,self.WIN_CENTERY,100 ,1))
			# ~ print(valme)
			pygame.draw.rect(vars.screen, self.RED, (self.WIN_CENTERX-350,self.WIN_CENTERY-int(valme),700 ,1))
			# ~ self.yback = self.yPosSquare

			# ~ else:
				# ~ self.yPosSquare = self.yback

			ysin = yPos2
			yimu = self.WIN_CENTERY  - int(self.yPosSquare)
			# ~ print(yimu)
			# ~ print(vars.time - self.inittime2)
			# draw the sine ball and label
			if vars.showSquare:
			# draw the sine ball and label
				pygame.draw.circle(vars.screen, self.BLUE, (int(self.WIN_CENTERX),  self.WIN_CENTERY-int(self.yPosSquare) ), 10)
				if self.showSquare2:
					for x, y in self.posRecord['square']:
						pygame.draw.circle(vars.screen, self.LBLUE, (x, y), 4)
			
			# ~ pygame.draw.circle(vars.screen, self.BLUE, (int(self.xPos2),yimu), 10)   #PB NOV 2024+

			if vars.time - self.inittime2 > 2000:
				self.inittime2 = vars.time
			# ~ if int(self.step/(2*math.pi)) >self.contador+self.contadorb:
				# ~ self.count = 1
				# ~ if self.count-self.count2 == 1:
				self.contador += 1
				print(self.contador)
				self.posRecord['square'] = [] 
					# ~ self.count2 = 1
				if self.contador >= 40:
					self.blocktimes.append((vars.time-self.inittime)/1000)
					self.data_list3.append(["Pausa_juego3",vars.gameLevel,str(vars.AMPLITUDE),str(vars.step) ,(str(vars.time- self.inittime2)),(str(self.xPos2)),(str(ysin)),(str(yimu)),(str(yimu-ysin)),(str(-1)),(str(vars.x1)),(str(vars.y1)),(str(vars.z1))])
					self.save_to_csv(self.data_list3)
					self.data_list3 = []
					# ~ vars.f3.write("Pausa_juego3" +'\t'+ vars.gameLevel +'\t'+ str(vars.AMPLITUDE)  +'\t'+  str(vars.step) +'\t'+(str(vars.time - self.inittime2))+'\t'+(str(self.xPos2))+'\t'+(str(ysin)) + '\t'+(str(yimu))+'\t'+(str(yimu-ysin))+'\t'+(str(self.contador))+'\t'+(str(vars.x1))+'\t'+(str(vars.y1))+'\t'+(str(vars.z1))+'\n') ##PB 27 12 19
					print(str(self.contador)+" repeticiones")
					print(str((vars.time-self.inittime)/1000)+" segundos")
					vars.pause = True
					self.contador = 0
		
				
			# ~ else:
				# ~ self.count = 0
				# ~ self.count2 = 0
			self.data_list3.append(["juego3" , vars.gameLevel , str(vars.AMPLITUDE)  ,  str(vars.step) ,(str(vars.time- self.inittime2)),(str(self.xPos2)),(str(ysin)) ,(str(yimu)),(str(yimu-ysin)),(str(self.contador)),(str(vars.x1)),(str(vars.y1)),(str(vars.z1))])

			# ~ vars.f3.write("juego3" +'\t'+ vars.gameLevel +'\t'+ str(vars.AMPLITUDE)  +'\t'+  str(vars.step) +'\t'+(str(vars.time - self.inittime2))+'\t'+(str(self.xPos2))+'\t'+(str(ysin)) + '\t'+(str(yimu))+'\t'+(str(yimu-ysin))+'\t'+(str(self.contador))+'\t'+(str(vars.x1))+'\t'+(str(vars.y1))+'\t'+(str(vars.z1))+'\n') ##PB 27 12 19

			
		else:
			print("tiempo "+str(((vars.time-self.inittime)/1000)-self.blocktimes[-1]))
			print("tiempo ejecutado " + str(self.blocktimes[-1]-self.blocktimes[-0]))
			vars.font2 = pygame.font.SysFont('Arial', 50)
			vars.screen.blit(vars.font2.render("THIS IS A PAUSE", True, (0,0,0)), (100, 100))
			vars.screen.blit(vars.font2.render("THANKS A LOT", True, (0,0,0)), (100, 300))
			

