CC=gcc

BINS = $(patsubst %.c, %.bin, $(wildcard *.c))

all: $(BINS)

%.bin: %.c
	$(CC) -Wall $< -o $@

.PHONY: clean
clean:
	rm -Rf *.bin