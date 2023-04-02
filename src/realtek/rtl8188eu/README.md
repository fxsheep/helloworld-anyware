# RTL8188EU

## Info

- CPU
  - MCS-51 (8051) compatible

## Usage


### Dependencies
```
sudo apt install sdcc
```

### Build
```
make
```

### Load & Run
```
sudo python3 rtl8188eu_load_fw.py firmware.bin
```

Now the Wi-Fi adapter's LED will start blinking at fixed period. Replug the adapter to get back to normal state.

## Alternative
`rtl8188eu_blink_direct.py` achieves mostly same LED blinking effect as above. However, the LED is toggled from USB memory access by the host directly, instead of the on-chip 8051 CPU. 
```
sudo python3 rtl8188eu_blink_direct.py
```
