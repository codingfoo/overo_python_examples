#!/bin/bash
# for omap 35xx, setup pwm associated with general purpose timer 
# for a frequency of 50hz, 1500us pulse width
# On the overo summit board 40 pin
# header, the output can be observed on pins 29-32

# stop the timer
devmem2 0x4903E024 w 0x00000000 
devmem2 0x49040024 w 0x00000000
devmem2 0x48086024 w 0x00000000
devmem2 0x48088024 w 0x00000000

# change clock for pwm 10 and 11, 8 and 9 already use correct clock
devmem2 0x48004A40 w 0x03CA

# set mux 
devmem2 0x48002174 w 0x01020102 
# devmem2 0x48002176 h 0x01020102
devmem2 0x48002178 w 0x01020102
# devmem2 0x48002180 h 0x01020102

# set value for TLDR, timer load (20ms period)
devmem2 0x4903E02C w 0xFFFC08F0 
devmem2 0x4904002C w 0xFFFC08F0
devmem2 0x4808602C w 0xFFFC08F0
devmem2 0x4808802C w 0xFFFC08F0

# set value for TMAR, timer match (1500us pulse width)
devmem2 0x4903E038 w 0xFFFC551C 
devmem2 0x49040038 w 0xFFFC551C
devmem2 0x48086038 w 0xFFFC551C
devmem2 0x48088038 w 0xFFFC551C

# set value for TCRR, timercounter
devmem2 0x4903E028 w 0xFFFFFFFF 
devmem2 0x49040028 w 0xFFFFFFFF
devmem2 0x48086028 w 0xFFFFFFFF
devmem2 0x48088028 w 0xFFFFFFFF

# set TCLR, start the timer
devmem2 0x4903E024 w 0x00001843 
devmem2 0x49040024 w 0x00001843
devmem2 0x48086024 w 0x00001843
devmem2 0x48088024 w 0x00001843
