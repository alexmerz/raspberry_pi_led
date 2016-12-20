# blink a single LED
# see https://www.youtube.com/watch?v=CgGqIvRXH3U&lc=z12qjj2oiljpgxqan04ccrfw5yyxtd3x1iw

import RPi.GPIO as GPIO
import time

led_pin = 27

try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led_pin, GPIO.OUT)
	while True:
		GPIO.output(led_pin, True)
		time.sleep(1.0)
		GPIO.output(led_pin, False)
		time.sleep(1.0)
		
except KeyboardInterrupt:
	pass
	
GPIO.cleanup()