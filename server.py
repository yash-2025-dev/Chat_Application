import socket
import threading

HOST = "0.0.0.0"
PORT = 5002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print("💬 Chat Server Started on port", PORT)


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)


def handle_client(conn, addr):
    print(f"✅ Connected: {addr}")
    clients.append(conn)

    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            print(f"{addr}: {msg.decode()}")
            broadcast(msg, conn)
        except:
            break

    clients.remove(conn)
    conn.close()
    print(f"❌ Disconnected: {addr}")


while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
