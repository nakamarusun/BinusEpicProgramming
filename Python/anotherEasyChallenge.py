class Circle():

    __radius: float
    __color: str

    def __init__(self, radius = 1.0, color = "red"):
        self.__radius = radius
        self.__color = color

    def getRadius(self) -> float:
        return self.__radius

    def setRadius(self, radius: float):
        self.__radius = radius

    def getColor(self) -> str:
        return self.__color

    def setColor(self, color: str):
        self.__color = color

    def toString(self) -> str:
        return "The circle's radius is: " + str(self.__radius) + " painted with " + self.__color.upper()

    def getArea(self) -> float:
        return (3.1415 * self.__radius**2 )

class Cylinder(Circle):

    __height: float

    def __init__(self, radius = 1.0, color = "red", height = 1.0):
        super().__init__(radius, color)
        self.__height = height

    def getHeight(self) -> float:
        return self.__height

    def setHeight(self, height: float):
        self.__height = height

    def toString(self) -> str:
        return super().toString() + " and height: " + str(self.__height)

    def getVolume(self) -> float:
        return super().getArea() * self.__height

myCylinder = Cylinder(5, "black", 3)

print(myCylinder.toString())