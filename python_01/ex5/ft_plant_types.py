class Plant:
    """
    Base class representing a generic plant.

    Attributes:
        name (str): Name of the plant.
        height (float): Height of the plant in centimeters.
        age (int): Age of the plant in days.
    """

    def __init__(self, name: str, height: float, age: int):
        """
        Initialize a Plant instance.

        Args:
            name (str): Plant name.
            height (float): Plant height in centimeters.
            age (int): Plant age in days.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Represents a flowering plant.

    Inherits from:
        Plant

    Attributes:
        color (str): Flower color.
    """

    def __init__(self, name, height, age, color):
        """
        Initialize a Flower instance.

        Args:
            name (str): Plant name.
            height (float): Height in centimeters.
            age (int): Age in days.
            color (str): Flower color.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Simulate the flower blooming.
        """
        print(f"{self.name} is blooming beautifully!")

    def show_info(self):
        """
        Display detailed information about the flower.
        """
        print(
            "\n"
            + self.name
            + " (Flower): "
            + str(self.height)
            + "cm, "
            + str(self.age)
            + " days, "
            + self.color
            + " color"
        )


class Tree(Plant):
    """
    Represents a tree.

    Inherits from:
        Plant

    Attributes:
        trunk_diameter (float): Diameter of the tree trunk in centimeters.
    """

    def __init__(self, name, height, age, trunk_diameter):
        """
        Initialize a Tree instance.

        Args:
            name (str): Tree name.
            height (float): Height in centimeters.
            age (int): Age in days.
            trunk_diameter (float): Diameter of the trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Calculate and display the approximate shade area
        produced by the tree based on trunk diameter.
        """
        print(
            self.name
            + " provides "
            + str(f"{self.trunk_diameter * 1.56 :.0f} ")
            + "square meters of shade"
        )

    def show_info(self):
        """
        Display detailed information about the tree.
        """
        print(
            "\n"
            + self.name
            + " (Tree): "
            + str(self.height)
            + "cm, "
            + str(self.age)
            + " days, "
            + str(self.trunk_diameter)
            + "cm diameter"
        )


class Vegetable(Plant):
    """
    Represents a vegetable plant.

    Inherits from:
        Plant

    Attributes:
        harvest_season (str): Season during which the vegetable is harvested.
        nutritional_value (str): Main nutritional benefit of the vegetable.
    """

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Initialize a Vegetable instance.

        Args:
            name (str): Vegetable name.
            height (float): Height in centimeters.
            age (int): Age in days.
            harvest_season (str): Harvest season.
            nutritional_value (str): Nutritional benefit.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutritional(self):
        """
        Display the nutritional value of the vegetable.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")

    def show_info(self):
        """
        Display detailed information about the vegetable,
        including its nutritional value.
        """
        print(
            "\n"
            + self.name
            + " (Vegetable): "
            + str(self.height)
            + "cm, "
            + str(self.age)
            + " days, "
            + str(self.harvest_season)
            + " harvest"
        )
        self.show_nutritional()


print("=== Garden Plant Types ===")

Rose = Flower("Rose", 25, 30, "red")
vanilla = Flower("Vanilla", 200, 300, "white")

Rose.show_info()
Rose.bloom()
vanilla.show_info()
vanilla.bloom()

Oak = Tree("Oak", 500, 1825, 50)
olive = Tree("Olive", 600, 1000, 40)

Oak.show_info()
Oak.produce_shade()
olive.show_info()
olive.produce_shade()

Tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("Carrot", 30, 60, "autumn", "vitamine C")

Tomato.show_info()
carrot.show_info()
