'''
SSSID maker
Makes wifi networks
with a name from a file with a specified interval
'''
import machine
import time
import network
import uasyncio
import random
import os
from machine import Pin, reset
from network import WLAN

led = Pin(22, Pin.OUT)

def buttons_setup():
    print("_ buttons setup _\n")
    Button32 = Pin(32, Pin.IN, Pin.PULL_UP)
    Button33 = Pin(33, Pin.IN, Pin.PULL_UP)
    Button32.irq(trigger=Pin.IRQ_RISING, handler=button_right)
    Button33.irq(trigger=Pin.IRQ_RISING, handler=button_left)

def button_right(pin):
    print(pin.id)
    pass

def button_left(pin):
    print(pin)
    pass

buttons_setup()

# read filesystem and select first *.txt file to read
print("_ text preparation _\n")
texts = []
for file in os.listdir():
    if file.endswith(".txt"):
        texts.append(file)
f = open(texts[0])
rows = f.read().split("\n")
count = len(rows) - 1
f.close()

tokens = []
for row in rows:
    words = row.split(" ")

current_row = 0

def makeSSID():
    global rows, current_row
    led.on()
    name = rows[current_row]
    print(name)
    ap = WLAN(network.AP_IF)
    ap.config(essid=name)
    ap.active(True)
    current_row = (current_row + 1) % count
    led.off()

async def SSIDmaker():
    while True:
        makeSSID()
        await uasyncio.sleep(8)

uasyncio.run(SSIDmaker())