import socket

hostname = raw_input('Hostname : ')
IPHOLDER = socket.gethostbyname(hostname)

print '-- IP -- :', hostname, ' - ', IPHOLDER
