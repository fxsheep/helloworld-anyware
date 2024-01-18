#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#include <mcs51/8051.h>

#define	MSB(word)      (BYTE)(((WORD)(word) >> 8) & 0xff)
#define LSB(word)      (BYTE)((WORD)(word) & 0xff)

#define XVAL(addr)     (*( __xdata volatile unsigned char  *)(addr))
#define IVAL(addr)     (*( __idata volatile unsigned char  *)(addr))

void usb_isr (void) __interrupt {
	EX0 = 0;
}

void ep_isr (void) __interrupt {
	EX1 = 0;
}

void timer0_isr (void) __interrupt {
	ET0 = 0;
}

void timer1_isr (void) __interrupt {
	ET1 = 0;
}

void com0_isr (void) __interrupt {
	ES = 0;
}

int main(void) {
   	int i, j;
	while(1){
		XVAL(0xFA15) |= 1;
		for(i = 0; i <= 10000; i++)
			for(j = 0; j <= 100; j++);
		XVAL(0xFA15) &= 0xFE;
		for(i = 0; i <= 10000; i++)
			for(j = 0; j <= 100; j++);
	}
	return 0;
}

