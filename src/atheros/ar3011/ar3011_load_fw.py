#!/usr/bin/env python3
import argparse,sys,usb

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

vid = 0x0cf3
pid = 0x3000

def auto_int(x):
    return int(x, 0)

parser = argparse.ArgumentParser(description='Load AR3011 firmware')
parser.add_argument('firmware', type=str, help='firmware filename')
parser.add_argument('--vid', type=auto_int, help='USB VID')
parser.add_argument('--pid', type=auto_int, help='USB PID')
args = parser.parse_args()

if(args.vid):
    vid = args.vid
if(args.pid):
    pid = args.pid

dev = usb.core.find(idVendor=vid, idProduct=pid)
if (dev == None):
    print("No AR3011 BootROM device found")
    exit()
if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)
dev.set_configuration()

fw = open(args.firmware, mode='rb')

dev.ctrl_transfer(USB_VENDOR_REQUEST_OUT, USB_REQ_DFU_DNLOAD, 0, 0, fw.read(FW_HDR_SIZE))

while True:
    blk = fw.read(BULK_SIZE)
    if len(blk) == 0:
        break
    dev.write(USB_EP_DFU_BULK, blk, 3000)
    if len(blk) < BULK_SIZE:
        break

