LIB_PATH=/lib/modules
obj-m += mod_hw.o
all:
	make -C $(LIB_PATH)/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C $(LIB_PATH)/$(shell uname -r)/build M=$(PWD) clean
