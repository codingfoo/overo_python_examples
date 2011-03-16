#!/usr/bin/env python

import mmap
import struct

PIN8 = 'PIN8' 
PIN9 = 'PIN9' 
PIN10 = 'PIN10'
PIN11 = 'PIN11'

class PWM:
  """Class that provides an interface for pwm for the overo.
     Assumes that the init_pwm.sh script has been run to mux/initilize pins"""
    def __init__(self):
      self.MAP_SIZE = mmap.PAGESIZE
      self.MAP_MASK = mmap.PAGESIZE - 1

      self.pin_address = {
            'PIN8' : 0x4903E038,
            'PIN9' : 0x49040038,
            'PIN10' : 0x48086038,
            'PIN11' : 0x48088038
            }

      self.pin_index = {}

      for pin, address in self.ADDRESS:
        self.pin_index[pin] = address & self.MAP_MASK

      self.pin_mappings = {}

    def read_pin(self, pin ):
      index = self.pin_index[pin]
      value = mappings[pin][index:index + 4]
      return value

    def write_pin(self, pin, value):
      """See overo omap processor document for valid values.
         The relationship to real world values depends on the application."""
      #TODO: value range check
      index = self.pin_index[pin]
      converted_value = struct.pack( 'L', value )
      self.pin_map[ index : index + 4 ] = converted_value #write 4 bytes, each register value is 4 bytes

    def open_pin(self, pin):
      self.f = open( "/dev/mem", "w+b")

      self.mappings[ pin ] = mmap.mmap(self.f.fileno(), self.MAP_SIZE, offset=self.ADDRESS[ pin ] & ~self.MAP_MASK )

    def open_pins(self):
      self.f = open( "/dev/mem", "w+b")

      for pin, address in self.ADDRESS:
        self.mappings[ pin ] = mmap.mmap(self.f.fileno(), self.MAP_SIZE, offset=self.ADDRESS[ pin ] & ~self.MAP_MASK )

    def close(self):
      for pin, map in self.pin_map:
        map.close()

      self.f.close()

def main():
  pwm_object = PWM()

  pwm_object.open_pins()

  test_pin = PIN8

  print pwm_object.read_pin(test_pin)

  pwm_object.close()

if __name__ == "__main__":
  main()

