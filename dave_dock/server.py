from cmath import rect
from http import server
from socket import socket, AF_INET, SOCK_STREAM
import logging
from concurrent.futures import ThreadPoolExecutor


class ChatServer:
    def __init__(self, host, port):
        self.logger = self._setup_logger()
        self.sock = self._setup_socket(host, port)
        self.connections = []


    def run(self):
        self.logger.info("Chat server is running")
        with ThreadPoolExecutor() as executor:
            while True:
                # blocks and waits for incoming connections
                # returns tuple containing new socket object
                # with the connection and address of the client on the other end
                connection, address = self.sock.accept() 
                self.logger.debug(f"New Connection: {address}")

                self.connections.append(connection)
                self.logger.debug(f"Connections: {self.connections}")

                executor.submit(self.relay_messages, connection, address)


    def relay_messages(self, connection, address):
        while True:
            data  = connection.recv(4096)

            for connection in self.connections:
                connection.send(data)
            if not data:
                self.logger.warning("No data, exiting")
                break


    @staticmethod
    def _setup_logger():
        logger = logging.getLogger('chat_server')
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(logging.DEBUG)
        return logger

    @staticmethod
    def _setup_socket(host, port):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((host, port))
        sock.listen()
        return sock

if __name__ == "__main__":
    server = ChatServer('localhost',4333)
    server.run()