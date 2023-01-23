import random
import sys
import time
import threading
import socket
import keyboard
import server

# known_peers = [1]

# known_peers.append(1)




# def receive_message():
#     try:
#         print("receiving message")

def main():
    while True:

        # process = multiprocessing.Process(target=create_node)
        # process.start()
        # process.join()
        # print("Process finished")

        try:
            match input("enter command: "):
                case "create node":
                    this = int(input("enter this node number: "))
                    neighbour = int(input("enter neighbour node number: "))

                    # match input("enter command in node settings: "):
                    #     case "show known peers":
                    #         show_known_peers(known_peers)

                    thread = threading.Thread(target=server.create_node(this, neighbour))
                    thread.start()
                    thread.join()

        except KeyboardInterrupt:
            sys.exit(0)


def show_known_peers(known_peers):
    print("known peers: " + str(known_peers))


if __name__ == "__main__":
    main()
