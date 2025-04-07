# Error Handling in Python
# Summary: This script demonstrates various techniques for handling errors in Python.
# It includes basic try-except blocks, handling multiple exceptions, using else and finally,
# raising exceptions manually, defining custom exceptions, nested try-except blocks,
# assertions, and logging exceptions.

try:
    # Attempting to divide by zero, which raises a ZeroDivisionError
    result = 10 / 0
except ZeroDivisionError as e:
    # Handling the error and printing a message
    print(f"Error: {e}")

# Example 2: Catching multiple exceptions
try:
    undefined_variable = "This is  defined variables"
    # Attempting to access an undefined variable
    print(undefined_variable)
except (ZeroDivisionError, NameError) as e:
    # Handling multiple types of errors
    print(f"Error: {e}")

# Example 3: Using else with try-except
try:
    # A block of code that does not raise an exception
    result = 10 / 2
except ZeroDivisionError as e:
    # This block will not execute because no error occurs
    print(f"Error: {e}")
else:
    # This block executes if no exception is raised
    print(f"Result is: {result}")

# Example 4: Using finally to execute cleanup code
try:
    # Attempting to open a file that does not exist
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    # Handling the file not found error
    print(f"Error: {e}")
finally:
    # This block executes no matter what
    print("Execution of the try-except block is complete.")

# Example 5: Raising exceptions manually
try:
    # Raising a custom exception
    raise ValueError("This is a manually raised ValueError.")
except ValueError as e:
    # Handling the manually raised exception
    print(f"Error: {e}")

# Example 6: Defining and using custom exceptions
class CustomError(Exception):
    """A custom exception class."""
    pass

try:
    # Raising the custom exception
    raise CustomError("This is a custom error.")
except CustomError as e:
    # Handling the custom exception
    print(f"Error: {e}")

# Example 7: Nested try-except blocks
try:
    try:
        # Attempting an operation that raises an exception
        result = 10 / 0
    except ZeroDivisionError as e:
        # Handling the inner exception
        print(f"Inner Error: {e}")
        # Raising a new exception
        raise ValueError("A new error occurred.") from e
except ValueError as e:
    # Handling the outer exception
    print(f"Outer Error: {e}")

# Example 8: Using assertions for error checking
try:
    # Using an assertion to validate a condition
    x = -1
    assert x >= 0, "x must be non-negative"
except AssertionError as e:
    # Handling the assertion error
    print(f"Assertion Error: {e}")

# Example 9: Logging exceptions (optional)
import logging

# Configuring the logging module
logging.basicConfig(level=logging.ERROR)

try:
    # Attempting an operation that raises an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Logging the error
    logging.error("An error occurred", exc_info=True)