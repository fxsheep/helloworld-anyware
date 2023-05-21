# helloworld-anyware
Non-exhausive list of HelloWorld running on anything that (secretly) has a CPU and firmware

## Intro
You're probably viewing this text using a computer(PC, laptop, mobile phone or tablet). However, you're actually not doing so with a single computer, but with many computers. This is true for any modern PC or mobile device, because almost every peripheral/gadget today includes its own CPU, RAM, ROM and runs a firmware code. In short, they are computers on their own.  

`helloworld-anyware` aims at reminding this simple yet possibly not well-known fact, by attempting to run a basic program on CPUs inside ubiquitous hardwares(e.g. USB Flash Drives, Wi-Fi cards, Bluetooth adapters, SSDs, stuff on laptop motherboards), which proves the existence of these cores.  

## Precaution
Running a custom firmware may cause unexpected behavior and brick/physically damage your devices. 
 - Do not attempt to run any arbitrary code on a device that is important to you.
 - Be extra careful with 'stateful' devices, e.g. a USB flash drive that has NAND flash, or a Wi-Fi card that has e-fuses for calibration. In case they are (accidentally) changed, there is no sufficient knowledge provided in this repo to change them back.

## Usage
Each hardware/peripheral has its own way to build(different CPU architectures), load(different DFU/ISP implementations) and run(different output devices, such as an LED) a HelloWorld. Please refer to chip-specific description for details. Find your target using the table below.

## List of hardwares
|      Category       |     Manufacturer    |                  Chip                   | Status  |
|---------------------|---------------------|-----------------------------------------|---------|
|  Bluetooth adapter  |       Atheros       |      [AR3011](./src/atheros/ar3011)     |   WIP   |
|  CMMB TV receiver   |        Siano        |      [SMS1180](./src/siano/sms1180)     |   WIP   |
|   USB Flash Drive   |        Huayi        |      [HY6919](./src/huayi/hy6919)       |Supported|
|   USB Flash Drive   |       Phison        |   [PS2251-50](./src/phison/ps2251-50)   |Supported|
|   USB Flash Drive   |       Phison        |[PS2251-70-25](./src/phison/ps2251-70-25)|Supported|
|   USB Flash Drive   | Solid State Systems |     [SSS6690](./src/sss/sss6690)        |Supported|
|    Wi-Fi adapter    |       Realtek       |   [RTL8188EU](./src/realtek/rtl8188eu)  |Supported|
|    Wi-Fi adapter    |       Realtek       |   [RTL8191SU](./src/realtek/rtl8191su)  |   WIP   |

## Adding support for new devices
Details of how a chip works varies vastly from one chip to another, hence here's only a general route if you want to add support for a new device.
- Gathering information about your target device
  - What chip does it use (lsusb, teardown, etc.)
  - Datasheet of the chip (CPU architecture, pinout for GPIO/LED)
- Diving into the details
  - Linux kernel driver source (e.g. Wi-Fi cards)
  - Manufacturer tools (e.g. USB flash drives)
  - [fwupd](https://github.com/fwupd/fwupd) project 
  - USB packet capture
  - Firmware blob
- Sorting out the details
  - DFU/ISP protocol
  - Firmware load address (usually not zero)
  - Firmware usage (some uses the firmware as a library, called by bootrom)
  - Hardware initialization (not required by most)
  - Output 'device' (GPIO/LED registers)
- Implementing a custom firmware
  - Toolchain (may not be readily available in e.g. `apt`)
  - A startup asm file (a 'good' entry point, HW init)
  - A minimal main.c (toggles LED etc.)
  - A Makefile
- Implementing a minimal firmware loader
  - Talk to the chip with its DFU/ISP protocol
  - Not necessarily required when protocol is simple enough (e.g. use `sg_raw`)

## What's next (beyond this repo)
Getting a minimal program to run is the first step towards a custom firmware. Here are some possible next steps:
- Implementing a bit-banged UART TX/'Ir'DA via LED
  - Dumping the internal ROM
- Experimenting with unknown registers
- Implementing a FOSS alternative firmware
- Repurposing the device, e.g.
  - A NAND programmer/USB to parallel port with USB flash drive controllers

