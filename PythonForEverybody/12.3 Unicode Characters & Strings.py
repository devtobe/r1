# The ord() function tells us the numeric value of a simple ASCII character
print(ord("H"))
print("你好")
print(type("你好"))
print(type(b"abc"))
print()


# When pulling things in python 3, you will have to decode the things that you pulled in.
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    mystring = data.decode()
    print(mystring)

mysock.close()

