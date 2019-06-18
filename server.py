import socket
import time
import threading

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
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.broad_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.broad_server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        # Set timeout
        self.server.settimeout(0.2)

        # Bind the socket
        self.server.bind((self.IP, self.TRANS_P))

        self.broad_server.bind((self.IP, self.PORT))
    
    def generateKey(self):
        pass

    def setupClient(self):
        
        self.server.listen(10)

        while 1:
            try:
                conn, addr = self.server.accept()
                
                with conn:
                    print("Connected by: {0}".format(addr))
                    while 1:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print(data)

            except Exception as e:
                print("[ERR] setupClient")
                print(e)

    # Thread that handles response messages
    

    # Method to handle multiple concurrent requests
    

    def start_transmit(self):

        # Initialize the socket
        self.init_socket()

        # Transmit the message
        message = b'I am SERVER'
        
        # Listening for responses on a different thread

        handle_client = threading.Thread(target=self.setupClient)
        handle_client.start()

        # Broadcasting thread
        broad_thread = threading.Thread(target=self.broadcast_thread, args=(message,))
        broad_thread.start()

    def broadcast_thread(self, message):
        while 1:
            try:
                self.broad_server.sendto(message, ('<broadcast>', self.TRANS_P))
                print("[LOG] message: {0} has been sent!".format(message))
            except Exception as e:
                print("[LOG] We are breaking mate!\n")
                print(e)

                break

            # Sleep for sometime
            time.sleep(1)


def main():
    server = Server("", 1034, 37020)
    server.start_transmit()

if __name__ == "__main__":
    main()
