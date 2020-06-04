
# Imports
import RPi.GPIO as GPIO
import time
import requests

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)

# Turn off GPIO warnings
GPIO.setwarnings(False)

PIR = 17

# Set GPIO pin as input
GPIO.setup(PIR, GPIO.IN)

# Variables to hold the current and last states
currentstate = 0
previousstate = 0
Trig = 18
ECHO = 24
buzzer = 3
LED = 2

GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)

try:
	print("Lets Begin.....")

	# Loop until PIR output is 0
	while GPIO.input(PIR) == 1:

		currentstate = 0

	print("*****Ready*****")


	while True:

		# Read PIR state
		currentstate = GPIO.input(PIR)

		GPIO.output(Trig, False)
		time.sleep(1)
		GPIO.output(Trig, True)
		time.sleep(0.01)
		GPIO.output(Trig, False)


		if currentstate == 1 and previousstate == 0:

			while GPIO.input(ECHO) ==0:
				pulse_start = time.time()
			while GPIO.input(ECHO) == 1:
				pulse_end = time.time()

			pulse_duration = pulse_end-pulse_start
			distance = pulse_duration*11150
			distance = round(distance,2)
			print("Motion Detected: your dog is near the bowl")
			time.sleep(2)

			if (distance > 10):
				GPIO.output(LED, GPIO.HIGH)
				print("Food is not there")
				r = requests.post('https://maker.ifttt.com/trigger/motion_detected/with/key/cuoIT5m7aqSPf96bTvDxFI', params = {"value1":"none","value2":"none","value3":"none"})
				previousstate =1
				GPIO.output(LED, GPIO.LOW)

			else:
				print("Food is already there")
				r = requests.post('https://maker.ifttt.com/trigger/full_bowl/with/key/cuoIT5m7aqSPf96bTvDxFI', params={"value1":"none","value2":"none","value3":"none"})
				GPIO.output(LED, GPIO.LOW)

			previousstate = 1

			#Wait 60 seconds before looping again
			print("Waiting 60 seconds")
			time.sleep(60)

		# If the PIR has returned to ready state
		elif currentstate == 0 and previousstate == 1:

			print("*****Ready*****")
			previousstate = 0

		# Wait for 10 milliseconds
		time.sleep(0.01)

except KeyboardInterrupt:
	print("    Quit")

	# Reset GPIO settings
	GPIO.cleanup()
