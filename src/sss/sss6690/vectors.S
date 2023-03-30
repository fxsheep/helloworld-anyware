	.globl __sdcc_gsinit_startup

	.area VECTOR	(ABS,CODE)
	.org	0xb000
	ljmp	__sdcc_gsinit_startup

