#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#include <mcs51/8051.h>

#define	MSB(word)      (BYTE)(((WORD)(word) >> 8) & 0xff)
#define LSB(word)      (BYTE)((WORD)(word) & 0xff)

#define XVAL(addr)     (*( __xdata volatile unsigned char  *)(addr))
#define IVAL(addr)     (*( __idata volatile unsigned char  *)(addr))

#define REG_LEDCFG2    0x004e

int main(void) {
   	int i, j;
   	__asm__("clr EA");
	while(1){
		XVAL(REG_LEDCFG2) = (1<<5 | 1<<3);
		for(i = 0; i <= 10000; i++)
			for(j = 0; j <= 100; j++);
		XVAL(REG_LEDCFG2) = (1<<5);
		for(i = 0; i <= 10000; i++)
			for(j = 0; j <= 100; j++);
	}
	return 0;
}

