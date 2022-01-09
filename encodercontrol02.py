import RPi.GPIO as gpio
import time
import numpy as np



radius = 0.0325
dist = float(input(" Please enter distance:"))

revs =( 4701.2 * dist )

print(revs)

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(31, gpio.OUT) #IN1
    gpio.setup(33, gpio.OUT) #IN1
    gpio.setup(35, gpio.OUT) #IN1
    gpio.setup(37, gpio.OUT) #IN1
    
    gpio.setup(7,gpio.IN,pull_up_down = gpio.PUD_UP)
    gpio.setup(12,gpio.IN,pull_up_down = gpio.PUD_UP)

def gameover():
    # Set all pins LOW
    gpio.output(31, False)
    gpio.output(33, False)
    gpio.output(35, False)
    gpio.output(37, False)

    gpio.cleanup()

init()

counterBR = np.uint64(0)
counterFL = np.uint64(0)
buttonBR = int(0)
buttonFL = int(0)

pwm1 = gpio.PWM(31,50)
pwm2 = gpio.PWM(37,50)
val = 60
pwm2.start(val)
pwm1.start(val)
time.sleep(0.1)




state_br = open("br_Statees2.txt", 'w')
state_fl = open( "fl_Statees2.txt", 'w')

for i in range(0,200000):
	print("counterBR:", counterBR,"counterFL:",counterFL, 'BR state', gpio.input(12),'FL state',gpio.input(7))


	state_br.write(str(buttonBR)+str("\n"))
	state_fl.write(str(buttonFL)+str('\n'))



	if int(gpio.input(12)) != int(buttonBR):
		buttonBR = int(gpio.input(12))
		counterBR +=1
	
	if int(gpio.input(7)) != int(buttonFL):
		buttonFL = int(gpio.input(7))
		counterFL+=1


	if counterBR >= revs:
		pwm1.stop()

	if counterFL >= revs:
		pwm2.stop()

	if counterBR >=revs and counterFL >= revs:

		gameover()
		print('Thanks for playing')
		break
