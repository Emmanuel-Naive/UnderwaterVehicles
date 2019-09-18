# -*- coding: utf-8 -*-                #通过声明可以在程序中书写中文
#输入通道与角度。即可选通并使该通道的舵机转动到相应的角度
from __future__ import division                             #导入 __future__ 文件的 division 功能函数(模块、变量名....)   #新的板库函数  //=
import time  
import Adafruit_PCA9685                                     #导入Adafruit_PCA9685模块  

# Uncomment to enable debug output.  
#import logging  
#logging.basicConfig(level=logging.DEBUG)
#调试打印日志输出
# Initialise the PCA9685 using the default address (0x40).  
pwm = Adafruit_PCA9685.PCA9685()                            #把Adafruit_PCA9685.PCA9685()引用地址赋给PWM标签  
# Alternatively specify a different address and/or bus:  
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)  

#2^12精度  角度转换成数值
#angle输入的角度值(0--180)
#pulsewidth高电平占空时间(0.5ms--2.5ms)
#/1000将us转换为ms
#20ms时基脉冲(50HZ)
#pulse_width=((angle*11)+500)/1000;
#将角度转化为500(0.5)<-->2480(2.5)的脉宽值(高电平时间)   angle=180时  pulse_width=2480us(2.5ms)
#date/4096=pulse_width/20 ->有上pulse_width的计算结果得date=4096*( ((angle*11)+500)/1000 )/20-->int date=4096((angle*11)+500)/20000;

def set_ect(channel,dc):
    pulse_width=int(dc*0.2)
    date=int(4096*pulse_width/20)              #进行四舍五入运算 date=int(4096*((angle*11)+500)/(20000)+0.5)
    pwm.set_pwm(channel, 0, date)

min=2.5
max=12.5

pwm.set_pwm_freq(50)    # Set frequency to 50hz, good for servos.

if True:
    channel=12
    dc=min
    set_ect(channel,dc)
    time.sleep(2)

    channel = 12
    dc = max
    set_ect(channel,dc)
    time.sleep(2)

    channel = 12
    dc = 2
    set_ect(channel, dc)
    time.sleep(2)