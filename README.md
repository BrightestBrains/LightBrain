
# LightBrain

## Overview

The initial motivation was to develop a compact and relatively versatile light control device. Communicating with colleagues interested in electronics, I made a few design decisions so that the functionality would meet a number of requests: wide power supply voltages, protection, buttons, DMX support, shifted ouputs.

* ESP32-WROOM module
* four level shifted outputs
* 6-30V protected power input
* RS485 chip (DMX Support)
* Convinent buttons and user LED
* Very handy WAGO spring terminals

## Usage

Designed mostly for the usage with [WLED firmware](https://github.com/Aircoookie/WLED) by [Aircookie](https://github.com/Aircoookie)

There is no USB=>UART bridge in design. This was done to make the design smaller and cheaper. In the future, a firmware device with pogopin will be made, but most likely there will be a revision of the entire design. WLED has OTA functionality which can be used in case of update the firmware.

The board comes with a few examples that I wrote to test the functionality of the board. I really like [micropython](https://micropython.org/), which works fine on these boards. Very handy for prototyping, the buttons and custom LED makes it interactive. Unfortunately, I never got around to running DMX with python. Then I wrote an example using the SparkFunDMX library, which works like a charm.
