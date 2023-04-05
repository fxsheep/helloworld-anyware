AS := sdas8051
ASFLAGS := -l -o -s
CC := sdcc
CFLAGS := -mmcs51 --std-sdcc11 --model-small --stack-auto --code-loc 0x9000
OBJCOPY := sdobjcopy

BINARIES := firmware.bin

all: $(BINARIES)

%.rel: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

%.rel: %.S
	$(AS) $(ASFLAGS) $<

firmware.ihx: main.rel vectors.rel
	$(CC) $(CFLAGS) -o $@ $^

%.bin: %.ihx
	$(OBJCOPY) -I ihex -O binary $< $@
	truncate -s 10240 $@

clean:
	rm -f *.asm *.bin *.fw *.ihx *.lk *.lst *.map *.mem *.rel *.rst *.sym

.PHONY: all clean
