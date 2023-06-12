#!/usr/bin/env python3
import argparse,sys,usb

# USB protocol
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

USB_MSG_TIMEOUT = 1000

# DFU protocol
USB_FIRMWARE_DOWNLOAD = 0x30
USB_FIRMWARE_DOWNLOAD_COMPLETE = 0x31
BLOCK_SIZE = 4096

# Memory address
AR9271_FIRMWARE_BASE = 0x501000
AR9271_FIRMWARE_TEXT_BASE = 0x903000

vid = 0x0cf3
pid = 0x9271

def auto_int(x):
    return int(x, 0)

parser = argparse.ArgumentParser(description='Load AR9271 firmware')
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
    print("No AR9271 BootROM device found, wrong VID/PID?")
    exit()
if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)
dev.set_configuration()

fw = open(sys.argv[1], mode='rb')

memaddr = AR9271_FIRMWARE_BASE

while True:
    blk = fw.read(BLOCK_SIZE)
    if len(blk) == 0:
        break
    dev.ctrl_transfer(USB_VENDOR_REQUEST_OUT, USB_FIRMWARE_DOWNLOAD, memaddr >> 8, 0, blk)
    if len(blk) < BLOCK_SIZE:
        break
    memaddr = memaddr + len(blk)

# Boot
dev.ctrl_transfer(USB_VENDOR_REQUEST_OUT, USB_FIRMWARE_DOWNLOAD_COMPLETE, AR9271_FIRMWARE_TEXT_BASE >> 8, 0)

