import math

class Shapes:
    def __init__(self, name):
        self.name = name

class Shapes2D(Shapes):
    def __init__(self, name):
        super().__init__(name)

class Square(Shapes2D):
    def __init__(self, name, side):
        Shapes2D.__init__(self,name)
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(Shapes2D):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Shapes3D(Shapes):
    def __init__(self, name):
        super().__init__(name)


class Cube(Shapes3D):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def volume(self):
        return self.side ** 3


class Cone(Shapes3D):
    def __init__(self, name, radius, height):
        super().__init__(name)
        self.radius = radius
        self.height = height

    def volume(self):
        return (1 / 3) * math.pi * self.radius ** 2 * self.height


def main():
    print("Choose a shape to create:")
    print("1. Square")
    print("2. Triangle")
    print("3. Cube")
    print("4. Cone")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        name = input("Enter the name of the square: ")
        side_length = float(input("Enter the side length of the square: "))
        square = Square(name, side_length)
        print(f"The area of the square '{square.name}' is: {square.area()}")

    elif choice == 2:
        name = input("Enter the name of the triangle: ")
        a = float(input("Enter side a of the triangle: "))
        b = float(input("Enter side b of the triangle: "))
        c = float(input("Enter side c of the triangle: "))
        triangle = Triangle(name, a, b, c)
        print(f"The area of the triangle '{triangle.name}' is: {triangle.area()}")

    elif choice == 3:
        name = input("Enter the name of the cube: ")
        side_length = float(input("Enter the side length of the cube: "))
        cube = Cube(name, side_length)
        print(f"The volume of the cube '{cube.name}' is: {cube.volume()}")

    elif choice == 4:
        name = input("Enter the name of the cone: ")
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))
        cone = Cone(name, radius, height)
        print(f"The volume of the cone '{cone.name}' is: {cone.volume()}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
