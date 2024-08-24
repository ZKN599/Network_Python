import socket


host = "127.0.0.1" # enter your ip adress to scan


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



for port in range(1,65300):
  result = s.connect_ex((host,port)) # result = 0 port open a  nonzero value the port is closed
  print(port,":",result)
