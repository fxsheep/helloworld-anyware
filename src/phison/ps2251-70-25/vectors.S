	.globl __sdcc_gsinit_startup

	.area VECTOR	(ABS,CODE)
	.org	0x5000
__interrupt_vect:
	ljmp	__sdcc_gsinit_startup
	.ds	0x46 - 0x3
        ljmp    __sdcc_gsinit_startup

