#!/usr/bin/env python

import mmap

class PWM:
    """Class that implements pwm for the overo"""
    def __init__(self):
        self.MAP_SIZE = mmap.PAGESIZE
        self.MAP_MASK = mmap.PAGESIZE - 1

        self.PIN8_ADDRESS = 0x4903E038
        self.PIN9_ADDRESS = 0x49040038
        self.PIN10_ADDRESS = 0x48086038
        self.PIN11_ADDRESS = 0x48088038

        self.f = open( "/dev/mem", "w+b")

        self.pin8_map = mmap.mmap(self.f.fileno(), self.MAP_SIZE, offset=self.PIN8_ADDRESS & ~self.MAP_MASK )
        self.pin9_map = mmap.mmap(self.f.fileno(), self.MAP_SIZE, offset=self.PIN9_ADDRESS & ~self.MAP_MASK )
        self.pin10_map = mmap.mmap(self.f.fileno(), self.MAP_SIZE, offset=self.PIN10_ADDRESS & ~self.MAP_MASK )
        self.pin11_map = mmap.mmap(self.f.fileno(), self.MAP_SIZE, offset=self.PIN11_ADDRESS & ~self.MAP_MASK )

        self.pin8_index = self.PIN8_ADDRESS & self.MAP_MASK
        self.pin9_index = self.PIN9_ADDRESS & self.MAP_MASK
        self.pin10_index = self.PIN10_ADDRESS & self.MAP_MASK
        self.pin11_index = self.PIN11_ADDRESS & self.MAP_MASK

    def close(self):
        self.pin8_map.close()
        self.pin9_map.close()
        self.pin10_map.close()
        self.pin11_map.close()
        self.f.close()

    def pin_read(self, index, map ):
        value = map[ index : index + 4 ] #read 4 bytes, each register value is 4 bytes
        print value.encode("hex")

    def pin8_read(self):
        self.pin_read( self.pin8_index, self.pin8_map )

    def pin9_read(self):
        self.pin_read( self.pin9_index, self.pin9_map )

    def pin10_read(self):
        self.pin_read( self.pin10_index, self.pin10_map )

    def pin11_read(self):
        self.pin_read( self.pin11_index, self.pin11_map )

    def pin_write(self, index, map, value ):
        converted_value = struct.pack( 'L', value )
        map[ index : index + 4 ] = converted_value #write 4 bytes, each register value is 4 bytes

    def pin8_write(self, value):
        self.pin_write( self.pin8_index, self.pin8_map, value )

    def pin9_write(self, value):
        self.pin_write( self.pin9_index, self.pin9_map, value )

    def pin10_write(self, value):
        self.pin_write( self.pin10_index, self.pin10_map, value )

    def pin11_write(self, value):
        self.pin_write( self.pin11_index, self.pin11_map, value )

def main():
  pwm_object = PWM()
  pwm_object.pin8_read()
  pwm_object.pin9_read()
  pwm_object.pin10_read()
  pwm_object.pin11_read()
  pwm_object.close()

if __name__ == "__main__":
  main()

