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


GPIO.setup(26, GPIO.IN) # señal entrada
GPIO.setup(11, GPIO.OUT) #señal apagado entrada
GPIO.setup(13, GPIO.IN) #persona en entrada

GPIO.setup(6, GPIO.OUT) #señal apagado salida
GPIO.setup(5, GPIO.IN) #señal salida(arduino2)
GPIO.setup(19, GPIO.IN)#persona salida

GPIO.setup(10, GPIO.OUT) #apagado señal oportunidad
GPIO.setup(9, GPIO.IN) #señal oportunidad
oportunidad = GPIO.input(9)

GPIO.setup(6, GPIO.OUT) 
GPIO.output(6,GPIO.HIGH)
time.sleep(0.5)
GPIO.setup(6, GPIO.OUT) 
GPIO.output(6,GPIO.LOW)
señalSalida = GPIO.input(5)
personaSalida = GPIO.input(19)

GPIO.setup(11, GPIO.OUT)
GPIO.output(11,GPIO.HIGH)
time.sleep(0.5)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11,GPIO.LOW)
personaEntrada = GPIO.input(13)
señalEntrada = GPIO.input(26)

def PostOport():
    url= 'http://143.198.132.112/smarthh/novaspost_oportunidades.php'
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
        response = requests.post('http://143.198.132.112/smarthh/novaspost_oportunidades.php',data = {'foo2':'bar2'})
        #print (response.text)
    else:
        pass
        #print ('no fue posible')
    
def PostEfect():
    url= 'http://143.198.132.112/smarthh/novaspost_efectivo.php'
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
        response = requests.post('http://143.198.132.112/smarthh/novaspost_efectivo.php',data = {'foo2':'bar2'})
        #print (response.text)
    else:
        pass
        #print ('no fue posible entrar')

flag = 1
print("Iniciando...")
while True:
    
    GPIO.setup(26, GPIO.IN)
    señalEntrada = GPIO.input(26)
    GPIO.setup(5, GPIO.IN)
    señalSalida = GPIO.input(5)
    #print("señal entrada:")
    #print(señalEntrada)
    #print("señal salida:")
    #print(señalSalida)
    
    if(señalEntrada == 1):
        GPIO.setup(13, GPIO.IN) 
        personaEntrada = GPIO.input(13)
        GPIO.setup(19, GPIO.IN)
        personaSalida = GPIO.input(19)
        oportunidad = GPIO.input(9)
        #print("alguien en la puerta")
        #print(personaEntrada)
        if(oportunidad == 1):
            flag = 1;
        else:
            flag = 0;
        while(personaEntrada == 1 or personaSalida == 1):
            personaEntrada = GPIO.input(13)
            personaSalida = GPIO.input(19)
            #print("alguien en la puerta")
            #print(personaEntrada)
            
        if(flag ==1):
            GPIO.output(10,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(10,GPIO.LOW)
            time.sleep(0.2)
            PostOport()
            PostEfect()
                #realizar peticion http oportunidad con lavado de manos
        else:
            GPIO.output(10,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(10,GPIO.LOW)
            time.sleep(0.2)
            PostOport()
            #realizar peticion http oportunidad sin lavado de manos

        while(señalEntrada == 1 or señalSalida == 1):
            GPIO.setup(26, GPIO.IN)
            señalEntrada = GPIO.input(26)
            GPIO.setup(5, GPIO.IN)
            señalSalida = GPIO.input(5)
            GPIO.setup(6, GPIO.OUT)    
            GPIO.output(6,GPIO.HIGH)
            time.sleep(0.4)
            GPIO.setup(6, GPIO.OUT)
            GPIO.output(6,GPIO.LOW)
            time.sleep(0.2)
            GPIO.setup(11, GPIO.OUT)    
            GPIO.output(11,GPIO.HIGH)
            time.sleep(0.4)
            GPIO.setup(11, GPIO.OUT)
            GPIO.output(11,GPIO.LOW)
            time.sleep(0.2)
            #print("apagando... entrada")
            
      
        GPIO.setup(6, GPIO.OUT)
        GPIO.output(6,GPIO.LOW)
        GPIO.setup(11, GPIO.OUT)
        GPIO.output(11,GPIO.LOW)
        #print("señal apagada")

    elif (señalSalida == 1):

        GPIO.setup(13, GPIO.IN) 
        personaEntrada = GPIO.input(13)
        GPIO.setup(19, GPIO.IN)
        personaSalida = GPIO.input(19)
        while(personaEntrada == 1 or personaSalida == 1):
            personaEntrada = GPIO.input(13)
            personaSalida = GPIO.input(19)
            #print("alguien en la puerta")
            #print(personaEntrada)
            
        while(señalEntrada == 1 or señalSalida == 1):
            GPIO.setup(26, GPIO.IN)
            señalEntrada = GPIO.input(26)
            GPIO.setup(5, GPIO.IN)
            señalSalida = GPIO.input(5)
            GPIO.setup(6, GPIO.OUT)    
            GPIO.output(6,GPIO.HIGH)
            time.sleep(0.4)
            GPIO.setup(6, GPIO.OUT)
            GPIO.output(6,GPIO.LOW)
            time.sleep(0.2)
            GPIO.setup(11, GPIO.OUT)    
            GPIO.output(11,GPIO.HIGH)
            time.sleep(0.4)
            GPIO.setup(11, GPIO.OUT)
            GPIO.output(11,GPIO.LOW)
            time.sleep(0.2)
            #print("apagando... salida")

        GPIO.setup(6, GPIO.OUT)
        GPIO.output(6,GPIO.LOW)
        GPIO.setup(11, GPIO.OUT)
        GPIO.output(11,GPIO.LOW)
        #print("señal apagada")
        #print("saliendo")

    else:
        
        GPIO.output(6,GPIO.LOW)
        GPIO.setup(11, GPIO.OUT)
        GPIO.output(11,GPIO.LOW)
        #print("no hay nadie")
 


