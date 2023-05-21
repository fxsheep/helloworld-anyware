#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#include <mcs51/8051.h>

#define	MSB(word)      (BYTE)(((WORD)(word) >> 8) & 0xff)
#define LSB(word)      (BYTE)((WORD)(word) & 0xff)

#define XVAL(addr)     (*( __xdata volatile unsigned char  *)(addr))
#define IVAL(addr)     (*( __idata volatile unsigned char  *)(addr))

int main(void) {
   	int i, j;
	while(1){
		__asm__("clr p1.1");
		for(i = 0; i <= 10000; i++)
			for(j = 0; j <= 100; j++);
		__asm__("setb p1.1");
		for(i = 0; i <= 10000; i++)
			for(j = 0; j <= 100; j++);
	}
	return 0;
}

