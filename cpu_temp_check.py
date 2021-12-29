#!/usr/bin/env python3
########################################################################
# Filename    : 
# Description : 
# Author      : 
# modification: 
########################################################################

from time import sleep, strftime
from datetime import datetime


# the most important function ever!
def get_time_now(): # get system time
    return datetime.now().strftime(' %H:%M:%S')


def get_cpu_temp(): # get the CPU temperature " /sys/class/thermal/thermal_zone()/temp "
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    print("CPU temp: {:.2f}".format( float(cpu)/1000 )+" Celsius" + get_time_now() )

    return '{:.2f}'.format( float(cpu)/1000 ) + ' C'

def loop():
    while True:
        get_cpu_temp()
        sleep(3)

def destroy():
    GPIO.cleanup() # Relase GPIO resources


if __name__ == '__main__':
    print('Program is starting ..')
    
    try:
        loop()
    except KeyboardInterrupt:   # Press control-c to end the program
        destroy()