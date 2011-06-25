#!/usr/bin/env python

import socket

class SocketCommunication:
  def __init__(self):
    self.RECEIVER_HOST = '192.168.1.4'    # The remote host
    self.PORT =  3000 # The same port as used by the server

  def open(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    self.sock.connect((self.RECEIVER_HOST, self.PORT))

  def close(self):
    self.sock.close()

  def communicate(self, data):
    self.sock.send(data) 

def main():
  pass #TODO: add example

if __name__ == "__main__":
  main()
