# -*- coding: utf-8 -*-                #通过声明可以在程序中书写中文
import RPi.GPIO as gpio
import time
import sys

pin1 = 18

gpio.setmode(gpio.BOARD)
gpio.setup(pin1, gpio.OUT)

l = gpio.PWM(pin1, 500)     #频率设置为500Hz
l.start(0)

dc=80
l.ChangeDutyCycle(dc)
time.sleep(5)

l.stop()
gpio.cleanup()