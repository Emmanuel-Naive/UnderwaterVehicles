# -*- coding: utf-8 -*-                 #通过声明可以在程序中书写中文
import RPi.GPIO as GPIO                 #引入RPi.GPIO库函数命名为GPIO
import time                             #引入计时time函数

# BOARD编号方式，基于插座引脚编号
GPIO.setmode(GPIO.BOARD)                #将GPIO编程方式设置为BOARD模式

#接口定义
INT1 = 11                               #将L298 INT1口连接到树莓派Pin11
INT2 = 12                               #将L298 INT2口连接到树莓派Pin12
INT3 = 13                               #将L298 INT3口连接到树莓派Pin13
INT4 = 15                               #将L298 INT4口连接到树莓派Pin15
while 1:
    a=input("请输入指令：")
    if a=="L":                                              #左电机工作，开始抽水，同时电磁阀开启
        GPIO.setup(INT3, GPIO.OUT)
        GPIO.setup(INT4, GPIO.OUT)
        continue
    if a=="R":                                              #右电机工作，开始排水，同时电磁阀关闭
        GPIO.setup(INT1, GPIO.OUT)
        GPIO.setup(INT2, GPIO.OUT)
        continue
    if a=="E":
        break
GPIO.cleanup()