#/'/

import smbus
import time
from enum import Enum

class Direction(Enum):
	CCW = 2
	CW = 1

class Command(Enum):
	STEPPER_MOVE = 0x01
	STEPPER_STOP = 0x04
	WAIT_SWITCH = 0x05
	CLEAR_POLL = 0x10
	WAIT_HALL = 0x11
	REQUEST = 0xAA
	CUP_EJECT = 0x20

class Result(Enum):
	TRUE = 1
	FALSE = 0

bus = smbus.SMBus(1)


def readData(address):
	value = None

	while (value is None):
		try:
			value = bus.read_i2c_block_data(address,0,2)
		except:
			print("read error!")
			pass

	parsedValue = value[0:2]
	print(parsedValue) 

	return parsedValue
#	value = bus.read_byte_data(address,3)
#	return value

def sendCommand(address, command, p1,p2,p3):

	#Commands:
	# Stepper Direction (1 for CCW and 2 for CW). Speed (RPM)
	# 0x01: Stepper Free Rotate (direction, speed, 0)
	# 0x02: Stepper Timed Rotate (direction, speed, seconds)
	# 0x03: Stepper Steps Rotate (direction, speed, steps)
	# 0x04: Stepper Stop (0,0,0)
	# 0x05: Calibrate (0,0,0)
	# 0x10: Clear States (0,0,0)
	# 0x11: Request Hall Sensor (0,0,0)
	# 0x20: Dispense Cup
	# 0xaa: Wait (command, response)
	# 0x
	data = [command, p1, p2, p3]
	print("Sending command: " + str(command) + " to " + str(address) + " with args " + str(p1) + ", " + str(p2) + ", " + str(p3) + ".")
	try:
		bus.write_i2c_block_data(address,0,data)
	except:
		pass

def waitOnUnity(address,command,response):
	#poll for data on that address until event is tripped (or 20 seconds)
	print("Waiting on Unity at " + str(address) + " for " + str(response) + " response to command " + str(command) + ".")

	pollCount = 0;
	maxPollCount = 1000;
	data = None

	while (data is None) or ((data[1] is not response) and (pollCount < maxPollCount)):
		try:
			sendCommand(address,0xaa,command,response,0)
			data = readData(address)
		except:
			print("i2c read hiccup!")
			pass
		print(pollCount)
		pollCount=pollCount+1
		time.sleep(0.1)
	if pollCount is maxPollCount:
		print("[!] i2c read error or Unity process incomplete")
		return False
	else:
		print("Unity process completed successfully.")
		return True

def newRequestCallback(pval, fval, cval):
	print("New Request Received:")
	print("Protein: " +str(pval) + "%")
	print("Fat: " +str(fval) + "%")
	print("Carbs: " + str(cval) + "%\n")
	
	
	beginProcess()


def beginProcess():
	#Calibrate Gantry Cart
	sendCommand(0xA,Command.STEPPER_MOVE.value,Direction.CW.value,60,0)
	waitOnUnity(0xA,Command.WAIT_SWITCH.value,Result.TRUE.value)
	sendCommand(0xA,Command.STEPPER_STOP.value,0,0,0)
	sendCommand(0x4,Command.CLEAR_POLL.value,0,0,0)
	sendCommand(0x5,Command.CLEAR_POLL.value,0,0,0)
	sendCommand(0x6,Command.CLEAR_POLL.value,0,0,0)
	sendCommand(0xA,Command.CLEAR_POLL.value,0,0,0)
	time.sleep(0.5)

	#Eject Cup
	sendCommand(0x3, Command.CUP_EJECT.value,0,0,0)
	time.sleep(5)

	#Move Cart to First Ingredient
	sendCommand(0xA,Command.STEPPER_MOVE.value,Direction.CCW.value,120,0)
	waitOnUnity(0x4,Command.WAIT_HALL.value,Result.TRUE.value)
	time.sleep(0.25)
	sendCommand(0xA,Command.STEPPER_STOP.value,0,0,0)
	time.sleep(1)

	#Dispense First Ingredient
	sendCommand(0x4,Command.STEPPER_MOVE.value,Direction.CW.value,40,0)
	time.sleep(0.5)
	sendCommand(0x4,Command.STEPPER_STOP.value,0,0,0)
	time.sleep(2)

	#Move Cart to Second Ingredients
	sendCommand(0xA,Command.STEPPER_MOVE.value,Direction.CCW.value,120,0)
	waitOnUnity(0x5,Command.WAIT_HALL.value,Result.TRUE.value)
	time.sleep(0.25)
	sendCommand(0xA,Command.STEPPER_STOP.value,0,0,0)
	time.sleep(1)

	#Dispense Second Ingredient
	sendCommand(0x5,Command.STEPPER_MOVE.value,Direction.CW.value,40,0)
	time.sleep(0.5)
	sendCommand(0x5,Command.STEPPER_STOP.value,0,0,0)
	time.sleep(2)

	#Move Cart to Third Ingredient
	sendCommand(0xA,Command.STEPPER_MOVE.value,Direction.CCW.value,120,0)
	waitOnUnity(0x6,Command.WAIT_HALL.value,Result.TRUE.value)
	time.sleep(0.25)
	sendCommand(0xA,Command.STEPPER_STOP.value,0,0,0)
	time.sleep(1)

	#Dispense Third Ingredient
	sendCommand(0x6,Command.STEPPER_MOVE.value,Direction.CW.value,40,0)
	time.sleep(0.5)
	sendCommand(0x6,Command.STEPPER_STOP.value,0,0,0)
	time.sleep(2)
	
	#Continue To End
	sendCommand(0xA,Command.STEPPER_MOVE.value,Direction.CCW.value,30,0)
	time.sleep(0.2)
	sendCommand(0xA,Command.STEPPER_MOVE.value,Direction.CCW.value,60,0)
	time.sleep(0.2)
	sendCommand(0xA,Command.STEPPER_MOVE.value,Direction.CCW.value,120,0)
	time.sleep(0.2)
	sendCommand(0xA,Command.STEPPER_STOP.value,0,0,0)
	time.sleep(1)

	sendCommand(0xA,Command.STEPPER_MOVE.value,Direction.CCW.value,60,0)
	waitOnUnity(0xA,Command.WAIT_SWITCH.value,Result.TRUE.value)
	sendCommand(0xA,Command.STEPPER_STOP.value,0,0,0)

	sendCommand(0x3,Command.CLEAR_POLL.value,0,0,0)
	sendCommand(0x4,Command.CLEAR_POLL.value,0,0,0)
	sendCommand(0x5,Command.CLEAR_POLL.value,0,0,0)
	sendCommand(0x6,Command.CLEAR_POLL.value,0,0,0)
	sendCommand(0xA,Command.CLEAR_POLL.value,0,0,0)

	print("\nGranolaPod Complete! Returning to UI.\n")
	time.sleep(3)
