import socket
target_host = "192.168.100.173"
target_port = 9997

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send data
client.sendto(b'TESSSSSSSSSS',(target_host,target_port))
# receive data
data, addr = client.recvfrom(4096)
print(data.decode())
client.close()