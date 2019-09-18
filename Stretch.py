# -*- coding: utf-8 -*-                #通过声明可以在程序中书写中文
#输入通道与角度。即可选通并使该通道的舵机转动到相应的角度
from __future__ import division                             #导入 __future__ 文件的 division 功能函数(模块、变量名....)   #新的板库函数  //=
import time  
import Adafruit_PCA9685                                     #导入Adafruit_PCA9685模块  


pwm = Adafruit_PCA9685.PCA9685()                            #把Adafruit_PCA9685.PCA9685()引用地址赋给PWM标签  

#2^12精度  角度转换成数值
#angle输入的角度值(0--180)
#pulsewidth高电平占空时间(0.5ms--2.5ms)
#/1000将us转换为ms
#20ms时基脉冲(50HZ)
#pulse_width=((angle*11)+500)/1000;
#将角度转化为500(0.5)<-->2480(2.5)的脉宽值(高电平时间)   angle=180时  pulse_width=2480us(2.5ms)
#date/4096=pulse_width/20 ->有上pulse_width的计算结果得date=4096*( ((angle*11)+500)/1000 )/20-->int date=4096((angle*11)+500)/20000;
date=0
def set_servo_angle(channel, angle):                          #输入角度转换成12^精度的数值
    date=int(4096*((angle*11)+500)/20000)              #进行四舍五入运算 date=int(4096*((angle*11)+500)/(20000)+0.5)
    pwm.set_pwm(channel, 0, date)

channel=0
angle=0
pwm.set_pwm_freq(50)                        # Set frequency to 50hz, good for servos.

if True :                                    # Move servo on channel O between extremes.
    channel=4
    angle=45
    set_servo_angle(channel,angle)
    channe1=8
    angle=45
    set_servo_angle(channe1,angle)