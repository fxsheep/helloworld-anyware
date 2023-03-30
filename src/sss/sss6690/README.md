# SSS6690

## Info

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

### Load
Assuming the drive is `/dev/sda`
```
sudo sg_raw -s 4096 /dev/sda ff 50 00 00 00 00 00 00 00 00 00 00 < firmware.bin 
```

### Run
```
sudo sg_raw -r 512 /dev/sda ff e0 00 00 00 00 00 00 00 00 00 00 
```
Now the flash drive's status LED will start blinking at fixed period. It will stop responding to USB. Replug the drive to get back to normal state.


