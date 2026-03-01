class SecurePlant:
    """
    Docstring for SecurePlant
    Secure plant is a blueprint for a plant but encapsuled
    """

    def __init__(self, name: str):
        """
        Docstring for __init__
        constructur it self
        :param self: pointer to the object instance
        :param name: name of the plant
        :type name: str
        """
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")

    @property
    def get_height(self):
        """
        Docstring for get_height
        this is the getter i use it like a proprety
        :param self: pointer to the object instance
        """
        return self.__height

    @property
    def get_age(self):
        """
        Docstring for get_age
        this is the getter i use it like a proprety
        :param self: pointer to the object instance
        """
        return self.__age

    def set_height(self, value: float):
        """
        Docstring for set_height
        this is a setter
        :param self: pointer to the object instance
        :param value: the updated height
        :type value: float
        """
        if value < 0:
            print(
                "\nInvalid operation attempted: height " +
                str(value) +
                "cm [REJECTED]"
            )
            print("Security: Negative height rejected\n")
        else:
            self.__height = value
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, value: int):
        """
        Docstring for set_age
        this is a setter
        :param self: pointer to the object instance
        :param value: the updated age
        :type value: float
        """
        if value < 0:
            print(
                "\nInvalid operation attempted: age " +
                str(value) +
                "days [REJECTED]"
            )
            print("Security: Negative age rejected\n")
        else:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")


print("=== Garden Security System ===")
Rose = SecurePlant("Rose")
SecurePlant.set_height(Rose, 25)
Rose.set_age(30)
Rose.set_height(-5)
print(f"Current plant: {Rose.name} ({Rose.get_height}cm, {Rose.get_age} days)")
