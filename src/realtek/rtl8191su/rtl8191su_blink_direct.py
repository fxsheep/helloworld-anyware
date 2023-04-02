#!/usr/bin/env python3
import sys,usb,time

#USB protocol
USB_TYPE_MASK = (0x03 << 5)
USB_TYPE_STANDARD = (0x00 << 5)
USB_TYPE_CLASS = (0x01 << 5)
USB_TYPE_VENDOR = (0x02 << 5)
USB_TYPE_RESERVED = (0x03 << 5)

USB_RECIP_MASK = 0x1f
USB_RECIP_DEVICE = 0x00
USB_RECIP_INTERFACE = 0x01
USB_RECIP_ENDPOINT = 0x02
USB_RECIP_OTHER = 0x03
USB_RECIP_PORT = 0x04
USB_RECIP_RPIPE = 0x05

USB_DIR_OUT = 0
USB_DIR_IN = 0x80

USB_VENDOR_REQUEST = ( USB_TYPE_VENDOR | USB_RECIP_DEVICE )
USB_VENDOR_REQUEST_IN = ( USB_DIR_IN | USB_VENDOR_REQUEST )
USB_VENDOR_REQUEST_OUT = ( USB_DIR_OUT | USB_VENDOR_REQUEST )

#Realtek protocol
RTW_USB_CONTROL_MSG_TIMEOUT = 500
REALTEK_USB_CMD_REQ = 0x05
REALTEK_USB_CMD_IDX = 0x00

#Addr space
RTL8712_IOBASE_IOREG = 0x10250000
RTL8712_SYSCFG = RTL8712_IOBASE_IOREG
RTL8712_GP = (RTL8712_IOBASE_IOREG + 0x2E0)
LEDCFG = (RTL8712_GP + 0x12)

dev = usb.core.find(idVendor=0x0bda, idProduct=0x8172)
if (dev == None):
    print("No RTL8191SU device found")
    exit()
if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)
dev.set_configuration()

#Only IOREG regisers are accessible
def ioreg_read(base, size):
    base = base & 0xffff
    return dev.ctrl_transfer(USB_VENDOR_REQUEST_IN, REALTEK_USB_CMD_REQ, base, 0, size)

def ioreg_write(base, data):
    base = base & 0xffff
    dev.ctrl_transfer(USB_VENDOR_REQUEST_OUT, REALTEK_USB_CMD_REQ, base, 0, data)

while True:
    ioreg_write(LEDCFG, [0x20])
    time.sleep(1)
    ioreg_write(LEDCFG, [0x22])
    time.sleep(1)

