import socket

"""
Version: 0.1a

Client:
    -> Waits for broadcast from server
    -> Aligns to the given server
    -> If the current server is different broadcasted
        -> Realign to new server

    -> Wait for commands for server

    TEST IMPLEMENTATION:
        -> Only displays the basic messages transmitted

"""

class Client:

    def __init__(self, ip, port):
        # Get the 
        self.IP = ip
        self.PORT = port

    def start_listen(self):
        # Create a socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        # Bind it
        self.client.bind((self.IP, self.PORT))

        # Listen for messages
        while True:
            # Get the data and the address for the message
            data, addr = self.client.recvfrom(1024)
            print("Received message: {0}".format(data))
            

            # Send OK to server and setup the initialization
            self.client.connect(addr)
            self.client.sendall(b'OK')


def main():
    clt = Client("", 37020)
    clt.start_listen()


if __name__ == "__main__":
    main()
