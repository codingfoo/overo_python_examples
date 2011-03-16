import serial
import math
import struct

class IMU:
  """Class for working with a Microstrain IMU"""
  def __init__(self):
    self.IMU_PORT = '/dev/ttyS0'
    self.IMU_BAUD = 115200
    self.CMD_ACCEL_ANG_ORIENT = '\xC8'
    self.CMD_ACCEL_ANG_ORIENT_SIZE = 67

    self.IMU_COMMAND = self.CMD_ACCEL_ANG_ORIENT
    self.IMU_MESSAGE_SIZE = self.CMD_ACCEL_ANG_ORIENT_SIZE

  def open_imu(self):
    self.imu = serial.Serial(self.IMU_PORT, self.IMU_BAUD)

  def close_imu(self):
    self.imu.close()

  def read_imu(self):
    self.imu.write(self.IMU_COMMAND)

    #TODO check IMU write

    data = []
    data = self.imu.read(self.IMU_MESSAGE_SIZE) 
    
    #TODO check read status, check first char, checksum

    #conversion to numbers
    accel_x = struct.unpack('>f', data[1:5])[0]
    accel_y = struct.unpack('>f', data[5:9])[0]
    accel_z = struct.unpack('>f', data[9:13])[0]
    ang_rate_x = struct.unpack('>f', data[13:17])[0]
    ang_rate_y = struct.unpack('>f', data[17:21])[0]
    ang_rate_z = struct.unpack('>f', data[21:25])[0]

    #orientation matrix
    m_1 = struct.unpack('>f', data[33:37])[0]
    m_2 = struct.unpack('>f', data[45:49])[0]
    m_3 = struct.unpack('>f', data[57:61])[0]

    #handle clock rollover outside of function
    t = 0
    t = struct.unpack('>I', data[61:65])[0]

    time = 0.0
    time = t / 62500.0 # convert time to seconds
    
    return accel_x, accel_y, accel_z, m_1, m_2, m_3, ang_rate_x, ang_rate_y, ang_rate_z, time, data  

def main():
  imu = IMU()

  imu.open_imu()

  accel_x, accel_y, accel_z, m_1, m_2, m_3, ang_rate_x, ang_rate_y, ang_rate_z, time, data  = imu.read_imu()

  print accel_x
  print accel_y
  print accel_z
  print ang_rate_x
  print ang_rate_y
  print ang_rate_z
  print time

  imu.close_imu()

if __name__ == "__main__":
  main()
