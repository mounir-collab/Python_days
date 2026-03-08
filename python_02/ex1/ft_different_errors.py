def garden_operations(type_error: str):
    """
    Intentionally trigger a specific built-in Python exception.

    This function is designed for educational purposes to demonstrate
    how different exceptions are raised. Based on the provided string,
    it executes code that will raise a corresponding exception.

    Supported error types:
        - "ValueError": Raised by attempting to convert a non-numeric
          string to an integer.
        - "ZeroDivisionError": Raised by dividing a number by zero.
        - "FileNotFoundError": Raised by attempting to open a file
          that does not exist.
        - "KeyError": Raised by accessing a non-existent key
          in a dictionary.

    Args:
        type_error (str): The name of the exception type to trigger.

    Raises:
        ValueError: If "ValueError" is provided.
        ZeroDivisionError: If "ZeroDivisionError" is provided.
        FileNotFoundError: If "FileNotFoundError" is provided.
        KeyError: If "KeyError" is provided.
    """
    if type_error == "ValueError":
        int("hello")
    elif type_error == "ZeroDivisionError":
        9 / 0
    elif type_error == "FileNotFoundError":
        open("missing.txt", "r")
    elif type_error == "KeyError":
        d = {"first_key": 12, "last_key": 21}
        print(d["no_thing"])


def test_error_types():
    """
    Demonstrate handling of multiple built-in Python exceptions.

    This function sequentially tests different exception scenarios
    by calling `garden_operations()` with predefined error types.
    Each call is wrapped in a try/except block to ensure that
    exceptions are caught and handled without terminating the program.

    The following exceptions are demonstrated:
        - ValueError
        - ZeroDivisionError
        - FileNotFoundError
        - KeyError
        - Multiple exception handling in a single except clause

    The final test shows how multiple exception types can be
    grouped together in one except statement, allowing the
    program to continue execution after an error occurs.
    """
    print("=== Garden Error Types Demo ===")

    List_Errors = ["ValueError",
                   "ZeroDivisionError",
                   "FileNotFoundError",
                   "KeyError"
                   ]

    print("\nTesting ValueError...")
    try:
        garden_operations(List_Errors[0])
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations(List_Errors[1])
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations(List_Errors[2])
    except FileNotFoundError as e:
        print("Caught FileNotFoundError: ", e)

    print("\nTesting KeyError...")
    try:
        d = {"first_key": 12, "last_key": 21}
        print(d["no_thing"])
    except KeyError as k:
        print("Caught KeyError: ", k)

    print("\nTesting multiple errors together...")
    try:
        9 / 0
        int("--1")
        d = {"key_1": 12, "key_2": 21}
        print(d["key_3"])
    except (ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
