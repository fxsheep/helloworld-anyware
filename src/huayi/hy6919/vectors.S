	.globl __sdcc_gsinit_startup

	.area VECTOR	(ABS,CODE)
	.org	0x9000
	ljmp	__sdcc_gsinit_startup
	ljmp	__sdcc_gsinit_startup

