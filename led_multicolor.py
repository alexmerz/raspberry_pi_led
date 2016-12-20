# blink a multi-color LED using PWM
# see https://www.youtube.com/watch?v=CgGqIvRXH3U&lc=z12qjj2oiljpgxqan04ccrfw5yyxtd3x1iw

import RPi.GPIO as GPIO
import time

led_red = 27
led_green = 22
led_blue = 23

try:
	GPIO.setmode(GPIO.BCM)
	
	GPIO.setup(led_red, GPIO.OUT)
	GPIO.setup(led_green, GPIO.OUT)
	GPIO.setup(led_blue, GPIO.OUT)
	
	pwm_red = GPIO.PWM(led_red, 100)
	pwm_green = GPIO.PWM(led_green, 100)
	pwm_blue = GPIO.PWM(led_blue, 100)
	
	pwm_red.start(0)
	pwm_green.start(0)
	pwm_blue.start(0)
	
	while True:
		for dc in range(0, 101, 2):
			pwm_red.ChangeDutyCycle(dc)
			pwm_green.ChangeDutyCycle(0)
			pwm_blue.ChangeDutyCycle(0)
			time.sleep(0.02)
		for dc in range(0, 101, 2):
			pwm_red.ChangeDutyCycle(0)
			pwm_green.ChangeDutyCycle(dc)
			pwm_blue.ChangeDutyCycle(0)
			time.sleep(0.02)
		for dc in range(0, 101, 2):
			pwm_red.ChangeDutyCycle(0)
			pwm_green.ChangeDutyCycle(0)
			pwm_blue.ChangeDutyCycle(dc)
			time.sleep(0.02)
		
except KeyboardInterrupt:
	pass

pwm.stop()
GPIO.cleanup()