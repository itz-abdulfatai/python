class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

class SubPoint(Point):
    def innter(self):
        print("inner")

point1 = Point(3,5)

print(point1.x)

