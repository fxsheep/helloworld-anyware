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

#Realtek protocol
RTW_USB_CONTROL_MSG_TIMEOUT = 500
REALTEK_USB_CMD_REQ = 0x05
REALTEK_USB_CMD_IDX = 0x00
RTL_FW_PAGE_SIZE = 4096

#Address space
REG_FW_START_ADDRESS = 0x1000
REG_SYS_FUNC = 0x0002
REG_MCU_FW_DL = 0x0080

#Bits definition
SYS_FUNC_CPU_ENABLE = (1<<10)
MCU_FW_DL_ENABLE = (1<<0)
MCU_FW_DL_READY = (1<<1)
MCU_WINT_INIT_READY = (1<<6)

if len(sys.argv) != 2 :
    print("usage: rtl8188eu_load_fw.py <raw firmware(no header)>")
    exit()

fw = open(sys.argv[1], mode='rb')

dev = usb.core.find(idVendor=0x0bda, idProduct=0x8179)
if (dev == None):
    print("No RTL8188EU device found")
    exit()
if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)
dev.set_configuration()

def xram_read(base, size):
    return dev.ctrl_transfer(USB_VENDOR_REQUEST_IN, REALTEK_USB_CMD_REQ, base, 0, size)

def xram_write(base, data):
    dev.ctrl_transfer(USB_VENDOR_REQUEST_OUT, REALTEK_USB_CMD_REQ, base, 0, data)

def xram_readb(addr):
    return int.from_bytes(xram_read(addr, 1), "little")

def xram_writeb(addr, val):
    xram_write(addr, val.to_bytes(1, byteorder='little'))

def xram_readh(addr):
    return int.from_bytes(xram_read(addr, 2), "little")

def xram_writeh(addr, val):
    xram_write(addr, val.to_bytes(2, byteorder='little'))

def xram_readl(addr):
    return int.from_bytes(xram_read(addr, 4), "little")

def xram_writel(addr, val):
    xram_write(addr, val.to_bytes(4, byteorder='little'))

#Disable firmware download
xram_writeb(REG_MCU_FW_DL, 0x00)


#Reset CPU

#Disable 8051
xram_writeh(REG_SYS_FUNC, (xram_readh(REG_SYS_FUNC) & (~SYS_FUNC_CPU_ENABLE)))

#Enable 8051
xram_writeh(REG_SYS_FUNC, (xram_readh(REG_SYS_FUNC) | SYS_FUNC_CPU_ENABLE))


#Enable firmware download
xram_writeb(REG_MCU_FW_DL, (xram_readb(REG_MCU_FW_DL) | MCU_FW_DL_ENABLE))

#Reset 8051
xram_writel(REG_MCU_FW_DL, (xram_readl(REG_MCU_FW_DL) & (~(1<<19))))

#Download firmware
i = 0
while True:
    page = fw.read(RTL_FW_PAGE_SIZE)
    if len(page) == 0:
        break
    #Bank switching
    val = xram_readb(REG_MCU_FW_DL + 2) & 0xF8
    val = val | i
    xram_writeb(REG_MCU_FW_DL + 2, val)
    xram_write(REG_FW_START_ADDRESS, page)
    if len(page) < RTL_FW_PAGE_SIZE:
        break
    i = i + 1

#Disable firmware download
xram_writeb(REG_MCU_FW_DL, (xram_readb(REG_MCU_FW_DL) & (~MCU_FW_DL_ENABLE)))


#Finish download
val = xram_readl(REG_MCU_FW_DL)
val = val | MCU_FW_DL_READY
val = val & (~MCU_WINT_INIT_READY)
xram_writel(REG_MCU_FW_DL, val)


#Reset CPU again

#Disable 8051
xram_writeh(REG_SYS_FUNC, (xram_readh(REG_SYS_FUNC) & (~SYS_FUNC_CPU_ENABLE)))

#Enable 8051
xram_writeh(REG_SYS_FUNC, (xram_readh(REG_SYS_FUNC) | SYS_FUNC_CPU_ENABLE))

fw.close()
