import socket

def connect_peer(peer, neighbour):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")

    port = peer

    s.connect(("localhost", port))

    msg = input(f"enter message to send to {peer}: ")