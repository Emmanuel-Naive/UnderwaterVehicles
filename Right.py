# -*- coding: utf-8 -*-                #通过声明可以在程序中书写中文
import RPi.GPIO as gpio
import time
import sys

pin2 = 22

gpio.setmode(gpio.BOARD)
gpio.setup(pin2, gpio.OUT)

r = gpio.PWM(pin2, 500)     #频率设置为500Hz
r.start(0)

dc=80
r.ChangeDutyCycle(dc)
time.sleep(5)

r.stop()
gpio.cleanup()