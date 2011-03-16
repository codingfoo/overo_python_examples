class GPIO:
  def __init__(self):
    self.PIN =  "147"
    self.ON = '1'
    self.OFF = '0'

    export = open('/sys/class/gpio/export')
    export.write(self.PIN)
    export.close()

    direction = open('/sys/class/gpio/gpio' + self.PIN + '/direction')
    direction.write('out')
    direction.close()
    
    self.gpio_value = open('sys/class/gpio/gpio' + self.PIN + '/value')
    self.gpio_value.write( self.OFF )

  def on(self):
    self.gpio_value.write( self.ON )

  def off(self):
    self.gpio_value.write( self.OFF )

  def close(self):
    self.gpio_value.close()

def main():
  g = GPIO()

  g.off()

  sleep(2)

  g.on()

  sleep(2)

  g.off()

  g.close()

if __name__ == "__main__":
  main()
