# AU6989SN

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

### Load & Run
Assuming the drive is `/dev/sda`  
First, drop to ROM mode:
```
sudo sg_raw -r 512 /dev/sda f8 51 00 ff 00 00 00 00
```
Then load and run custom code:
```
sudo sg_raw -s 12800 /dev/sda fa 0a 00 18 00 00 00 00 < firmware.bin
```

Now the flash drive's status LED will start blinking at fixed period. It will stop responding to USB. Replug the drive to get back to normal state.


