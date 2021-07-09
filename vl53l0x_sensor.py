import time

import board
import busio
import RPi.GPIO as GPIO

import adafruit_vl53l0x
 
GPIO.setup(17, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.LOW)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26,GPIO.HIGH)

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
i = 1
flag = 1
while True:
    if flag == 1:
        GPIO.setup(17, GPIO.OUT)
        GPIO.output(17,GPIO.LOW)
        GPIO.setup(26, GPIO.OUT)
        GPIO.output(26,GPIO.HIGH)
        i2c = busio.I2C(board.SCL, board.SDA)
        vl53 = adafruit_vl53l0x.VL53L0X(i2c)    
        print("sensor1:")
        print("Range: {0}mm".format(vl53.range))
        flag = 0
    
    else:
        GPIO.setup(17, GPIO.OUT)
        GPIO.output(17,GPIO.HIGH)
        GPIO.setup(26, GPIO.OUT)
        GPIO.output(26,GPIO.LOW)
        i2c = busio.I2C(board.SCL, board.SDA)
        vl53 = adafruit_vl53l0x.VL53L0X(i2c)    
        print("sensor2:")
        print("Range: {0}mm".format(vl53.range))
        flag = 1
        
    time.sleep(1.0)
    i += 1
    print(i)
 

