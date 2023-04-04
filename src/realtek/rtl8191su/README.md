# RTL8191SU

## Info

- CPU
  - MIPS little endian

## Usage
**Note that currently only direct register toggling is supported. While it achieves a similar result, it does not involve running code directly on the internal CPU(the goal of this project).**

### Dependencies
TODO

### Build
TODO

### Load & Run
TODO

## Alternative
~~`rtl8191su_blink_direct.py` achieves mostly same LED blinking effect as above.~~ However, the LED is toggled from USB memory access by the host directly, instead of the on-chip CPU. 
```
sudo python3 rtl8191su_blink_direct.py
```
