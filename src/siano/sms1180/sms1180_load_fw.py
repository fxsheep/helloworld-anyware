#!/usr/bin/env python3
import sys,usb
from sms1180usb import *

MSG_SMS_INIT_DEVICE_REQ          = 578
MSG_SMS_DATA_DOWNLOAD_REQ        = 660
MSG_SMS_DATA_VALIDITY_REQ        = 662
MSG_SMS_SWDOWNLOAD_TRIGGER_REQ   = 664
MSG_SMS_GET_VERSION_EX_REQ       = 668

SMS_MAX_PAYLOAD_SIZE             = 240

if len(sys.argv) != 2 :
    print("usage: sms1180_load_fw.py <firmware>")
    exit()

dev = usb.core.find(idVendor=0x187f, idProduct=0x0300)
if (dev == None):
    print("No SMS1180 device found")
    exit()
if dev.is_kernel_driver_active(0):
    dev.detach_kernel_driver(0)
dev.set_configuration()

fw = open(sys.argv[1], mode='rb')

sms1180 = SMS1180USB(dev)

# Check chip version
sms1180.msg_send_req(MSG_SMS_GET_VERSION_EX_REQ)

ret = sms1180.msg_get_resp()
if len(ret) != 1:
    if 'Vega' in str(ret[1]):
        header = fw.read(12)
        fw_checksum, fw_len, fw_start = struct.unpack("<III", header)

        # Load
        pos = 0
        while pos < fw_len:
            blk = fw.read(SMS_MAX_PAYLOAD_SIZE)
            sms1180.msg_send_req(MSG_SMS_DATA_DOWNLOAD_REQ, (fw_start + pos).to_bytes(4, byteorder="little") + blk)
            ret = sms1180.msg_get_resp()
            if len(ret) == 1:
                continue
            else: 
                retval = int.from_bytes(ret[1], 'little')
                if(retval != 0):
                    continue
            pos = pos + len(blk)
        
        # Checksum
        sms1180.msg_send_req(MSG_SMS_DATA_VALIDITY_REQ, struct.pack("<III", fw_start, fw_len, 0))
        ret = sms1180.msg_get_resp()
        if len(ret) != 1:
            # should do some checking right? But kernel driver doesn't
            pass
        
        # Boot
        entry = fw_start
        priority = 6
        stack_size = 0x200
        parameter = 0
        task_id = 4
        sms1180.msg_send_req(MSG_SMS_SWDOWNLOAD_TRIGGER_REQ, struct.pack("<IIIII", entry, priority, stack_size, parameter, task_id))
        ret = sms1180.msg_get_resp()
        if len(ret) != 1:
            retval = int.from_bytes(ret[1], 'little')
            if(retval != 1):
                pass
            else:
                print("Load success")

        # Postload
        # MSG_SMS_INIT_DEVICE_REQ

fw.close()


