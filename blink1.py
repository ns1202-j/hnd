#blink.py
import time
import board
import busio
import adafruit_vl53l0x
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
i = 1

while i < 10 :
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(15, GPIO.OUT)
        GPIO.output(15,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(15,GPIO.LOW)
        time.sleep(1)
        print(i)
        GPIO.output(15,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(15,GPIO.LOW)
        time.sleep(1)
        i += 1

print(i)
