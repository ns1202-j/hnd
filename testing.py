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
GPIO.setup(11, GPIO.OUT) #señal apagado salida(arduino1)
GPIO.setup(5, GPIO.IN) #señal salida(arduino2)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)


GPIO.setup(4, GPIO.OUT)
GPIO.output(4,GPIO.HIGH)
señalEntrada = GPIO.input(5)
GPIO.output(6,GPIO.LOW)
GPIO.output(11,GPIO.LOW)
GPIO.output(11,GPIO.LOW)


while True:
    
 
    print("esperando apagado...")
    print("señal: ")
    print(señalEntrada)
    
    time.sleep(5.0)

    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6,GPIO.HIGH) #apagando señal de salida
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11,GPIO.HIGH) #apagando señal de entrada
    señalEntrada = GPIO.input(5)
    print("señal: ")
    print(señalEntrada) 
    print("apagado")
    time.sleep(5.0)

    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6,GPIO.LOW) #apagando señal de salida
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11,GPIO.LOW) #apagando señal de entrada
    

    
time.sleep(0.5)
