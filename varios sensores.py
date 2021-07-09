import time
import board
import busio
import digitalio
import adafruit_vl53l0x
from adafruit_vl53l0x import VL53L0X
import RPi.GPIO as GPIO

i2c = board.I2C()
GPIO.setmode(GPIO.BCM)

xshut1 = GPIO.setup(17, GPIO.OUT)
xshut1 = GPIO.setup(26, GPIO.OUT)
xshut2 = GPIO.setup(27, GPIO.OUT)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.LOW)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26,GPIO.LOW)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27,GPIO.LOW)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.LOW)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26,GPIO.LOW)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27,GPIO.HIGH)

i2c = busio.I2C(board.SCL, board.SDA)
vl53De = adafruit_vl53l0x.VL53L0X(i2c)
vl53De = VL53L0X(i2c)
vl53De.set_address(0x30)
print("sensor 1: ", vl53De.range)

###############sensor2

GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.HIGH)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26,GPIO.LOW)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27,GPIO.HIGH)


i2c = busio.I2C(board.SCL, board.SDA)
vl53S1 = VL53L0X(i2c)
vl53S1.set_address(0x31)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.HIGH)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26,GPIO.HIGH)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27,GPIO.HIGH)

i2c = busio.I2C(board.SCL, board.SDA)
vl53Do = VL53L0X(i2c)
vl53Do.set_address(0x32)
    
print(vl53S1.range)    
print(vl53De.range)
print(vl53Do.range)

def detect_range(count=5):
   
    while True:
        
        print(vl53De.range)
        print(vl53S1.range)
        print(vl53De.range)
        
detect_range()
print(
    "Multiple VL53L0X sensors' addresses are assigned properly\n"
    "execute detect_range() to read each sensors range readings"
)



