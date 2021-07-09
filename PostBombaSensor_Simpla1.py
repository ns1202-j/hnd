import time
import requests
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

def PostOport():
    
    query = {'lat':'45','lon':'180'}
    #response = requests.get('https://192.168.11.41/nova/consulta1.php', params = query)
    #response = requests.get('https://xkcd.com/353/')
    #response = requests.get('http://192.168.11.41/nova/consulta1.php')
    #print (response.text)
    response = requests.post('http://192.168.11.41/nova/novaspost_oportunidades.php',data = {'foo2':'bar2'})
    print (response.text)

def PostEfect():
    
    query = {'lat':'45','lon':'180'}
    #response = requests.get('https://192.168.11.41/nova/consulta1.php', params = query)
    #response = requests.get('https://xkcd.com/353/')
    #response = requests.get('http://192.168.11.41/nova/consulta1.php')
    #print (response.text)

    response = requests.post('http://192.168.11.41/nova/novaspost_efectivo.php',data = {'foo2':'bar2'})

    print (response.text)

    
i = 0
j = 0
flag = 1
flag1 = 1
flagPump = 1
flagOp = 1
while True:

    valHand = HandSensor()
    valOp = OpSensor()
    
    print ("sensor de manos: ", valHand)
    print ("sensor para personas: ", valOp)
   
    
    if valHand > 120:
        
        GPIO.setup(15, GPIO.OUT)
        GPIO.output(15,GPIO.HIGH)
        flag = 1
        flagPump = 1
        
            
    elif valHand < 120 and valHand != 0:

        if flagPump == 1:

            GPIO.setup(15, GPIO.OUT)
            GPIO.output(15,GPIO.LOW)
            time.sleep(0.7)
            GPIO.setup(15, GPIO.OUT)
            GPIO.output(15,GPIO.HIGH)
            flagPump = 0

        else:
                
            print (i)
        
        if flag == 1:

            flagOp = 0
            flag = 0
            
            
                
        else:
            print (i)
            
    else:
        print("error")
        

    if valOp > 600:
        flag1 = 1
                
    else:
        
        if flag1 == 1:
            j = j + 1
            flag1 = 0

            if flagOp == 0:

                i = i + 1
                PostEfect()
                flagOp = 1

            print ("valor de j: ")
            PostOport()
            print (j)
            
        else:
            print ("valor de j: ")
            print (j)
        
       
 
  
