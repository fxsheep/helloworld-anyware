#!/usr/bin/env python3
import sys,usb

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

#DFU protocol
USB_REQ_DFU_DNLOAD = 1
BULK_SIZE = 4096
FW_HDR_SIZE = 20
USB_EP_DFU_BULK = 0x02

if len(sys.argv) != 2 :
    print("usage: ar3011_load_fw.py <firmware>")
    exit()

dev = usb.core.find(idVendor=0x0cf3, idProduct=0x3000)
if (dev == None):
    print("No AR3011 BootROM device found")
    exit()
if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)
dev.set_configuration()

fw = open(sys.argv[1], mode='rb')

dev.ctrl_transfer(USB_VENDOR_REQUEST_OUT, USB_REQ_DFU_DNLOAD, 0, 0, fw.read(FW_HDR_SIZE))

while True:
    blk = fw.read(BULK_SIZE)
    if len(blk) == 0:
        break
    dev.write(USB_EP_DFU_BULK, blk, 3000)
    if len(blk) < BULK_SIZE:
        break

