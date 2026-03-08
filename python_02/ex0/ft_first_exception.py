# exception = An event that interrupts the flow of a program
# (ZeroDivisionError, TypeError, ValueError)


def check_temperature(temp_str: str):
    """
    Validate and evaluate a temperature value provided as a string.

    This function attempts to convert the input string into an integer.
    If the conversion succeeds, the temperature is checked against
    acceptable limits for plants (0°C to 40°C inclusive).

    - If temperature < 0 → returns a "too cold" error message.
    - If temperature > 40 → returns a "too hot" error message.
    - Otherwise → returns a message indicating the temperature is suitable.

    If the input cannot be converted to an integer, a ValueError is caught
    and a descriptive error message is returned instead of crashing.

    Args:
        temp_str (str): The temperature value as a string.

    Returns:
        str: A message describing whether the temperature is valid,
             suitable, or invalid.
    """
    try:
        to_test = int(temp_str)
        print(f"\nTesting temperature: {to_test}")
        if to_test < 0:
            return f"Error: {to_test}°C is too cold for plants (min 0°C)"
        elif to_test > 40:
            return f"Error: {to_test}°C is too hot for plants (max 40°C)"
        else:
            return f"Temperature {to_test}°C is perfect for plants!"
    except ValueError:
        print(f"\nTesting temperature: {temp_str}")
        return f"Error: '{temp_str}' is not a valid number"


def test_temperature_input():
    """
    Execute predefined test cases for the temperature validation function.

    This function tests different scenarios:
    - A valid temperature within range.
    - A non-numeric input (triggers ValueError handling).
    - A temperature above the allowed maximum.
    - A temperature below the allowed minimum.

    The purpose is to demonstrate that exception handling prevents
    the program from crashing when invalid input is provided.
    """
    # Test 1
    print(check_temperature("25"))

    # Test 2
    print(check_temperature("abc"))

    # Test 3
    print(check_temperature("100"))

    # Test 4
    print(check_temperature("-50"))

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
