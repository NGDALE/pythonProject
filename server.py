import socket


def create_node(this, neighbour):
    known_peers = []

    print("node created with numbers: " + str(this) + " and " + str(neighbour))

    if neighbour not in known_peers and neighbour != 0:
        known_peers.append(neighbour)
        # known_peers[0] = neighbour
        print("new node added to known nodes: " + str(neighbour))
    elif neighbour == 0:
        print("no new node added to known nodes")

    show_known_peers(known_peers)

    while True:

        match input("listen (l) , message (m), show known peers (s), send heartbeat (h) mode: "):
            case "l":
                s = initiate_socket(this)
                s.listen(5)
                print("socket is listening")

                while True:
                    c, addr = s.accept()
                    print('Got connection from', addr)
                    received = c.recv(1024).decode()

                    if received == "heartbeat":
                        print("heartbeat received")
                        known_peers.append(addr[1])
                    else:
                        print("received message: " + received)

                    c.close()
                    print("connection closed")
                    break
            case "m":
                s = initiate_socket(this)
                if len(known_peers) == 0:
                    print("no known peers")
                    s.close()
                else:
                    receiver = known_peers[0]
                    s.connect(("localhost", receiver))
                    print("connected to " + str(receiver))
                    msg = input(f"enter message to send to {receiver}: ")
                    s.send(msg.encode())
                    s.close()
                    print("connection closed")
            case "s":
                show_known_peers(known_peers)
            case "h":
                for i in range(len(known_peers)):
                    try:
                        s = initiate_socket(this)
                        s.connect(("localhost", known_peers[i]))
                        print("connected to " + str(known_peers[i]))
                        msg = "heartbeat"
                        s.send(msg.encode())
                        s.close()
                        print("connection closed")
                    except ConnectionRefusedError:
                        bad = known_peers[i]
                        print("connection refused to " + str(bad))
                        known_peers.remove(bad)
                        print("removed " + str(bad) + " from known peers")


def show_known_peers(known_peers):
    print("known peers: " + str(known_peers))


def initiate_socket(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    print("socket bound to %s" % port)
    return s
