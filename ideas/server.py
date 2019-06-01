import socket
import time

"""
Version: 0.1a

Server:
    -> Broadcasts a message
    -> Recognize all client nodes
    -> Send commands to client nodes

    TEST IMPLEMENTATION:
        -> Transmit messages to the client nodes to display

"""
class Server:
    
    def __init__(self, ip, port, trans_p):
        self.IP = ip
        self.PORT = port
        self.TRANS_P = trans_p
    
    def init_socket(self):
        # Create socket for the server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        # Set timeout
        self.server.settimeout(0.2)

        # Bind the socket
        self.server.bind((self.IP, self.PORT))
        
    def start_transmit(self):

        # Initialize the socket
        self.init_socket()

        # Transmit the message
        message = b'I am SERVER'
        
        while 1:
            self.server.sendto(message, ('<broadcast>', self.TRANS_P))
            print("[LOG] message: {0} has been sent!".format(message))

            # Sleep for sometime
            time.sleep(1)


def main():
    server = Server("", 44444, 37020)
    server.start_transmit()

if __name__ == "__main__":
    main()
