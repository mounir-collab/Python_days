class Plant:
    """
    Docstring for Plant
    its a blueprint for any plant
    """

    def __init__(self, name: str, height: float, age: int):
        """
        Docstring for __init__

        :param self: pointer to the object instance
        :param name: name attribut
        :param height: height attribut
        :param plant_age: plant_age attribut
        """

        self.name = name
        self.height = height
        self.plant_age = age

    def get_info(self):
        """
        Docstring for get_info
        this method show the informations of the plant
        :param self:  pointer to the object instance
        """
        return f"{self.name} ({self.height}cm , {self.plant_age} days)"


def main():

    plants = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    hei_l = [25, 200, 5, 80, 15]
    age_l = [30, 365, 90, 45, 120]

    plants_data = []
    for name, height, age in zip(plants, hei_l, age_l):  # By unpacking
        plants_data.append(Plant(name, height, age))

    total = 0
    for plant in plants_data:
        print(f"Created: {plant.get_info()}")
        total += 1
    print("\nTotal plants created: ", total)


if __name__ == "__main__":
    main()
