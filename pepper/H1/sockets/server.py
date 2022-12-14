from ObjectRecognition import ObjectRecognition
import socket
import sys

class AzureConnector():

    def __init__(self):
        self.HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        self.PORT = 54321        # Port to listen on (non-privileged ports are > 1023)
        self.isReady = False

        print("starting python server with python version:")
        print(sys.version)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            conn, addr = s.accept()
            self.isReady = True
            with conn:
                print('Connected by', addr)
                print('Creating ObjectRecognition Object')
                or1 = ObjectRecognition()
                data = or1.getTagsEncoded()
                while True:
                    if not data:
                        break
                    conn.sendall(data)

    def isReady(self):
        return self.isReady()

if __name__ == "__main__":
    ac = AzureConnector()


