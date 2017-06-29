# Echo client
import socket

class StartSocket:


    def start(slef):
        HOST = '127.0.0.1'
        PORT = 5000

        sock = socket.socket()
        sock.connect((HOST, PORT))

        while True:
            # Send to server to receive data
            sock.send('p')
            # Receive data array
            data = sock.recv(1024)
            print("Received array data server\n")

            #

        sock.close()
        return data


if __name__ == '__main__':
    StartSocket()