	.globl __sdcc_gsinit_startup

	.area VECTOR	(ABS,CODE)
	.org	0xc000
	ljmp	__sdcc_gsinit_startup

