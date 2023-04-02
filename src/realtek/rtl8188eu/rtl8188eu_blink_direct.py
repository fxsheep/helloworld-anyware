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

dev = usb.core.find(idVendor=0x0bda, idProduct=0x8179)
if (dev == None):
    print("No RTL8188EU device found")
    exit()
if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)
dev.set_configuration()

addr = 0x004e

while True:
    dev.ctrl_transfer(USB_VENDOR_REQUEST_OUT, REALTEK_USB_CMD_REQ, addr, 0, [(1<<5 | 1<<3)])
    time.sleep(1)
    dev.ctrl_transfer(USB_VENDOR_REQUEST_OUT, REALTEK_USB_CMD_REQ, addr, 0, [(1<<5)])
    time.sleep(1)

