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
numSensorManos = 17
numSensorOp = 26
numSensorEf = 27

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.setup(15, GPIO.OUT)
GPIO.output(15,GPIO.HIGH)

GPIO.setup(numSensorManos, GPIO.OUT)
GPIO.output(numSensorManos,GPIO.LOW)
GPIO.setup(numSensorOp, GPIO.OUT)
GPIO.output(numSensorOp,GPIO.LOW)
GPIO.setup(numSensorEf, GPIO.OUT)
GPIO.output(numSensorEf,GPIO.LOW)

GPIO.setup(numSensorManos, GPIO.OUT)
GPIO.output(numSensorManos,GPIO.HIGH)
GPIO.setup(numSensorOp, GPIO.OUT)
GPIO.output(numSensorOp,GPIO.LOW)
GPIO.setup(numSensorEf, GPIO.OUT)
GPIO.output(numSensorEf,GPIO.LOW)

i2c = busio.I2C(board.SCL, board.SDA)
vl53Hands = adafruit_vl53l0x.VL53L0X(i2c)
vl53Hands = VL53L0X(i2c)
vl53Hands.set_address(0x30)

###############sensor2
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(numSensorManos, GPIO.OUT)
GPIO.output(numSensorManos,GPIO.HIGH)
GPIO.setup(numSensorOp, GPIO.OUT)
GPIO.output(numSensorOp,GPIO.HIGH)
GPIO.setup(numSensorEf, GPIO.OUT)
GPIO.output(numSensorEf,GPIO.LOW)

i2c = busio.I2C(board.SCL, board.SDA)
vl53Op = VL53L0X(i2c)
vl53Op.set_address(0x31)

###############sensor3
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(numSensorManos, GPIO.OUT)
GPIO.output(numSensorManos,GPIO.HIGH)
GPIO.setup(numSensorOp, GPIO.OUT)
GPIO.output(numSensorOp,GPIO.HIGH)
GPIO.setup(numSensorEf, GPIO.OUT)
GPIO.output(numSensorEf,GPIO.HIGH)

i2c = busio.I2C(board.SCL, board.SDA)
vl53Salida = VL53L0X(i2c)
vl53Salida.set_address(0x32)

def inicializar():
    numSensorManos = 17
    numSensorOp = 26
    numSensorEf = 27

    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    GPIO.setup(15, GPIO.OUT)
    GPIO.output(15,GPIO.HIGH)

    GPIO.setup(numSensorManos, GPIO.OUT)
    GPIO.output(numSensorManos,GPIO.LOW)
    GPIO.setup(numSensorOp, GPIO.OUT)
    GPIO.output(numSensorOp,GPIO.LOW)
    GPIO.setup(numSensorEf, GPIO.OUT)
    GPIO.output(numSensorEf,GPIO.LOW)

    GPIO.setup(numSensorManos, GPIO.OUT)
    GPIO.output(numSensorManos,GPIO.HIGH)
    GPIO.setup(numSensorOp, GPIO.OUT)
    GPIO.output(numSensorOp,GPIO.LOW)
    GPIO.setup(numSensorEf, GPIO.OUT)
    GPIO.output(numSensorEf,GPIO.LOW)

    i2c = busio.I2C(board.SCL, board.SDA)
    vl53Hands = adafruit_vl53l0x.VL53L0X(i2c)
    vl53Hands = VL53L0X(i2c)
    vl53Hands.set_address(0x30)

    ###############sensor2
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(numSensorManos, GPIO.OUT)
    GPIO.output(numSensorManos,GPIO.HIGH)
    GPIO.setup(numSensorOp, GPIO.OUT)
    GPIO.output(numSensorOp,GPIO.HIGH)
    GPIO.setup(numSensorEf, GPIO.OUT)
    GPIO.output(numSensorEf,GPIO.LOW)

    i2c = busio.I2C(board.SCL, board.SDA)
    vl53Op = VL53L0X(i2c)
    vl53Op.set_address(0x31)

    ###############sensor3
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(numSensorManos, GPIO.OUT)
    GPIO.output(numSensorManos,GPIO.HIGH)
    GPIO.setup(numSensorOp, GPIO.OUT)
    GPIO.output(numSensorOp,GPIO.HIGH)
    GPIO.setup(numSensorEf, GPIO.OUT)
    GPIO.output(numSensorEf,GPIO.HIGH)

    i2c = busio.I2C(board.SCL, board.SDA)
    vl53Salida = VL53L0X(i2c)
    vl53Salida.set_address(0x32)
    

