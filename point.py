class Point:
    """Represents a three-dimensional point."""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Point(self.x * other, self.y * other, self.z * other)

    __rmul__ = __mul__

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __repr__(self):
        x, y, z = self
        return f"Point({x=}, {y=}, {z=})"


if __name__ == "__main__":
    p1 = Point(1, 2, 3)
    print(p1)

    p2 = Point(1, 2, 3)
    print(p1 == p2)

    p2.x = 4
    print(p1 == p2)

    print(p2)

    print("", end="\n")

    p3 = Point(1, 2, 3)
    p4 = Point(4, 5, 6)
    print(p3 + p4)
    print(p3 - p4)

    print(p3 * 2)
    print(2 * p3)

    x_pos, y_pos, z_pos = p1
    print(x_pos, y_pos, z_pos, sep="|")

    print(p1 == "hello")
