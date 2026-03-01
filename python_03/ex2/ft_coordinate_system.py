import math
import sys


def create_position(x: int, y: int, z: int):
    """Create a 3D position tuple from x, y, z coordinates."""
    return (x, y, z)


def distance_3d(cor1: tuple[int, int, int],
                cor2: tuple[int, int, int]) -> float:
    """
    Calculate the Euclidean distance between two 3D coordinates.

    Args:
        cor1: First coordinate as a tuple (x1, y1, z1).
        cor2: Second coordinate as a tuple (x2, y2, z2).

    Returns:
        The distance between the two points as a float.
    """
    x1, y1, z1 = cor1
    x2, y2, z2 = cor2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(cord_str: str) -> tuple[int, int, int]:
    """
    Convert a comma-separated string of coordinates into a tuple of integers.
    """
    x, y, z = cord_str.split(",")

    return int(x), int(y), int(z)


if __name__ == "__main__":

    print("=== Game Coordinate System ===\n")

    if len(sys.argv) > 1:
        if len(sys.argv) != 3:
            print("Usage: python3 ft_coordinate_system.py "
                  "<x1,y1,z1> <x2,y2,z2>")
            print('Example: python3 ft_coordinate_system.py "1,2,3" "2,3,4"')
        else:
            cord1_str = sys.argv[1]
            cord2_str = sys.argv[2]
            try:
                print(f'Parsing coordinates: "{cord1_str}" and "{cord2_str}"')

                parsed_coord1 = parse_coordinates(cord1_str)
                parsed_coord2 = parse_coordinates(cord2_str)

                print(f"Parsed Positions: {parsed_coord1} , "
                      + f"{parsed_coord2}")

                print(
                    f"Distance between {parsed_coord1} "
                    + f"and {parsed_coord2}: "
                    + f"{distance_3d(parsed_coord2 , parsed_coord1):.2f}"
                )

                print("\nUnpacking demonstration:")
                player_position = parse_coordinates(cord2_str)
                x, y, z = player_position
                print(f"Player at x={x}, y={y}, z={z}")
                print(f"Coordinates: X={x}, Y={y}, Z={z}")

            except Exception as err:
                print("Error parsing coordinates: ", err)
                print(
                    "Error details - Type: " +
                    f"{type(err).__name__}, Args: {err.args}"
                )

    else:
        position_zero = (0, 0, 0)
        try:
            player_position = create_position(10, 20, 5)
            print("Position created: ", player_position)
            distance_between = distance_3d(player_position, position_zero)
            print(
                f"Distance between {position_zero} "
                + f"and {player_position}: {distance_between:.2f}"
            )

            cord_str = "3,4,0"
            parsed_coordinates = parse_coordinates(cord_str)
            print(f'\nParsing coordinates: "{cord_str}"')
            print("Parsed position: ", parsed_coordinates)
            print(
                f"Distance between {position_zero} "
                + f"and {parsed_coordinates}: "
                + f"{distance_3d(parsed_coordinates , position_zero)}"
            )

            invalid_cord = "abc,def,ghi"
            print(f'\nParsing invalid coordinates: "{invalid_cord}"')
            parse_coordinates(invalid_cord)
        except Exception as e:
            print("Error parsing coordinates: ", e)
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

        print("\nUnpacking demonstration:")
        player_position = (3, 4, 0)
        x, y, z = player_position
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
