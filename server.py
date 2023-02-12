import socket               # Import socket module
import threading

import functions

host = '127.0.0.1' # Get local machine name
port = 55555       # Reserve a port for your service.
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        print(f'{addr} has joined')
        new_thread_rec=threading.Thread(target=functions.on_new_client_receive, args=(conn, addr))
        # new_thread_send = threading.Thread(target=functions.on_new_client_send, args=(conn, addr))
        new_thread_rec.start()
        # new_thread_send.start()
