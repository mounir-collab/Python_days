class GardenError(Exception):
    """
    Base exception class for all garden-related errors.

    This class serves as the parent exception for more specific
    garden error types. It allows catching all garden errors
    using a single exception type.
    """
    pass


class PlantError(GardenError):
    """
    Exception raised for problems related to plants.

    Attributes:
        message (str): Description of the plant-related issue.
    """

    def __init__(self, message="Something wrong!"):
        """
        Initialize a PlantError instance.

        Args:
            message (str): Custom error message describing the issue.
        """
        super().__init__(message)


class WaterError(GardenError):
    """
    Exception raised for water-related problems in the garden.

    Attributes:
        message (str): Description of the water-related issue.
    """

    def __init__(self, message="Something wrong!"):
        """
        Initialize a WaterError instance.

        Args:
            message (str): Custom error message describing the issue.
        """
        super().__init__(message)


def check_plant():
    """
    Simulate a plant health check.

    Raises:
        PlantError: If the plant is detected to be in poor condition.
    """
    raise PlantError("The tomato plant is wilting!")


def check_water():
    """
    Simulate a water supply check.

    Raises:
        WaterError: If the water level is insufficient.
    """
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    try:
        print("\nTesting PlantError...")
        check_plant()
    except PlantError as e:
        print("Caught PlantError: ", e)

    try:
        print("\nTesting WaterError...")
        check_water()
    except WaterError as e:
        print("Caught WaterError: ", e)

    L_errors = [check_plant, check_water]
    print("\nTesting catching all garden errors...")
    for check in L_errors:
        try:
            check()
        except GardenError as e:
            print("Caught a garden error: ", e)
    print("\nAll custom error types work correctly!")
