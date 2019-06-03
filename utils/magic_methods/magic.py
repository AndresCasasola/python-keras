class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

p1 = Point(1, 3)
p2 = Point(1, 2)

print(p1)