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

## Supported hardwares
|      Category       |     Manufacturer    |                  Chip                   | 
|---------------------|---------------------|-----------------------------------------|
|   USB Flash Drive   | Solid State Systems |     [SSS6690](./src/sss/sss6690)        |



