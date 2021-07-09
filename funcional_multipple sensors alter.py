import time
import board
import digitalio 
from adafruit_vl53l0x import VL53L0X
import RPi.GPIO as GPIO

# declare the singleton variable for the default I2C bus
i2c = board.I2C()
GPIO.setmode(GPIO.BCM)


# declare the digital output pins connected to the "SHDN" pin on each VL53L0X sensor

    #DigitalInOut(board.D7),
GPIO.setup(17, GPIO.OUT)
    #DigitalInOut(board.D9),
GPIO.setup(27, GPIO.OUT)

vl53 = []

    
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.LOW)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27,GPIO.HIGH)
 
vl53.insert(0, VL53L0X(i2c)) 
vl53[0].set_address(0x30)
time.sleep(1.0)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.HIGH)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27,GPIO.LOW)
 
vl53.insert(1, VL53L0X(i2c)) 
vl53[1].set_address(0x31)    


 

GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.HIGH)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27,GPIO.HIGH)



def detect_range(count=5):
    """ take count=5 samples """
    print("funcion")
    count = 1
    while True:
        GPIO.setup(17, GPIO.OUT)
        GPIO.output(17,GPIO.LOW)
        GPIO.setup(27, GPIO.OUT)
        GPIO.output(27,GPIO.HIGH)
        print("Sensor {} Range: {}mm".format(vl53[1].range)) 
        time.sleep(1.0)
        count += 1
        print(count)


print(
    "Multiple VL53L0X sensors' addresses are assigned properly\n"
    "execute detect_range() to read each sensors range readings"
)

detect_range()