def HandSensor():
    
    try:
        vH = vl53Hands.range
        return (vH)
    except OSError:
        
        #print ('estatus dañado sensor salida')
        inicializar()

def OpSensor():

    try:
        vO = vl53Op.range
        return (vO)
    except OSError:
        #print ('estatus dañado sensor salida')
        inicializar()  

def EfSensor():
 
    try:
        vE = vl53Salida.range
        return (vE)
    except OSError:
        #print ('estatus dañado sensor salida')
        inicializar()
   


def PostOport():
    url= 'http://192.168.11.41/nova/novaspost_oportunidades.php'
    status_code = 200
    try:
        status_code = requests.get(url, timeout = 10)
        
    except requests.exceptions.ConnectTimeout:
        #print ('time out')
        status_code = 3
    except requests.exceptions.ConnectionError:
        #print ('error de conexion')
        status_code = 3
        
    if status_code == 200:
        query = {'lat':'45','lon':'180'}
        response = requests.post('http://192.168.11.41/nova/novaspost_oportunidades.php',data = {'foo2':'bar2'})
        #print (response.text)
    else:
        pass
        #print ('no fue posible')

def PostEfect():
    url= 'http://192.168.11.41/nova/novaspost_efectivo.php'
    status_code = 200
    try:
        status_code = requests.get(url, timeout = 5)
        status_code.raise_for_status()
    except requests.exceptions.ConnectTimeout:
        #print ('time out')
        status_code = 3
    except requests.exceptions.ConnectionError:
       # print ('error de conexion')
        status_code = 3
    
    if status_code == 200:
        query = {'lat':'45','lon':'180'}
        response = requests.post('http://192.168.11.41/nova/novaspost_efectivo.php',data = {'foo2':'bar2'})
        #print (response.text)
    else:
        pass
        #print ('no fue posible entrar')

i = 0
j = 0
flag = 1
flag1 = 1
flagPump = 1
flagOp = 1
result = 0
#print("ready")
while True:

    valHand = HandSensor()
    valOp = OpSensor()
    valEf = EfSensor()
    #print("sensor salida: ", valEf)
    #print("sensor manos: ", valHand)

    try:

        if(valOp < 1000 and valEf >1000):
            var = 1
          #  print("Entrando, valor de sensor: ", valOp)

        elif(valOp <= 1000 and valEf <= 1000):
            var = 2
           # print("en la puerta")

        elif(valOp > 1000 and valEf > 1000):
            var = 3
            #print("no hay nadie")
        else:
            #print("saliendo")
            var = 0

    except TypeError:
        pass
        #print("error de tipo type")
    try:
            
        if valHand > 220:

            GPIO.setup(15, GPIO.OUT)
            GPIO.output(15,GPIO.HIGH)
            flag = 1
            flagPump = 1


        elif valHand <= 220 and valHand != 0:

            if flagPump == 1:

                GPIO.setup(15, GPIO.OUT)
                GPIO.output(15,GPIO.LOW)
                time.sleep(0.7)
                GPIO.setup(15, GPIO.OUT)
                GPIO.output(15,GPIO.HIGH)
                flagPump = 0

            else:
                pass

             #   print (i)

            if flag == 1:

                flagOp = 0
                flag = 0



            else:
                pass
              #  print (i)

        else:
            pass
            #print("error")
        
    except TypeError:
        pass
        #print("error de tipo type")


    if var == 0:
        flag1 = 1
        time.sleep(1.5)

    elif var == 2:
        flag1 = 1
        
    elif (var == 3):
        #print("no hay nadie")
        flag1 = 1
        
    else:

        if flag1 == 1:
            j = j + 1
            flag1 = 0

            if flagOp == 0:

                i = i + 1
                PostEfect()
                flagOp = 1
                
            PostOport()
         #   print (j)
            time.sleep(0.5)

        else:
            pass
          #  print (j)

