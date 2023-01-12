import multiprocessing
import random
import sys
import time


# known_peers = [1]

# known_peers.append(1)


def create_node(known_peers, this, neighbour):
    print("node created with numbers: " + str(this) + " and " + str(neighbour))

    if neighbour not in known_peers and neighbour != 0:
        known_peers.append(neighbour)
        # known_peers[0] = neighbour
        print("new node added to known nodes: " + str(neighbour))
    elif neighbour == 0:
        print("no new node added to known nodes")

    show_known_peers(known_peers)


# def receive_message():
#     try:
#         print("receiving message")


def main():
    known_peers = []

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

                    process = multiprocessing.Process(target=create_node, args=(known_peers, this, neighbour))
                    process.start()
                    process.join()
        except KeyboardInterrupt:
            sys.exit(0)


def show_known_peers(known_peers):
    print("known peers: " + str(known_peers))


if __name__ == "__main__":
    main()
