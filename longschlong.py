# This is just a test file where I'll write some nonesense code

import math

# Create a circle class which characterizes a circle with radius r
class Circle():
    def __init__(self, radius):
        self._radius = radius
    
    def circle_area(self):
        return math.pi * (self._radius ** 2)

    def circle_perimeter(self):
        return math.pi * 2 * self._radius
    
    def GetRadius(self):
        return self._radius

def main():
    really_cool_circle = Circle(67)
    print(f"My really cool circle has an area of {really_cool_circle.circle_area()} and perimeter {really_cool_circle.circle_perimeter()}")

if __name__ == "__main__":
    main()

# long dong schlong