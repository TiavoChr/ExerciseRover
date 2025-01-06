from abc import ABC, abstractmethod
from typing import Callable

class IRoverInterpreter(ABC):
    """
    Interface for interpreting commands sent to the rover.
    """

    @abstractmethod
    def sent(command: str) -> object:
        """
        Process a command sent to the rover.

        Args:
            command (str): The command to be processed.

        Returns:
            object: Result or state after processing the command.
        """
        pass

class IMessageDecoder(ABC):
    """
    Interface for decoding messages sent over the communication channel.
    """

    @abstractmethod
    def decode(message: str) -> str:
        """
        Decode a received message into a readable command.

        Args:
            message (str): The raw message to decode.

        Returns:
            str: The decoded command.
        """
        pass

class ICommandListener(ABC):
    """
    Interface for subscribing to command notifications.
    """

    @abstractmethod
    def subscribe(callback: Callable[[str], "RoverState"]):
        """
        Subscribe to commands with a callback function.

        Args:
            callback (Callable[[str], RoverState]): Function to be called when a command is received.
        """
        pass

class ICommandSender(ABC):
    """
    Interface for sending commands to the rover.
    """

    @abstractmethod
    def send(command: str) -> "RoverState":
        """
        Send a command to the rover.

        Args:
            command (str): The command to be sent.

        Returns:
            RoverState: The rover's state after processing the command.
        """
        pass

# Utility function: Decode command from a TCP message formatted as "BEGIN:command:END"
def decode_message_to_command(message: str) -> str:
    """
    Extract and decode a command from a structured TCP message.

    Args:
        message (str): The raw TCP message containing the command.

    Returns:
        str: The extracted command if the format is valid, None otherwise.
    """
    if not message.startswith('BEGIN:') or not message.endswith(':END'):
        return None
    return message[6:-4]  # Extract the command between BEGIN: and :END

# @deprecated
# This function is deprecated and should not be used in new implementations.
def encode_command_to_message(command: str) -> str:
    """
    Encode a command into a structured TCP message format.

    Args:
        command (str): The command to encode.

    Returns:
        str: The encoded TCP message.
    """
    return f'BEGIN:{command}:CRC:END'

class MissionControl:
    """
    The MissionControl class coordinates communication with the rover.
    It sends commands and interacts with the rover's interpreter.
    """

    def __init__(self, commandSender: ICommandSender, rover: IRoverInterpreter):
        """
        Initialize the MissionControl instance.

        Args:
            commandSender (ICommandSender): Object responsible for sending commands.
            rover (IRoverInterpreter): Object responsible for interpreting rover commands.
        """
        self.__commandSender = commandSender
        self.__rover = rover

    def send(self, command: str) -> "RoverState":
        """
        Send a command to the rover and update its state.

        Args:
            command (str): The command to send to the rover.

        Returns:
            RoverState: The rover's updated state after processing the command.
        """
        self.__commandSender.send(command)
        self.__rover.receive(command)
        return self.__rover.getState()
