class Polygon:

    def __init__(self, sides: int, length_of_sides: int, no_of_angles: int):
        self.sides = sides
        self.length_of_sides = length_of_sides
        self.no_of_angles = no_of_angles

    def display(self):
        print(f"Polygon with {self.sides} sides!")

class Triangle(Polygon):

    def __init__(self, side1: int, side2: int, side3: int, angle1: int, angle2: int, angle3: int):
        super().__init__(sides=3, length_of_sides=0, no_of_angles=3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def determine_triangle(self):
        if self.side1 == self.side2 == self.side3 and self.angle1 == self.angle2 == self.angle3:
            print("Equilateral Triangle")
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3 and self.angle1 == self.angle2 or self.angle2 == self.angle3 or self.angle1 == self.angle3:
            if self.angle1 == 90 or self.angle2 == 90 or self.angle3 == 90:
                print("Right Triangle")
            else:
                print("Isosceles Triangle")
        elif self.side1 != self.side2 or self.side2 != self.side3 or self.side1 == self.side3 and self.angle1 != self.angle2 or self.angle2 != self.angle3 or self.angle1 == self.angle3:
            if self.angle1 > 90 or self.angle2 > 90 or self.angle3 > 90:
                print("Obtuse Triangle")
            elif self.angle1 < 90 and self.angle2 < 90 and self.angle3 < 90:
                print("Acute Triangle")
            else:
                print("Scalene Triangle")
        else:
            print("Invalid input.")

class Quadrilateral(Polygon):

    def __init__(self, leg1: int, leg2: int, leg3: int, leg4:int):
        super().__init__(sides=4, length_of_sides=0, no_of_angles=4)
        self.leg1 = leg1
        self.leg2 = leg2
        self.leg3 = leg3
        self.leg4 = leg4

    def determine_quadrilateral(self):
        if self.leg1 == self.leg2 and self.leg3 == self.leg4:
            print("Square")
        elif self.leg1 == self.leg3 and self.leg2 == self.leg4:
            print("Rectangle")
        elif self.leg1 == self.leg3 and self.leg2 == self.leg4:
            if self.leg1 == self.leg2:
                print("Rhombus")
            elif self.leg1 != self.leg2:
                print("Parallelogram")
        elif self.leg1 == self.leg3 and self.leg2 != self.leg4:
            print("Trapezoid")
        elif self.leg1 != self.leg3 and self.leg2 == self.leg4:
            print("Isosceles Trapezoid")
        else:
            print("Kite")

class Pentagon(Polygon):

    def __init__(self, side1: int, side2: int, side3: int, side4: int, side5: int):
        super().__init__(sides=5, length_of_sides=0, no_of_angles=0)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.side5 = side5

    def determine_pentagon(self):
        if self.side1 == self.side2 == self.side3 == self.side4 == self.side5:
            print("Pentagon")
        else:
            print("Invalid input.")

class Hexagon(Polygon):

    def __init__(self, side1: int, side2: int, side3: int, side4: int, side5: int, side6: int):
        super().__init__(sides=6, length_of_sides=0, no_of_angles=0)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.side5 = side5
        self.side6 = side6

    def determine_hexagon(self):
        if self.side1 == self.side2 == self.side3 == self.side4 == self.side5 == self.side6:
            print("Hexagon")
        else:
            print("Invalid input.")


def get_polygon(sides: int, *args):
    if sides == 3 and len(args) == 6:
        return Triangle(*args)
    elif sides == 4 and len(args) == 4:
        return Quadrilateral(*args)
    elif sides == 5 and len(args) == 5:
        return Pentagon(*args)
    elif sides == 6 and len(args) == 6:
        return Hexagon(*args)
    else:
        print("Invalid input.")

# EXAMPLES

# Equilateral Triangle
eq_triangle = get_polygon(3, 5, 5, 5, 60, 60, 60)
eq_triangle.determine_triangle()

# Right Triangle
iso_right_triangle = get_polygon(3, 5, 5, 7, 45, 45, 90)
iso_right_triangle.determine_triangle()

# Isosceles Triangle
iso_triangle = get_polygon(3, 6, 6, 4, 70, 70, 40)
iso_triangle.determine_triangle()

# Obtuse Triangle
obtuse_triangle = get_polygon(3, 5, 6, 7, 40, 50, 90)
obtuse_triangle.determine_triangle()

# Acute Triangle
acute_triangle = get_polygon(3, 4, 5, 6, 60, 50, 70)
acute_triangle.determine_triangle()

# Scalene Triangle
scalene_triangle = get_polygon(3, 4, 5, 6, 80, 60, 40)
scalene_triangle.determine_triangle()


# Square
square = get_polygon(4, 5, 5, 5, 5)
square.determine_quadrilateral()

# Rectangle
rectangle = get_polygon(4, 6, 4, 6, 4)
rectangle.determine_quadrilateral()

# Rhombus
rhombus = get_polygon(4, 5, 5, 5, 5)
rhombus.determine_quadrilateral()

# Parallelogram
parallelogram = get_polygon(4, 6, 4, 6, 4)
parallelogram.determine_quadrilateral()

# Trapezoid
trapezoid = get_polygon(4, 5, 7, 5, 9)
trapezoid.determine_quadrilateral()

# Isosceles Trapezoid
iso_trapezoid = get_polygon(4, 5, 8, 5, 6)
iso_trapezoid.determine_quadrilateral()

# Kite
kite = get_polygon(4, 4, 6, 4, 6)
kite.determine_quadrilateral()


# Pentagon
pentagon = get_polygon(5, 5, 5, 5, 5, 5)
pentagon.determine_pentagon()

# Hexagon
hexagon = get_polygon(6, 6, 6, 6, 6, 6, 6)
hexagon.determine_hexagon()