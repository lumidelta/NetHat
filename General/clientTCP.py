import socket

target_host="127.0.0.1"
target_port=9997

# create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to host
client.connect((target_host, target_port))

# send data
client.send(b"something")

# get responce
response = client.recv(4096)

print(response.decode())
client.close()
