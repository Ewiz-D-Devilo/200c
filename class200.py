import socket
from threading import Thread

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
iP_address='127.0.0.1'
port= 5000

server.bind((iP_address,port))
server.listen()

print("server has started")
list_of_clients=[]
def clientThread(conn,addr):
    print("welcome to this chatroom")
    conn.send("welcome to this chatroom".encode("utf-8"))
    while True:
        try:
            message=conn.recv(2048).decode("utf-8")
            if message:
                print(addr[0] + message)
                message_send="<"+addr[0]+">"+ message
                broadcast(message_send,conn)
            else:
                remove(conn)

        except:
            continue

def broadcast(messag,connection):
    for i in list_of_clients:
        if i!=connection:
            try:
                i.send(messag.encode("utf-8"))

            except:
                remove(i)

def remove(c):
    if c in list_of_clients:
        list_of_clients.remove(c)

while True:
    conn,addr=server.accept()
    #print(conn,addr)
    list_of_clients.append(conn)
    new_thread= Thread(target=clientThread,args=(conn,addr))
    new_thread.start()