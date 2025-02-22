# usage: python echo_quat_server.py [mac]
from mbientlab.metawear import MetaWear, libmetawear, parse_value
from mbientlab.metawear.cbindings import *
from time import sleep
from threading import Event
import math

import platform
import sys
import socket, pickle
import struct
import json




if socket.gethostname()=="raspberrypi":
	name = 3
elif socket.gethostname()=="raspberrypi2":
	name = 4
else:
	print('mac_sensor1 = D7:24:48:BE:AC:CA')
	print('mac_sensor2  = E7:87:02:27:25:7F')
	print('mac_sensor3  = E3:A9:46:B7:FB:F3')
	print('mac_sensor4  = F8:6A:C8:82:37:8D')	
	name = input("ingresa el numero de sensor que quieres usar, ej. 7:")
# ~ name = 1
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))
s.listen()
clientsocket, address = s.accept()

sleep(2)




# ~ s.connect((HOST, PORT))

# ~ s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ~ s.bind((HOST, PORT))
# ~ s.listen(5)
# ~ clientsocket, address = s.accept()


# ~ from pylsl import StreamInfo, StreamOutlet

# ~ HOST = ''                 # Symbolic name meaning all available interfaces
# ~ PORT = 50007              # Arbitrary non-privileged port
# ~ s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ~ s.bind((socket.gethostname(), 1234))
# ~ s.listen(1)
# ~ conn, addr = s.accept()
# ~ print('Connected by', addr)

# ~ s1 = 9

# ~ info = StreamInfo('Mbientlab', 'Quat', 4, 100, 'float32', 'myuid0003')

# next make an outlet
# ~ outlet = StreamOutlet(info)

if sys.version_info[0] == 2:
	range = xrange

# obtiene data online
class State:
	def __init__(self, device):
		self.device = device
		self.samples = 0
		self.callback = FnVoid_VoidP_DataP(self.data_handler)
		self.temp_data = "nada"

	def data_handler(self, ctx, data):
		if self.samples < 20:
			print("%s -> %s" % (self.device.address, parse_value(data)))
		self.samples += 1
		q = parse_value(data, n_elem = 2)
		self.temp_data = q
		#enviar()

		# ~ temp = json.dumps({'pitch': temp_data.pitch, 'yaw':temp_data.yaw, 'roll':temp_data.roll})
		# ~ temp = json.dumps({'w': self.temp_data.w, 'x': self.temp_data.x, 'y':self.temp_data.y, 'z':self.temp_data.z})
		# ~ print(temp)
		
		for i in range(len(sensores)):
			if self.device.address == sensores[i]:
				sen = i
			
		
		# ~ print(f"Connection from {address} has been established.")	
		mysample = [sen,self.temp_data.pitch, self.temp_data.yaw, self.temp_data.roll]
				
		data_string = pickle.dumps(mysample)
		# ~ data_string =msgpack.packb(mysample, use_bin_type=True)
		try:
			clientsocket.send(data_string)
		except:
			print("Resetting devices")
			events = []
			for s in states:
				e = Event()
				events.append(e)

				s.device.on_disconnect = lambda s: e.set()
				libmetawear.mbl_mw_debug_reset(s.device.board)

			for e in events:
				e.wait()
		
		
		
		
		# ~ print(mysample)
    # now send it and wait for a bit
		# ~ outlet.push_sample(mysample)
		# ~ sleep(0.1)

		# ~ conn.sendall(temp)

states = []
mac_sensor = [];
mac_sensor.append('D7:24:48:BE:AC:CA')
mac_sensor.append('E7:87:02:27:25:7F')
mac_sensor.append('E3:A9:46:B7:FB:F3')
mac_sensor.append('F8:6A:C8:82:37:8D')


# ~ sensores = [mac_sensor1, mac_sensor2, mac_sensor3, mac_sensor4]
sensores = [mac_sensor[int(name)-1]] #5


for sensor in sensores:
	d = MetaWear(sensor)
	d.connect()
	print("Connected to " + d.address)
	states.append(State(d))

def start_streaming(t):
	for s in states:
		print("Configuring device")
		libmetawear.mbl_mw_settings_set_connection_parameters(s.device.board, 1.5, 1.5, 0, 6000)

		print("Sensor Fusion")
		libmetawear.mbl_mw_sensor_fusion_set_mode(s.device.board, SensorFusionMode.NDOF);
		libmetawear.mbl_mw_sensor_fusion_set_acc_range(s.device.board, SensorFusionAccRange._2G);
		libmetawear.mbl_mw_sensor_fusion_write_config(s.device.board);

		signal = libmetawear.mbl_mw_sensor_fusion_get_data_signal(s.device.board, SensorFusionData.EULER_ANGLE)
		# ~ signal = libmetawear.mbl_mw_sensor_fusion_get_data_signal(s.device.board, SensorFusionData.QUATERNION)
		libmetawear.mbl_mw_datasignal_subscribe(signal, None, s.callback)
		
		libmetawear.mbl_mw_sensor_fusion_enable_data(s.device.board, SensorFusionData.EULER_ANGLE);
		# ~ libmetawear.mbl_mw_sensor_fusion_enable_data(s.device.board, SensorFusionData.QUATERNION);
		libmetawear.mbl_mw_sensor_fusion_start(s.device.board)

		sleep(0.001)#0.001#0.005#0.03
		
	sleep(t)

	# ~ conn.close()

	print("Total Samples Received")
	for s in states:
		print("%s -> %d" % (s.device.address, s.samples))

	print("Resetting devices")
	events = []
	for s in states:
		e = Event()
		events.append(e)

		s.device.on_disconnect = lambda s: e.set()
		libmetawear.mbl_mw_debug_reset(s.device.board)

	for e in events:
		e.wait()

start_streaming(7200)
