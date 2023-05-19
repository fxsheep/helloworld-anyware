import sys,usb,struct

USB_TIMEOUT_DEFAULT = 1000

SMS_EP_IN  = 0x81
SMS_EP_OUT = 0x02

HIF_TASK   = 11

class SMS1180USB:
    def __init__(self, dev, timeout=USB_TIMEOUT_DEFAULT):
        self.dev = dev
        self.timeout = timeout
    
    def usb_read(self):
        try:
            return bytes(self.dev.read(SMS_EP_IN, 512, self.timeout))
        except usb.core.USBTimeoutError:
            return None

    def usb_write(self, data):
        try:
            return self.dev.write(SMS_EP_OUT, data, self.timeout)
        except usb.core.USBTimeoutError:
            return False
    def msg_send_req_ex(self, request, src_id, dst_id, flags, payload):
        data = struct.pack("<HBBHH", request, src_id, dst_id, len(payload) + 8, flags) + payload
        self.usb_write(data)

    def msg_send_req(self, request, payload=bytes([])):
        return self.msg_send_req_ex(request, 0, HIF_TASK, 0, payload)

    #return: response, src_id, dst_id, length, flags, payload
    def msg_get_resp_ex(self):
        data = self.usb_read()
        if data == None or len(data) < 8:
            return None,
        else:
            response, src_id, dst_id, length, flags = struct.unpack("<HBBHH", data[0:8])
            return response, src_id, dst_id, length, flags, data[8:]

    #return: response, payload
    def msg_get_resp(self):
        ret = self.msg_get_resp_ex()
        if len(ret) == 1:
            return None,
        else:
            return ret[0], ret[5]
