# usage: python echo_quat_server.py [mac]
import serial
import sys
# ~ from pylsl import StreamInfo, StreamOutlet
import pickle
from time import strftime,localtime, sleep, time
import serial.tools.list_ports

ports = []
for i in serial.tools.list_ports.comports():
	print(i)
	if 'ACM' in str(i) or 'acm' in str(i) or 'Arduino' in str(i) or 'USB' in str(i):
		ports.append(str(i).split(" ")[0]) 


# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 65432        # The port used by the server

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen()
# clientsocket, address = s.accept()

# sleep(2)







# ~ namep = input("ingresa perto arduino yun (COM5, COM3, etc.. ver arduino ide, tools):")
namep = ports[0]
ser = serial.Serial(namep)
ser.flushInput()
r = None

# first create a new stream info (here we set the name to BioSemi,
# the content-type to FSR, 1 channels, 500 Hz, and float-valued data) The
# last value would be the serial number of the device or some other more or
# less locally unique identifier for the stream as far as available (you
# could also omit it but interrupted connections wouldn't auto-recover)
# ~ info = StreamInfo('Arduino', 'FSR', 1, 1000, 'float32', 'myuid34234')

# next make an outlet
# ~ outlet = StreamOutlet(info)

print("now sending data...")

start_time1 = time()### add by PB 02 22 2014
date1=strftime("%d.%m.%Y", localtime(start_time1))### add by PB 02 22 2014
time1=strftime("%H:%M:%S", localtime(start_time1))### add by PB 02 22 2014

filename = (date1[0:2] + date1[3:5] + date1[6:10] + time1[0:2] + time1[3:5] + time1[6:8])

# ~ f = open('./files/'+filename+'arduino.txt','a')
samples = 0
while True:
	# ~ if(not connected):
		# ~ try:
			# ~ s.connect((HOST, PORT))
			# ~ print("Server connected")
			# ~ connected = True
		# ~ except:
	ser_bytes = ser.readline()
	# ~ print(ser_bytes)
	
	decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
	try:
		mysample = [float(decoded_bytes)]
		if samples <20:
			print(mysample)
# 		data_string = pickle.dumps(mysample)
        with open('my_listf.pkl', 'wb') as file11:
            pickle.dump(mysample, file11)	
# 		clientsocket.send(data_string)
# 		clientsocket.settimeout(0)	
		samples += 1
	except:
		print("not sending")

	#sleep(0.001)
