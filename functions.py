clients=set()
address={}
messages=[]

def on_new_client_receive(clientsocket, addr):
    global address
    global messages
    global clients
    while True:
        if clientsocket not in clients:
            clients.add(clientsocket)
        if addr not in address:
            msg = clientsocket.recv(1024)
            messages.append((addr, msg))
            address[addr] = msg
            print(addr, ' >>> ', msg)
            msg = f"SERVER>>>Welcome to chat, {addr[0]}".encode()
            clientsocket.sendall(msg)
        else:
            msg = clientsocket.recv(1024)
            print(address[addr], ' >>> ', msg)
            messages.append((addr, msg))
            for c in clients:
                if addr != c.getpeername():
                    c.sendall(msg)

# def on_new_client_send(clientsocket, addr):
#     global address
#     global messages
#     global clients
#     if clientsocket not in clients:
#         clients.add(clientsocket)
#     if addr not in address:
#         address[addr] = messages[0][1]
#         messages.pop(0)
#         msg = f"SERVER>>>Welcome to chat, {addr[0]}".encode()
#         clientsocket.sendall(msg)
#     else:
#         print(messages)
#         if len(messages)==0:
#             msg=input("SERVER>>> ")
#             clientsocket.sendall(('SERVER>>>'+msg).encode())
#         else:
#             msg=messages[0]
#             for c in clients:
#                 c.sendall(msg)
#             messages.pop(0)

