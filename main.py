"""Runs calculator program on command-line interface.

Typical usage example (in command-line interface):
>> python main.py

"""

from typing import Optional, Tuple
from src.calculator import Calculator


def run_calculator():
    """The driver function for the Calculator program.

        Instantiates Calculator object and handles the operations of the program.
        The program collects numerical inputs and performs mathematical operations based on user's selection.
        Exceptions are handled by printing a human-readable string.

    """
    input_number1 = _collect_input_number("Enter first number: ")
    input_number2 = _collect_input_number("Enter second number: ")
    calc_obj = Calculator(input_number1, input_number2)
    current_option = None

    while current_option != "6":
        print("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Reset Calculator Inputs \n6. Exit")
        current_option = input("Pick an option: ")
        if current_option == "1":
            _print_result(calc_obj.add())
        elif current_option == "2":
            _print_result(calc_obj.subtract())
        elif current_option == "3":
            _print_result(calc_obj.multiply())
        elif current_option == "4":
            _print_result(calc_obj.divide())
        elif current_option == "5":
            input_number1 = _collect_input_number("Enter first number: ")
            input_number2 = _collect_input_number("Enter second number: ")
            calc_obj.reset(input_number1, input_number2)
        elif current_option == "6":
            print("Exiting program now.")
        else:
            print("Invalid choice. Please choose one of the six options below.")


def _convert_to_float(input_string: str) -> Optional[float]:
    """Converts the input of string type to a float type.

        This function converts the input returned by input() as a string to a float type.
        If it is unsuccessful in conversion, it prints a human readable error message and returns None.

        Args:
            input_string: the option entered by the user as a string.

        Returns:
            If successful, it returns the converted input as float.
            If unsuccessful, it prints an error message to the user and returns None.
    """
    try:
        input_float = float(input_string)
    except ValueError:
        print("Your input could not be converted to a number. Try entering a number.")
        return None
    else:
        return input_float


def _collect_input_number(prompt: str) -> float:
    """Collects the input, converts to float and returns the input number.

        This function collects the input, and converts it to a float.
        If input number is too large, it prints a human readable error message and resets input_number to None.

        Args:
            prompt: the string message displayed to the user e.g. "Enter first number"

        Returns:
            If successful, it returns the number entered by the user.
            If unsuccessful, it prints an error message and asks the user to re-enter the input.
            The function does not return until a valid number is entered by the user.
    """
    input_number = None
    while input_number is None:
        input_string = input(prompt)
        input_number = _convert_to_float(input_string)
        if input_number == float("inf") or input_number == float("-inf"):
            print("The number you entered is too large. Please try a smaller number.")
            input_number = None
    return input_number


def _print_result(result: Tuple[Optional[float], Optional[str]]):
    """Prints the results of the operation performed on the numerical inputs.

        This function takes the result (a tuple) as an argument,
        and prints the appropriate response based on if the operation was successful.
        If the first element of the tuple is not None, the operation is successful and it prints the numerical result.
        If the second element of the tuple is not None, the operation is unsuccessful and it prints the error message.

        Args:
            result: the tuple returned from the Calculator class methods
    """
    if result[0] is not None:
        print("Result: ", result[0])
    elif result[1] is not None:
        print(result[1])
    else:
        print("Something went wrong. Please try again.")


run_calculator()
