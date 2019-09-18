# -*- coding: utf-8 -*-                #通过声明可以在程序中书写中文
import RPi.GPIO as gpio
import time
import sys


pin = 18

gpio.setmode(gpio.BOARD)
gpio.setup(pin, gpio.OUT)

#频率设置为400Hz
p = gpio.PWM(pin, 500)
p.start(0)

dc=75
p.ChangeDutyCycle(dc)
time.sleep(2)
dc=80
p.ChangeDutyCycle(dc)
time.sleep(2)

p.stop()
gpio.cleanup()