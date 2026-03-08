def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Validate plant health parameters and raise errors if values are invalid.

    This function verifies three aspects of plant care:
        1. The plant name must not be an empty string.
        2. The water level must be within the range [1, 10].
        3. The sunlight exposure must be within the range [2, 12].

    If any validation fails, a ValueError is raised with a descriptive
    message explaining the problem. If all values are valid, the function
    prints a confirmation message indicating that the plant is healthy.

    Args:
        plant_name (str): The name of the plant.
        water_level (int): Water level on a scale from 1 to 10.
        sunlight_hours (int): Daily sunlight exposure in hours (2 to 12).

    Raises:
        ValueError: If the plant name is empty.
        ValueError: If the water level is outside the allowed range.
        ValueError: If the sunlight hours are outside the allowed range.
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    elif water_level < 1 or water_level > 10:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        else:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours < 2:
            message = f"Sunlight hours {sunlight_hours} is too low (min 2)"
            raise ValueError(message)
        else:
            message = f"Sunlight hours {sunlight_hours} is too high (max 12)"
            raise ValueError(message)
    return (f"Plant '{plant_name}' is healthy")


def test_plant_checks():
    """
    Execute test cases for plant health validation.

    This function tests multiple scenarios:
        - Valid input values (no exception expected).
        - Empty plant name (ValueError expected).
        - Invalid water level (ValueError expected).
        - Invalid sunlight hours (ValueError expected).

    Each test is wrapped in a try/except block to demonstrate
    controlled error handling without terminating the program.
    """
    print("\nTesting good values...")
    try:
        print(check_plant_health("tomato", 3, 5))
    except ValueError as e:
        print("Error: ", e)

    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 3, 4))
    except ValueError as e:
        print("Error: ", e)

    print("\nTesting bad water level...")
    try:
        print(check_plant_health("tomato", 15, 4))
    except ValueError as e:
        print("Error: ", e)

    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 5, 0))
    except ValueError as e:
        print("Error: ", e)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
