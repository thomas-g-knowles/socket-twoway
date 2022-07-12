import socket
from time import sleep

try:
  sock = socket.socket()
  sock.bind(('', 12345))
  sock.listen(5)
  host, address_port = sock.accept()
  print(f"- Socket established and running with a connection from IP: {address_port[0]} and PORT: {address_port[1]} \n")

  while True:
    client_response = host.recv(1024).decode()
    if client_response == "TERMINATE":
      print("- - Client terminated socket connection.")
      break
    print("- CLIENT:", client_response)

    data = ""
    while data == "":
      data = input("- SERVER: ")

    if data == "TERMINATE":
      host.send(data.encode())
      break
    
    host.send(data.encode())
except ConnectionResetError:
  print("- - Client forcefully terminated socket connection.")

host.close()
print("- - Socket closed; script termination imminent...")
for second in range(5, 0, -1):
  print("- -", second)
  sleep(1)
