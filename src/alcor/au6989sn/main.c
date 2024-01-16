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
	while (1) {
		XVAL(0x9001) = 0xff;
		for (uint16_t volatile i = 0; i < 60000; i++);
		XVAL(0x9001) = 0x00;	
		for (uint16_t volatile i = 0; i < 60000; i++);
	}
	return 0;
}

