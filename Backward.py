# -*- coding: utf-8 -*-                #通过声明可以在程序中书写中文
import RPi.GPIO as gpio
import time
import sys


pin1 = 18
pin2 = 22

gpio.setmode(gpio.BOARD)
gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.OUT)

l = gpio.PWM(pin1, 500)     #频率设置为500Hz
r = gpio.PWM(pin2, 500)
l.start(0)
r.start(0)

dc=60
l.ChangeDutyCycle(dc)
r.ChangeDutyCycle(dc)
time.sleep(1)

l.stop()
r.stop()
gpio.cleanup()