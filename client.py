import socket
import threading

ya_socket=socket.socket()
addr=('127.0.0.1', 55555)
ya_socket.connect(addr)
print("Connected to server")
my_name = b"Andrey"
ya_socket.send(my_name)
print(f"Message {my_name} sent to Server")

def send_message():
    while True:
        ya_socket.send(bytes(input('>>>'), encoding='utf-8'))

def receive_message():
    while True:
        data=ya_socket.recv(1024)
        print(data)

rec_thread=threading.Thread(target=send_message)
rec_thread.start()

get_thread=threading.Thread(target=receive_message)
get_thread.start()