import RPi.GPIO as gpio
import time
import numpy as np		
import math

def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(31, gpio.OUT)
	gpio.setup(33, gpio.OUT)
	gpio.setup(35, gpio.OUT)
	gpio.setup(37, gpio.OUT)

	gpio.setup(7, gpio.IN, pull_up_down= gpio.PUD_UP)
	gpio.setup(12, gpio.IN, pull_up_down= gpio.PUD_UP)

def gameover():
	gpio.output(31, False)
	gpio.output(33, False)
	gpio.output(35, False)
	gpio.output(37, False)
	
	gpio.cleanup()




file1 = open("Encoder_data_5.txt","a")



#file1 = open("Encoder_data_3.txt","a")

def forward(ticks):
	init()


	counterBR = np.uint64(0)
	counterFL = np.uint64(0)

	buttonBR = int(0)
	buttonFL = int(0)

	# Initialize pwm signal to control motor
	pwm1 = gpio.PWM(31,50)
	pwm2 = gpio.PWM(37,50)
	val = 80
	pwm1.start(val)
	pwm2.start(val)
	time.sleep(0.1)

	for i in range (0,10000000):
		print("counterBR = ",counterBR,"counterFL = ",counterFL,"BR state: ", gpio.input(12),"FL state: ", gpio.input(7))
		file1.write(str(gpio.input(12))+str(gpio.input(7))+"\n")

		if int(gpio.input(12) != int(buttonBR)):
			buttonBR = int(gpio.input(12))
			counterBR += 1

		if int(gpio.input(7) != int(buttonFL)):
			buttonFL = int(gpio.input(7))
			counterFL = counterFL+1
		
		if counterFL >= ticks-1:
			pwm1.stop()
			
		if counterBR >= ticks:
			pwm2.stop()


		if counterBR >=ticks and counterFL >= ticks-1 :	
			gameover()
			print("Thanks for Playing")
			#file1.close()
			break

def reverse(ticks):
	init()


	counterBR = np.uint64(0)
	counterFL = np.uint64(0)

	buttonBR = int(0)
	buttonFL = int(0)

	# Initialize pwm signal to control motor
	pwm1 = gpio.PWM(33,50)
	pwm2 = gpio.PWM(35,50)
	val = 80
	pwm1.start(val)
	pwm2.start(val)
	time.sleep(0.1)

	for i in range (0,10000000):
		print("counterBR = ",counterBR,"counterFL = ",counterFL,"BR state: ", gpio.input(12),"FL state: ", gpio.input(7))
		file1.write(str(gpio.input(12))+str(gpio.input(7))+"\n")

		if int(gpio.input(12) != int(buttonBR)):
			buttonBR = int(gpio.input(12))
			counterBR += 1

		if int(gpio.input(7) != int(buttonFL)):
			buttonFL = int(gpio.input(7))
			counterFL = counterFL+1
		
		if counterFL >= ticks-1:
			pwm1.stop()
			
		if counterBR >= ticks:
			pwm2.stop()


		if counterBR >=ticks-1 and counterFL >= ticks-1 :	
			gameover()
			print("Thanks for Playing")
			#file1.close()
			break

def left(ticks):
	init()


	counterBR = np.uint64(0)
	counterFL = np.uint64(0)

	buttonBR = int(0)
	buttonFL = int(0)

	# Initialize pwm signal to control motor
	pwm1 = gpio.PWM(33,50)
	pwm2 = gpio.PWM(37,50)
	val = 95
	pwm1.start(val)
	pwm2.start(val)
	time.sleep(0.1)

	for i in range (0,10000000):
		print("counterBR = ",counterBR,"counterFL = ",counterFL,"BR state: ", gpio.input(12),"FL state: ", gpio.input(7))
		file1.write(str(gpio.input(12))+str(gpio.input(7))+"\n")

		if int(gpio.input(12) != int(buttonBR)):
			buttonBR = int(gpio.input(12))
			counterBR += 1

		if int(gpio.input(7) != int(buttonFL)):
			buttonFL = int(gpio.input(7))
			counterFL = counterFL+1
		
		if counterFL >= ticks-1:
			pwm1.stop()
			pwm2.stop()
			break
			
		#if counterBR >= ticks:
			#pwm2.stop()


		#if counterBR >=ticks-1 and counterFL >= ticks-1 :	
			#gameover()
			#print("Thanks for Playing")
			#file1.close()
			#break

def right(ticks):
	init()


	counterBR = np.uint64(0)
	counterFL = np.uint64(0)

	buttonBR = int(0)
	buttonFL = int(0)

	# Initialize pwm signal to control motor
	pwm1 = gpio.PWM(31,50)
	pwm2 = gpio.PWM(35,50)
	val = 95
	pwm1.start(val)
	pwm2.start(val)
	time.sleep(0.1)

	for i in range (0,10000000):
		print("counterBR = ",counterBR,"counterFL = ",counterFL,"BR state: ", gpio.input(12),"FL state: ", gpio.input(7))
		file1.write(str(gpio.input(12))+str(gpio.input(7))+"\n")

		if int(gpio.input(12) != int(buttonBR)):
			buttonBR = int(gpio.input(12))
			counterBR += 1

		if int(gpio.input(7) != int(buttonFL)):
			buttonFL = int(gpio.input(7))
			counterFL = counterFL+1
		
		if counterFL >= ticks-1:
			pwm1.stop()
			pwm2.stop()
			
		#if counterBR >= ticks:
			#pwm2.stop()


		#if counterBR >=ticks-1 and counterFL >= ticks-1 :	
			#gameover()
			#print("Thanks for Playing")
			#file1.close()
			break

def key_input(event):
	init()
	print("Key: " ,event)
	key_press = event
#	tf=1
	if key_press.lower() == 'w':
		x = input('Enter distance in Meters:')
		x = float(x)
		ticks= (1/(3.14*2*0.0325))*x*960
		forward(ticks)
	elif key_press.lower() == 's':
		x = input('Enter distance in Meters:')
		x = float(x)
		ticks= (1/(3.14*2*0.0325))*x*960
		reverse(ticks)
	elif key_press.lower() == 'a':
		x = input('Enter Angle in degrees:')
		x = float(x)
		ticks= x*5.85
		left(ticks)
	elif key_press.lower() == 'd':
		x = input('Enter Angle in degrees:')
		x = float(x)
		ticks= x*5.85
		right(ticks)
	else:
		print("Invalid")
		#gameover()
		#gpio.cleanup()
while True:
#	forward(rev)
	key_press = input("Select driving mode:")
	if key_press =='p':
		file1.close()
		break
	key_input(key_press)
