import RPI.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIN_NUM = 26
CHECK_ON = 30
GPIO.setup(PIN_NUM,GPIO.IN)

try:
    while True:
        if GPIO.input(PIN_NUM)>=CHECK_ON:
            print("와이리 시끄럽노")
            
