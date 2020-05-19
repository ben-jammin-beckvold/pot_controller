'''
	Raspberry Pi Temperature Controlled Power
'''
import os
import time

import RPi.GPIO as GPIO
import datetime

import signal
import sys

def signal_handler(sig, frame):
  print('SIGINT: exiting')
  GPIO.output(power_switch, GPIO.LOW)
  sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BCM) # which pin reference
GPIO.setwarnings(False)

#define actuator GPIOs
power_switch = 27
#initialize GPIO status variables
power_status = 0
# Define switch as output
GPIO.setup(power_switch, GPIO.OUT)   
# turn switch OFF 
GPIO.output(power_switch, GPIO.LOW)

# DS18B20 setup
DS18B20 = '/sys/bus/w1/devices/28-01193a92da65/w1_slave'   # point to the address
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

def read_temp_C():
  f = open(DS18B20, "r")
  data = f.read()                                   # read the device details
  f.close()

  (discard, sep, reading) = data.partition(' t=')
  
  return float(reading) / 1000.0
	
def make_yogurt():
  # temps in C for ideal yogurt making
  high_limit = 46
  low_limit = 44

  tempc = read_temp_C()
  if (tempc > high_limit):
    GPIO.output(power_switch, GPIO.LOW)
    print("upper limit")
  if (tempc < low_limit):
    GPIO.output(power_switch, GPIO.HIGH)
    print("lower limit")

  print(tempc, "C \n")
  time.sleep(10)

if __name__ == "__main__":
  while True:
   make_yogurt()
