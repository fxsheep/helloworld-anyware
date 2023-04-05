#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#include <mcs51/8051.h>

#define	MSB(word)      (BYTE)(((WORD)(word) >> 8) & 0xff)
#define LSB(word)      (BYTE)((WORD)(word) & 0xff)

#define XVAL(addr)     (*( __xdata volatile unsigned char  *)(addr))
#define IVAL(addr)     (*( __idata volatile unsigned char  *)(addr))

#define LED_CTRL       (0xf310)
#define LED_CTRL_ON    (0x00)
#define LED_CTRL_OFF   (0x20)
#define LED_CTRL_BLINK (0x40)

int main(void) {
	int i, j;
	__asm__("clr EA");

	while(1){
		XVAL(LED_CTRL) = LED_CTRL_ON;
		for(i = 0; i <= 10000; i++)
			for(j = 0; j <= 100; j++);
		XVAL(LED_CTRL) = LED_CTRL_OFF;
		for(i = 0; i <= 10000; i++)
			for(j = 0; j <= 100; j++);
	}
	/* Or, just: */
	/*
	XVAL(LED_CTRL) = LED_CTRL_BLINK;
	while(1);
	*/
	return 0;
}

