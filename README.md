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
|         Category          |     Manufacturer    |                  Chip                   | CPU Architecture |   Status    |
|---------------------------|---------------------|-----------------------------------------|------------------|-------------|
|     Bluetooth adapter     |       Atheros       |      [AR3011](./src/atheros/ar3011)     |      Xtensa      |     WIP     |
|     Bluetooth adapter     |        Intel        |        [AX210](./src/intel/ibt)         |       ARC        | Unsupported |
|        Card Reader        |    Genesys Logic    |                GL3223                   |       8051       | Unsupported |
|        Card Reader        |    Genesys Logic    |                GL3233                   |       8051       | Unsupported |
|        Card Reader        |      Prolific       |                PL2733                   |       8051       | Unsupported |
|        Card Reader        |       Realtek       |                RTS5306                  |       8051       | Unsupported |
|        Card Reader        |    Silicon Motion   |                SM330                    |       8051       | Unsupported |
|       CD-ROM Drive        |      MediaTek       |                MT1198                   |       8051       | Unsupported |
|     CMMB TV receiver      |        Siano        |      [SMS1180](./src/siano/sms1180)     |       ARC        |     WIP     |
|           eMMC            |       Samsung       |                 VNC                     |       ARM        | Unsupported |
|     Hard Disk Drive       |       Marvell       |                88I6889                  |       ARM        | Unsupported |
|         Laptop EC         |       ITE Tech      |                IT8586                   |       8051       | Unsupported |
|         Laptop EC         |       ITE Tech      |                IT8987                   |       8051       | Unsupported |
|     Solid State Drive     |       JMicron       |     [JMF605](./src/jmicron/jmf605)      |       ARM        |     WIP     |
|     Solid State Drive     |       JMicron       |     [JMF608](./src/jmicron/jmf608)      |       ARM        |     WIP     |
|     Solid State Drive     |       JMicron       |     [JMF667](./src/jmicron/jmf667)      |       ARM        |     WIP     |
|     Solid State Drive     |       Marvell       |   [88NV1120](./src/marvell/88nv1120)    |       ARM        |     WIP     |
|     Solid State Drive     |       Marvell       |                88SS1074                 |       ARM        | Unsupported |
|     Solid State Drive     |       Phison        |      [PS3111](./src/phison/ps3111)      |      Xtensa      |     WIP     |
|     Solid State Drive     |       Samsung       |               S4LN045X01                |       ARM        | Unsupported |
|     Solid State Drive     |       SanDisk       |                Milpitas                 |       ARC        | Unsupported |
|     Solid State Drive     |    Silicon Motion   |                SM222                    |       8051       | Unsupported |
|     Solid State Drive     |    Silicon Motion   |                SM223                    |       8051       | Unsupported |
|     Solid State Drive     |    Silicon Motion   |                SM2231                   |       8051       | Unsupported |
|     Solid State Drive     |    Silicon Motion   |                SM2246                   |       ARC        | Unsupported |
|     Solid State Drive     |    Silicon Motion   |                SM2256                   |       ARC        | Unsupported |
|     Solid State Drive     |    Silicon Motion   |                SM2258                   |       ARC        | Unsupported |
|     Solid State Drive     |    Silicon Motion   |                SM2259                   |       ARC        | Unsupported |
|   Touch Panel Controller  |      FocalTech      |                FT5x06                   |       8051       | Unsupported |
|   Touch Panel Controller  |       Melfas        |                MMS134S                  |       ARM        | Unsupported |
|      USB Flash Drive      |     Alcor Micro     |    [AU6989SN](./src/alcor/au6989sn)     |       8051       |  Supported  |
|      USB Flash Drive      |        Huayi        |      [HY6919](./src/huayi/hy6919)       |       8051       |  Supported  |
|      USB Flash Drive      |       Phison        |   [PS2251-06](./src/phison/ps2251-06)   |       8051       |  Supported  |
|      USB Flash Drive      |       Phison        |   [PS2251-07](./src/phison/ps2251-07)   |       8051       |  Supported  |
|      USB Flash Drive      |       Phison        |   [PS2251-50](./src/phison/ps2251-50)   |       8051       |  Supported  |
|      USB Flash Drive      |       Phison        |[PS2251-70-25](./src/phison/ps2251-70-25)|       8051       |  Supported  |
|      USB Flash Drive      |       SanDisk       |                Anisha                   |       ARC        | Unsupported |
|      USB Flash Drive      |       SanDisk       |                Karona                   |       ARC        | Unsupported |
|      USB Flash Drive      |       SanDisk       |                Sumeru                   |       ARC        | Unsupported |
|      USB Flash Drive      |    Silicon Motion   |                SM3257                   |       8051       | Unsupported |
|      USB Flash Drive      |    Silicon Motion   |                SM3259                   |       8051       | Unsupported |
|      USB Flash Drive      |    Silicon Motion   |                SM3280                   |       ARC        | Unsupported |
|      USB Flash Drive      | Solid State Systems |     [SSS6690](./src/sss/sss6690)        |       8051       |  Supported  |
|          USB Hub          |    Genesys Logic    |                GL3520                   |      Unknown     | Unsupported |
|      USB-SATA adapter     |       JMicron       |     [JM20339](./src/jmicron/jm20339)    |       8051       |     WIP     |
|       Wi-Fi adapter       |       Atheros       |      [AR9271](./src/atheros/ar9271)     |      Xtensa      |     WIP     |
|       Wi-Fi adapter       |        Intel        |      [AX210](./src/intel/iwlwifi)       |       ARC        | Unsupported |
|       Wi-Fi adapter       |       Marvell       |                88W8801                  |       ARM        | Unsupported |
|       Wi-Fi adapter       |      MediaTek       |                MT7601                   |      NDS32       | Unsupported |
|       Wi-Fi adapter       |      Qualcomm       |                QCA6391                  |      QDSP6v6     | Unsupported |
|       Wi-Fi adapter       |       Ralink        |                RT2571                   |       8051       | Unsupported |
|       Wi-Fi adapter       |       Ralink        |                RT2870                   |       8051       | Unsupported |
|       Wi-Fi adapter       |       Realtek       |   [RTL8188EU](./src/realtek/rtl8188eu)  |       8051       |  Supported  |
|       Wi-Fi adapter       |       Realtek       |   [RTL8191SU](./src/realtek/rtl8191su)  |       MIPS       |     WIP     |

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

