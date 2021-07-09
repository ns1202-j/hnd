import time

import board
import busio
import RPi.GPIO as GPIO
import adafruit_vl53l0x
numSensorManos = 17
numSensorOp = 26
 
GPIO.setup(17, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.setup(numSensorManos, GPIO.OUT)
GPIO.output(numSensorManos,GPIO.HIGH)
GPIO.setup(numSensorOp, GPIO.OUT)
GPIO.output(numSensorOp,GPIO.LOW)

GPIO.setup(15, GPIO.OUT)
GPIO.output(15,GPIO.HIGH)

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

def HandSensor():
    GPIO.setup(numSensorOp, GPIO.OUT)
    GPIO.output(numSensorOp,GPIO.LOW)
    GPIO.setup(numSensorManos, GPIO.OUT)
    GPIO.output(numSensorManos,GPIO.HIGH)
    i2c = busio.I2C(board.SCL, board.SDA)
    vl53 = adafruit_vl53l0x.VL53L0X(i2c)
    vH = vl53.range
    GPIO.setup(numSensorManos, GPIO.OUT)
    GPIO.output(numSensorManos,GPIO.LOW)
    GPIO.setup(numSensorOp, GPIO.OUT)
    GPIO.output(numSensorOp,GPIO.LOW)

    return (vH)


def OpSensor():
    GPIO.setup(numSensorManos, GPIO.OUT)
    GPIO.output(numSensorManos,GPIO.LOW)
    GPIO.setup(numSensorOp, GPIO.OUT)
    GPIO.output(numSensorOp,GPIO.HIGH)
    i2c = busio.I2C(board.SCL, board.SDA)
    vl53 = adafruit_vl53l0x.VL53L0X(i2c)
    vO = vl53.range
    GPIO.setup(numSensorManos, GPIO.OUT)
    GPIO.output(numSensorManos,GPIO.LOW)
    GPIO.setup(numSensorOp, GPIO.OUT)
    GPIO.output(numSensorOp,GPIO.LOW)
  
    return (vO)

i = 0
j = 0
flag = 1
flag1 = 1
while True:

    valHand = HandSensor()
    valOp = OpSensor()
    
    print (valHand)
    print (valOp)
   
    
    if valHand > 120:
        
        GPIO.setup(15, GPIO.OUT)
        GPIO.output(15,GPIO.HIGH)
        flag = 1
        
            
    else:
        
        GPIO.setup(15, GPIO.OUT)
        GPIO.output(15,GPIO.LOW)
        if flag == 1:
            i = i + 1
            flag = 0
            print (i)
        else:
            print (i)
        

    if valOp > 600:
        flag1 = 1
                
    else:
        
        if flag1 == 1:
            j = j + 1
            flag1 = 0
            print ("valor de j: ")
            print (j)
        else:
            print ("valor de j: ")
            print (j)
        
  

 
