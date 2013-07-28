deps_config := \
	/home/fwmiller/Freescale/ltib/config/main.lkc

.config include/linux/autoconf.h: $(deps_config)

$(deps_config):
