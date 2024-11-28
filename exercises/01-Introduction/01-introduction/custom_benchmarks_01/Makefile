GXX = g++
RISCV_GXX = riscv64-linux-gnu-g++
GEM5_PATH ?= /workspaces/latin-america-2024/gem5

workload-x86:
	$(GXX) -o workload workload.c \
	-I$(GEM5_PATH)/include \
	-L$(GEM5_PATH)/util/m5/build/x86/out \
	-lm5
workload-riscv:
	$(RISCV_GXX) -o workload workload.c \
	-I$(GEM5_PATH)/include \
	-L$(GEM5_PATH)/util/m5/build/riscv/out \
	-lm5 -static
