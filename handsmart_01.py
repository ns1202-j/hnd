import time
import requests
import board
import busio
import asyncio
import urllib.request
import RPi.GPIO as GPIO
import adafruit_vl53l0x
from adafruit_vl53l0x import VL53L0X
import threading
from threading import Thread


GPIO.setup(4, GPIO.OUT)


GPIO.setup(4, GPIO.OUT)
GPIO.output(4,GPIO.HIGH)

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
i = 1
flag = 1

while True:
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        vl53 = adafruit_vl53l0x.VL53L0X(i2c)    
        print("sensor1:")
        print("Range: {0}mm".format(vl53.range))
        manos = vl53.range
        
        if manos <= 200:
              
            GPIO.setup(4, GPIO.OUT)
            GPIO.output(4,GPIO.HIGH)
                
               
    
        else:

            pass
        
    except OSError:

        pass
    

