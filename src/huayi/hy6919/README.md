# HY6919

## Info
**Note: Tested on COB packaged chips, version 6.80 and 6.90. A properly(SOP) packaged chip is untested but should work as well.**
- CPU
  - MCS-51 (8051) compatible

## Usage


### Dependencies
```
sudo apt install sdcc sg3-utils
```

### Build
```
make
```

### Load & Run
Assuming the drive is `/dev/sda`
```
sudo sg_raw -s 10240 /dev/sda df 00 00 00 14 00 00 00 00 00 00 00 00 00 00 d7 < firmware.bin 
```

Now the flash drive's status LED will start blinking at fixed period. It will stop responding to USB. Replug the drive to get back to normal state.


