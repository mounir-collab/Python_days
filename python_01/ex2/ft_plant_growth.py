class Plant:
    """
    Docstring for Plant
    """

    def __init__(self, name: str, height: float, age: int):
        """
        Docstring for __init__

        :param self: pointer to the object instance
        :param name: name attribut
        :param height: height attribut
        :param age: age attribut
        """
        self.name = name
        self.height = height
        self.plant_age = age

    def grow(self):
        """
        Docstring for grow

        how plants grow
        """
        self.height += 1

    def age(self):
        """
        Docstring for age

        how age of plant is changed
        """
        self.plant_age += 1

    def daily_watering(self):
        """
        Docstring for daily_watering

        :param self: pointer to the object instance

        """
        self.grow()
        self.age()

    def get_info(self):
        """
        Docstring for get_info

        get informations of the plant
        """
        d = {"name": self.name, "height": self.height, "age": self.plant_age}
        return d


def main():
    Rose = Plant("Rose", 25, 30)
    d = Plant.get_info(Rose)
    print("=== Day 1 ===")
    print(f"{d['name']}: {d['height']} cm, {d['age']} days old")
    Growth = 0
    day = 7
    for i in range(1, day):
        Rose.daily_watering()
        Growth += 1
    d = Rose.get_info()
    print(f"=== Day {day} ===")
    print(f"{d['name']}: {d['height']} cm, {d['age']} days old")
    print(f"Growth this week: +{Growth}cm")


if __name__ == "__main__":
    main()
