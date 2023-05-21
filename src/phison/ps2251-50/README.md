# PS2251-50

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

If your device is in normal mode(i.e. "working properly"), enter BootROM mode:
```
sudo sg_raw /dev/sda 06 bf 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

Load custom code to SRAM in BootROM mode:
```
sudo sg_raw -s 512 /dev/sda 06 b1 03 00 00 00 00 00 01 00 00 00 00 00 00 00 < header.bin
sudo sg_raw -s 4096 /dev/sda 06 b1 02 00 00 00 00 00 08 00 00 00 00 00 00 00 < firmware.bin
```

### Run
```
sudo sg_raw /dev/sda 06 b3 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```
Now the flash drive's status LED will start blinking at fixed period. It will stop responding to USB. Replug the drive to get back to normal state.


