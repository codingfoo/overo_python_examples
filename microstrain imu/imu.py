import serial
import struct

IMU_PORT = '/dev/ttyS0'
IMU_BAUD = 115200
IMU_TIME_CONVERSION = 19660800.0

CMD_ACCEL_ANG_ORIENT = '\xC8'
CMD_ACCEL_ANG_ORIENT_SIZE = 67
CMD_ACCEL_ANG_ORIENT_DATA_FORMAT = '>cfffffffffffffffIH'

class IMU:
  def __init__(self):
    self.IMU_PORT = IMU_PORT
    self.IMU_BAUD = IMU_BAUD

    self.IMU_COMMAND = CMD_ACCEL_ANG_ORIENT
    self.IMU_MESSAGE_SIZE = CMD_ACCEL_ANG_ORIENT_SIZE
    self.IMU_COMMAND_DATA_FORMAT = CMD_ACCEL_ANG_ORIENT_DATA_FORMAT

  def open(self):
    self.imu = serial.Serial(self.IMU_PORT, self.IMU_BAUD)

  def close(self):
    self.imu.close()

  def read(self):
    self.imu.write(self.IMU_COMMAND)

    #TODO check IMU write

    data = []
    data = self.imu.read(self.IMU_MESSAGE_SIZE) 
    
    #TODO check read status, check first char, checksum

    imu_parsed_data = struct.unpack(self.IMU_COMMAND_DATA_FORMAT, data)

    #handle clock rollover outside of function
    secs = imu_parsed_data[-2] / IMU_TIME_CONVERSION # convert time to seconds
    processed_data = imu_parsed_data[1:-2] + ( secs, )

    return  processed_data

def main():
  imu = IMU()
  imu.open()

  data  = imu.read()

  print data

  imu.close()

if __name__ == "__main__":
  main()
