class Plant:
    """
    Docstring for Plant
    """

    def __init__(self, name: str, height: float, age: int):
        """
        Docstring for __init__
        init is a constructor
        :param self: is a pointer to the instance object
        :param name: name of the plant
        :type name: str
        :param height: the height of the plant
        :type height: float
        :param age: the age of the plant
        :type age: int
        """
        self.name = name
        self.height = height
        self.plant_age = age


Rose = Plant("Rose", 25, 30)
Sunsflower = Plant("Sunflower", 80, 45)
Cactus = Plant("Cactus", 15, 120)

Plants = [Rose, Sunsflower, Cactus]

print("=== Garden Plant Registry ===")
for plant in Plants:
    print(f"{plant.name}: {plant.height}cm, {plant.plant_age} days old")
