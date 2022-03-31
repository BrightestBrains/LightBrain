import machine
import time
from machine import Pin, reset

led = Pin(22, Pin.OUT)

def buttons_setup():
    print("_ buttons setup _\n")
    Button32 = Pin(32, Pin.IN, Pin.PULL_UP)
    Button33 = Pin(33, Pin.IN, Pin.PULL_UP)
    Button32.irq(trigger=Pin.IRQ_RISING, handler=button_right)
    Button33.irq(trigger=Pin.IRQ_RISING, handler=button_left)

def button_right(pin):
    print("right")
    blink(35,15)

def button_left(pin):
    print("left")
    blink(200,3)

def blink(t,count):
    for i in range(count):
        led.on()
        time.sleep_ms(t)
        led.off()
        time.sleep_ms(t)

blink(125, 5)
buttons_setup()