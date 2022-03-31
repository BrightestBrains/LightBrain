'''
Simple test script to test dmx capability of LightBrain board
https://github.com/BrightestBrains/LightBrain

I didn't get the result I wanted because it doesn't work right.
But thanks to this script, it became clear that the hardware part works.
Functionality: press buttons to move through 'values buffer'
The user LED will be set to the current value and the value will be sent to the DMX
'''

import machine
from machine import UART, Pin, reset
import time

machine.freq(240000000)
dmx = UART(1)
dmx.init(250000, bits=8, parity=None, stop=2, tx=2, rx=25, txbuf=1024, rxbuf=1024)

dmx_bytes = [chr(0)]*513

rt485 = Pin(26, Pin.PULL_DOWN)
led = Pin(22, Pin.OUT)

def dmxtrigger():
    # This is a hack to make it work according to the protocol timings
    dmx.init(250000, bits=8, parity=None, stop=2, tx=2, rx=25, invert=dmx.INV_TX)
    time.sleep_us(100) 
    dmx.init(250000, bits=8, parity=None, stop=2, tx=2, rx=25, invert=0) 
    time.sleep_us(8) 

def write_frame(brightness):
    dmx_bytes[1] = chr(brightness)
    dmx_bytes[2] = chr(brightness)
    dmx_bytes[3] = chr(brightness)
   
    dmx.write(chr(0x00))
    dmxtrigger()    
    dmx.init(250000, bits=8, parity=None, stop=2, tx=2, rx=25, txbuf=1024, rxbuf=1024)
    # dmx.sendbreak() # — not working with this
    dmx.write(''.join(dmx_bytes))
    # time.sleep_ms(10) # not helping

write_frame(127)
print("*** SETUP FINISHED ***\n")

light = 0
values = [0,1,16,32,64,128,192,255]

def lightchange(value):
    global light
    light = (light + value) % 8
    print(str(light)+" | "+str(values[light]))

def lightup(pin):
    lightchange(1)
    # kinda hack, not working without doubling
    write_frame(values[light])
    write_frame(values[light])

def lightdown(pin):
    lightchange(-1)
    # kinda hack, not working without doubling
    write_frame(values[light])
    write_frame(values[light])

Button32 = Pin(32, Pin.IN, Pin.PULL_UP)
Button33 = Pin(33, Pin.IN, Pin.PULL_UP)

Button32.irq(trigger=Pin.IRQ_RISING, handler=lightup)
Button33.irq(trigger=Pin.IRQ_RISING, handler=lightdown)