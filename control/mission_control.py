# create client socket class (MissionControlClient) to connect to the rover (RoverServer) and send commands to it.

from abc import ABC, abstractmethod
from typing import Callable

class IRoverInterpreter(ABC):
    @abstractmethod
    def sent(command: str) -> object:
        pass

class IMessageDecoder(ABC):
    @abstractmethod
    def decode(message: str) -> str:
        pass

class ICommandListener(ABC):
    @abstractmethod
    def subscribe(callback: Callable[[str], RoverState]):
        pass

class ICommandSender(ABC):
    @abstractmethod
    def send(command: str) -> RoverState:
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
    return f'BEGIN:{command}:CRC:END'

class MissionControl:
    def __init__(self, commandSender: ICommandSender, rover: IRoverInterpreter):
        self.__commandSender = commandSender
        self.__rover = rover

    def send(self, command: str) -> RoverState:
        self.__commandSender.send(command)
        self.__rover.receive(command)
        return self.__rover.getState()
