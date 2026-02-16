import socket
import threading

HOST = input("Enter server IP (use 127.0.0.1 for same PC): ")
PORT = 5002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")


def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            print("\n" + msg)
        except:
            print("Disconnected from server")
            break


def send():
    while True:
        msg = input()
        full_msg = f"{name}: {msg}"
        client.send(full_msg.encode())


threading.Thread(target=receive, daemon=True).start()
send()
