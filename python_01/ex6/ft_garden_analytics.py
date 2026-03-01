class GardenManager:
    """
    Manages a garden and its plants.

    Attributes:
        owner_name (str): Name of the garden owner.
        all_plants (list): List of plants in this garden.
        total_growth (int): Total growth accumulated in the garden (in cm).

    Class Attributes:
        all_gardens (list): List of all garden instances.
        counter (int): Total number of gardens created.
    """

    all_gardens = []
    counter = 0

    def __init__(self, owner_name):
        """
        Initialize a new GardenManager instance.

        Args:
            owner_name (str): The name of the garden owner.
        """
        self.owner_name = owner_name
        self.all_plants = []
        self.total_growth = 0
        GardenManager.all_gardens.append(self)
        GardenManager.counter += 1

    @classmethod
    def create_garden_network(cls, owner_name):
        """
        Alternative constructor to create a new garden.

        Args:
            owner_name (str): Name of the garden owner.

        Returns:
            GardenManager: A new instance of GardenManager.
        """
        return cls(owner_name)

    @classmethod
    def total_gardens(cls):
        """
        Return the total number of gardens created.

        Returns:
            int: Number of GardenManager instances.
        """
        return cls.counter

    def add_plant(self, plant):
        """
        Add a plant to the garden.

        Args:
            plant (Plant): The plant instance to add.
        """
        self.all_plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_plants(self):
        """
        Increase the height of all plants in the garden by 1 cm.
        Updates total growth counter.
        """
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.all_plants:
            plant.describe_growing()
            self.total_growth += 1

    def show_report(self):
        """
        Display a detailed report of the garden,
        including plant information and statistics.
        """
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.all_plants:
            print("-", plant.display_info())

        stats = GardenManager.GardenStats(self)
        stats.show_statistics()

    def calculate_score(self):
        """
        Calculate the total garden score.

        Score calculation rules:
        - Base score: sum of plant heights.
        - +15 points for each FloweringPlant.
        - +prize_points for each PrizeFlower.

        Returns:
            int: Total calculated score.
        """
        score = 0
        for plant in self.all_plants:
            score += plant.height
            if isinstance(plant, FloweringPlant):
                score += 15
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

    @staticmethod
    def validate_height(height):
        """
        Validate that plant height is non-negative.

        Args:
            height (int or float): Height value to validate.

        Returns:
            bool: True if height >= 0, otherwise False.
        """
        return height >= 0

    class GardenStats:
        """
        Inner class responsible for computing
        and displaying garden statistics.
        """

        def __init__(self, garden):
            """
            Initialize GardenStats with a specific garden.

            Args:
                garden (GardenManager): Garden instance to analyze.
            """
            self.garden = garden

        def show_statistics(self):
            """
            Display statistics about plant types
            and total growth in the garden.
            """
            regular = 0
            flowering = 0
            prize_flowers = 0

            for plant in self.garden.all_plants:
                if isinstance(plant, PrizeFlower):
                    prize_flowers += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            print("")
            print(
                f"Plants added: {len(self.garden.all_plants)}, "
                f"Total growth: {self.garden.total_growth}cm"
            )
            print(
                f"Plant types: {regular} regular, "
                f"{flowering} flowering, "
                f"{prize_flowers} prize flowers"
            )


class Plant:
    """
    Represents a basic plant.

    Attributes:
        name (str): Name of the plant.
        height (int): Current height of the plant (in cm).
    """

    def __init__(self, name, height):
        """
        Initialize a plant.

        Args:
            name (str): Plant name.
            height (int): Initial height in centimeters.
        """
        self.name = name
        self.height = height

    def describe_growing(self):
        """
        Increase plant height by 1 cm
        and display growth message.
        """
        self.height += 1
        print(f"{self.name} grew 1cm")

    def display_info(self):
        """
        Return formatted plant information.

        Returns:
            str: Plant description.
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    Represents a flowering plant.

    Attributes:
        color (str): Flower color.
    """

    def __init__(self, name, height, color):
        """
        Initialize a flowering plant.

        Args:
            name (str): Plant name.
            height (int): Initial height.
            color (str): Flower color.
        """
        super().__init__(name, height)
        self.color = color

    def display_info(self):
        """
        Return formatted flowering plant information.

        Returns:
            str: Flowering plant description.
        """
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """
    Represents a flowering plant that earns prize points.

    Attributes:
        prize_points (int): Additional score points.
    """

    def __init__(self, name, height, color, prize_points):
        """
        Initialize a prize flower.

        Args:
            name (str): Plant name.
            height (int): Initial height.
            color (str): Flower color.
            prize_points (int): Extra scoring points.
        """
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def display_info(self):
        """
        Return formatted prize flower information.

        Returns:
            str: Prize flower description.
        """
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


print("=== Garden Management System Demo ===\n")

alice = GardenManager("Alice")
alice.add_plant(Plant("Oak Tree", 100))
alice.add_plant(FloweringPlant("Rose", 25, "red"))
alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

alice.grow_plants()
alice.show_report()


print("\nHeight validation test:", GardenManager.validate_height(10))
print(f"Garden scores - {alice.owner_name}: {alice.calculate_score()}")
print(f"Total gardens managed: {GardenManager.total_gardens()}")
