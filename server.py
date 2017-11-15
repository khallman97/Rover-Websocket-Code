# Sockets server.
import socket

s = socket.socket()
s.bind(("10.24.98.208", 5500))
s.listen(1)

print("Connection Waiting...")
sc, addr = s.accept()
print("Connection Matched!")

while True:
    print("Waiting message...")
    received = sc.recv(1028)
    print(type(received))
    a = received.decode('utf-8')
    print(type(a), len(a))
    if a == "quit":
        break
    if a == "turn left":
        hi = 1 #this is how we do things
    print("Received Message:", a)
    sc.send(received)

print("Good bye!")

sc.close()
s.close()
a = input("Enter key to End:")