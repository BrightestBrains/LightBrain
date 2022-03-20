"""
Simple example to try LightBrain buttons
Press a button to cycle through values
Current value will be shown as user LED brightness
"""
import machine
from machine import Pin, reset
import time

light = 0
values = [0,1,16,32,64,128,192,256]

pwm = machine.PWM(machine.Pin(22), freq=2200)

def lightchange(value):
    global light
    global pwm
    light = (len(values) + light + value) % len(values)
    pwm.duty(values[light])
    print(str(light)+" | "+str(values[light]))

def lightup(pin):
    lightchange(1)

def lightdown(pin):
    lightchange(-1)

Button32 = Pin(32, Pin.IN, Pin.PULL_UP)
Button33 = Pin(33, Pin.IN, Pin.PULL_UP)

Button32.irq(trigger=Pin.IRQ_RISING, handler=lightup)
Button33.irq(trigger=Pin.IRQ_RISING, handler=lightdown)