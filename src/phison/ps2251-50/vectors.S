	.globl __sdcc_gsinit_startup
	.globl _usb_isr
	.globl _ep_isr
	.globl _timer0_isr
	.globl _timer1_isr

	.area VECTOR	(ABS,CODE)
	.org	0x8000
__interrupt_vect:
	ljmp	__sdcc_gsinit_startup
	ljmp	_usb_isr
	.ds	0xB - (0x3 + 3)
	ljmp	_timer0_isr
	.ds	0x13 - (0xB + 3)
	ljmp	_ep_isr
	.ds	0x1B - (0x13 + 3)
	ljmp	_timer1_isr	
	.ds	0x4E - (0x1B + 3)
        ljmp    __sdcc_gsinit_startup

