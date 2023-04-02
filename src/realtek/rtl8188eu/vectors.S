	.globl __sdcc_gsinit_startup

	.area VECTOR	(ABS,CODE)
	.org	0x4000
	ljmp	__sdcc_gsinit_startup

