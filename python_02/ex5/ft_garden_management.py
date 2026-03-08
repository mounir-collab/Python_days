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


class Plant:
    """Represents a plant with a name, water level, and sunlight hours."""
    def __init__(self, plant_name, water_level=0, sunlight_hours=0):
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """Manages a collection of plants,
    watering operations, and health checks."""
    def __init__(self, name_manager: str):
        self.name_manager = name_manager
        self.garden_plants = []
        self.water_in_tank = 10

    def add_plant(self, plant: Plant):
        """Adds a plant to the garden after validating its name."""
        try:
            if not isinstance(plant.plant_name, str) or plant.plant_name == "":
                raise PlantError("Plant name cannot be empty!")
            else:
                self.garden_plants.append(plant)
                print(f"Added {plant.plant_name} successfully")
        except PlantError as e:
            print("Error adding plant: ", e)

    def water_plants(self):
        """Waters all plants and decreases the water tank level,
        ensuring cleanup."""
        print("Opening watering system")

        try:
            for plant in self.garden_plants:
                plant.water_level += 1
                self.water_in_tank -= 1
                print(f"Watering {plant.plant_name} - success")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant(plant: Plant):
        """Validates water and sunlight levels
        and raises errors if unhealthy."""
        if plant.water_level < 1 or plant.water_level > 10:
            if plant.water_level < 1:
                message = f"Water level {plant.water_level} is too low (min 1)"
                raise WaterError(message)
            else:
                raise WaterError(
                    f"Water level {plant.water_level} is too high (max 10)"
                )
        elif plant.sunlight_hours < 2 or plant.sunlight_hours > 12:
            if plant.sunlight_hours < 2:
                raise PlantError(
                    f"Sunlight hours {plant.sunlight_hours} is too low (min 2)"
                )
            else:
                raise PlantError(
                    "Sunlight hours "
                    + str(plant.sunlight_hours)
                    + "is too high (max 12)"
                )
        print(
            str(plant.plant_name)
            + ": healthy (water: "
            + str(plant.water_level)
            + ", sun: "
            + str(plant.sunlight_hours)
            + ")"
        )

    def check_plant_health(self):
        """Checks the health of all plants and handles potential errors."""
        for plant in self.garden_plants:
            try:
                GardenManager.check_plant(plant)
            except (WaterError, PlantError) as e:
                print(f"Error checking {plant.plant_name}: ", e)

    def check_water_in_tank(self):
        """Verifies sufficient water in the tank
        and handles low-level errors."""
        try:
            if self.water_in_tank < 20:
                raise GardenError("Not enough water in tank")
        except GardenError as e:
            print("Caught GardenError: ", e)


def test_garden_management():
    """Demonstrates the garden management workflow and error handling."""
    mounit = GardenManager("mounit")

    tomato = Plant("tomato", 4, 8)
    lettuce = Plant("lettuce", 14)
    carrot = Plant("")

    print("\nAdding plants to garden...")
    mounit.add_plant(tomato)
    mounit.add_plant(lettuce)
    mounit.add_plant(carrot)

    print("\nWatering plants...")
    mounit.water_plants()

    print("\nChecking plant health...")
    mounit.check_plant_health()

    print("\nTesting error recovery...")
    mounit.check_water_in_tank()
    print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===")
    test_garden_management()
    print("\nGarden management system test complete!")
