# This is not my code but I copied it from http://www.py4e.com/code3/socket1.py
# to understand how sockets and simple web browsers work.
# `urllib` hides all of this.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connects through port 80
mysock.connect(('data.pr4e.org', 80))
# converts strings (in Unicode) to UTF-8
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # converts UTF-8 back to strings (in Unicode)
    print(data.decode(),end='')

mysock.close()
