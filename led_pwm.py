# blink a multi-color LED using PWM
# see https://www.youtube.com/watch?v=CgGqIvRXH3U&lc=z12qjj2oiljpgxqan04ccrfw5yyxtd3x1iw

import RPi.GPIO as GPIO
import time

led_pin = 27

try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led_pin, GPIO.OUT)
	
	pwm = GPIO.PWM(led_pin, 100)
	pwm.start(0)
	
	while True:
		for dc in range(0, 101, 2):
			pwm.ChangeDutyCycle(dc)
			time.sleep(0.02)
		for dc in range(100, -1, -2):
			pwm.ChangeDutyCycle(dc)
			time.sleep(0.02)
		
except KeyboardInterrupt:
	pass

pwm.stop()
GPIO.cleanup()