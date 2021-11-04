"""This file contains the Calculator class that conducts basic mathematical operations.

Typical example:
calc_obj = Calculator(5, 2)
calc_obj.add()
>> 7

"""

from typing import Union, Optional, Tuple

numType = Union[int, float]
returnType = Tuple[Optional[numType], Optional[str]]


class Calculator:
    """The Calculator class is used to conduct mathematical operations on two numerical inputs.

    It contains the following operations as methods: addition, subtraction, multiplication and division.
    Each method for a mathematical operation returns a tuple.
    If the operation is successful, it returns the numerical result and no message.
    If the operation is unsuccessful, it returns no numerical result and an error message.

    Attributes:
        num1: The first numerical input of int or float type.
        num2: The second numerical input of int or float type.
    """
    def __init__(self, num1: numType, num2: numType):
        """Initializes Calculator class with num1 and num2 as its numerical inputs."""
        self.num1 = num1
        self.num2 = num2

    def add(self) -> returnType:
        """Performs addition operation on the two inputs."""
        return self.num1 + self.num2, None

    def subtract(self) -> returnType:
        """Performs subtraction operation on the two inputs."""
        return self.num1 - self.num2, None

    def multiply(self) -> returnType:
        """Performs multiplication operation on the two inputs."""
        return self.num1 * self.num2, None

    def divide(self) -> returnType:
        """Performs division operation on the two inputs."""
        try:
            result = self.num1 / self.num2
        except ZeroDivisionError:
            return None, "Cannot divide by zero. Please select another operator or choose option 5 to reset inputs."
        else:
            return result, None

    def reset(self, num1: numType, num2: numType):
        """Resets the calculator so the user is able to change inputs without exiting the program."""
        self.num1 = num1
        self.num2 = num2
