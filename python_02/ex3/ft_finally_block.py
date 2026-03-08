def water_plants(plant_list):
    """
    Simulates watering a list of plants.

    The function opens a watering system, iterates through the given
    list of plants, and waters each valid plant. A plant is considered
    valid if it is a non-empty string.

    If an invalid plant (e.g., None or empty string) is encountered,
    an Exception is raised and caught inside the function. The error
    message is displayed, and the watering system is properly closed
    using the finally block.

    Parameters:
        plant_list (list): A list containing plant names as strings.

    Raises:
        Exception: If a plant is not a valid non-empty string.
    """
    print("Opening watering system")

    for plant in plant_list:
        if not isinstance(plant, str) or plant == "":
            raise Exception(f"Cannot water {plant} - invalid plant!")
        print("Watering ", plant)


def test_watering_system():
    """
    Tests the watering system with valid and invalid plant lists.

    This function demonstrates:
    - Normal watering behavior with valid plant names.
    - Error handling when encountering invalid plant entries.
    - Guaranteed cleanup behavior via the finally block.
    """
    plants_garden = ["tomato", "lettuce", "carrots"]
    plants_Err = ["tomato", None]

    print("\nTesting normal watering...")
    try:
        water_plants(plants_garden)
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")

    print("\nTesting with error...")
    try:
        water_plants(plants_Err)
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Closing watering system (cleanup)")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
