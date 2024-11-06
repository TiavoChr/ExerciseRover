# create client socket class (MissionControlClient) to connect to the rover (RoverServer) and send commands to it.

import socket
import sys
from abc import ABC, abstractmethod

class IRoverInterpreter(ABC):
    @abstractmethod
    def sent(command: str) -> object:
        pass

class IMessageDecoder(ABC):
    @abstractmethod
    def decode(message: str) -> str:
        pass

class IMessageEncoder(ABC):
    @abstractmethod
    def encode(command: str) -> str:
        pass

class IMessenger(ABC):
    @abstractmethod
    def send(self, command: str):
        pass
    @abstractmethod
    def receive(self) -> str:
        pass
    @abstractmethod
    def close(self):
        pass

# get command in tcp message "BEGIN:command:END"
def decode_message_to_command(message: str) -> str:
    # decode the message to command
    # check if the message is in the correct format
    if not message.startswith('BEGIN:') or not message.endswith(':END'):
        return None
    # get the command
    return message[6:-4]

# @deprecated
def encode_command_to_message(command: str) -> str:
    return f'BEGIN:{command}:END'

class MissionControlClient:
    def __init__(self, host: str = '127.0.0.1', port: int = 24113):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def send(self, command: str):
        data = encode_command_to_message(command)
        self.client.send(data.encode())

    def receive(self) -> str:
        message = self.client.recv(1024).decode()
        return decode_message_to_command(message)

    def close(self):
        self.client.close()

# make RoverServer class to handle the connection from the rover

class RoverServer:
    def __init__(self, host: str = '127.0.0.1', port: int = 24113):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        self.client, self.addr = self.server.accept()

    def send(self, command: str):
        data = encode_command_to_message(command)
        self.client.send(data.encode())

    def receive(self) -> str:
        message = self.client.recv(1024).decode()
        return decode_message_to_command(message)

    def close(self):
        self.client.close()

class SocketCommunication(IMessenger):
    pass


# test on main function
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python mission_control.py [client|server]')
        sys.exit(1)

    if sys.argv[1] == 'client':
        client = MissionControlClient()
        client.send('Hello Rover!')
        print(client.receive())
        client.close()
    elif sys.argv[1] == 'server':
        server = RoverServer()
        print(server.receive())
        server.send('Hello Mission Control!')
        server.close()
    else:
        print('Usage: python mission_control.py [client|server]')
        sys.exit(1)
