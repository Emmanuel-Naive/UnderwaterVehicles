# -*- coding: utf-8 -*-                #通过声明可以在程序中书写中文
#输入通道与角度。即可选通并使该通道的舵机转动到相应的角度
from __future__ import division                             #导入 __future__ 文件的 division 功能函数(模块、变量名....)   #新的板库函数  //=
import time  
import Adafruit_PCA9685                                     #导入Adafruit_PCA9685模块  
 
pwm = Adafruit_PCA9685.PCA9685()                            #把Adafruit_PCA9685.PCA9685()引用地址赋给PWM标签  

def set_servo_speed(channel, speed):              
    pulse_width=1500+10*speed                      #500-1500us的PWM是控制它正转，值越小，旋转速度越大；1500-2500us的PWM是它反转，值越大，旋转速度越大。
    date=4096*pulse_width/20000                     #1500us的PWM是控制它停止。
    pwm.set_pwm(channel, 0, date)  

# Set frequency to 50hz, good for servos.  
pwm.set_pwm_freq(50)  

if True:               # Move servo on channel O between extremes. 
    channel=12
    speed=50
    set_servo_speed(channel, speed)  
    time.sleep(3)  
    speed=0
    set_servo_speed(channel, speed)  