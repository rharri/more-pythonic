class Foo:
    def __add__(self, other):
        print("Try my 'Foo.__add__' method first, unless 'Not Implemented'")
        return NotImplemented


class Bar:
    def __radd__(self, other):
        print("Try my 'Bar.__add__' method second, unless 'Not Implemented'")
        return None


class Junior:
    def __init__(self, name, experience_level):
        self.name = name
        self.experience_level = experience_level

    def __add__(self, other):
        if not isinstance(other, Senior):
            return NotImplemented
        return Partners(other, self)

    def __eq__(self, other):
        if not isinstance(other, Junior):
            # Why not return False? Some other type may implement their __eq__ method to be True when compared
            # to our class, this would obviously not be symmetric resulting in unexpected behaviour
            return NotImplemented
        return self.experience_level == other.experience_level

    def __repr__(self):
        return f"Junior('{self.name}')"


class Senior:
    def __init__(self, name, experience_level):
        self.name = name
        self.experience_level = experience_level

    def __add__(self, other):
        if not isinstance(other, Junior):
            return NotImplemented
        return Partners(self, other)

    def __eq__(self, other):
        if not isinstance(other, Senior):
            return NotImplemented
        return self.experience_level == other.experience_level

    def __repr__(self):
        return f"Senior('{self.name}')"


class Partners:
    def __init__(self, senior, junior):
        self.senior = senior
        self.junior = junior

    def __repr__(self):
        return repr(self.senior) + ", " + repr(self.junior)


if __name__ == "__main__":
    a = Junior("John", 3)
    b = Junior("Paul", 3)

    try:
        team_1 = a + b  # raises a TypeError instead of returning NotImplemented
        print(team_1)
    except TypeError:
        print(a.__add__(b))
        print(b.__add__(a))

    m = Senior("George", 15)

    team_2 = m + a
    print(team_2)

    team_3 = a + m
    print(team_3)

    print(a == m)  # False
    print(a.__eq__(m))  # NotImplemented
    print(a == b)  # True
    print(a.__eq__(b))  # True

    # Simple Example
    foo = Foo()
    bar = Bar()
    foo_bar = foo + bar

    # For __eq__
    # 1. a == b (Not Implemented)
    # 2. b == a (Not Implemented)
    # 3. False

    # For __add__, __sub__, __mul__, etc.
    # 1. a + b (Not Implemented)
    # 2. b + a (Not Implemented)
    # 3. raise TypeError
