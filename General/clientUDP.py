import socket

target_host="www.google.com"
target_port=80

# create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
client.sendto(b"AAABBBCCC", (target_host, target_port))

# get responce
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
