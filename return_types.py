import math


class Number:
    """Represents a number."""

    def __init__(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError
        self.x = x

    def __add__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return Number(self.x + other.x)

    def __bool__(self):
        if not isinstance(self.x, (int, float)):
            return False
        return True

    def __repr__(self):
        return f"Number({self.x})"


class NegativeNumber(Number):
    def __repr__(self):
        return f"Negative({self.x})"


NEGATIVE_NUMBER = NegativeNumber(-math.inf)  # sentinel object, identity matters


def i_return_none(x):
    """Returns None since there is no explicit return."""
    _ = x


def i_return_sentinel_object(x: int | float) -> Number:
    """Returns a Number object if x > 0, otherwise returns a negative object."""
    return Number(x) if x > 0 else NEGATIVE_NUMBER


def i_return_sentinel_value(x: int | float) -> int | float:
    """Returns x if x > 0, otherwise -1."""
    return x if x > 0 else -1  # sentinel value, value matters


if __name__ == "__main__":
    print(i_return_none(5))

    r = i_return_sentinel_object(-5)

    if r is NEGATIVE_NUMBER:
        print(f"I'm negative")
    else:
        print(f"I'm positive {r.x}")

    print(i_return_sentinel_object(5))

    print(NEGATIVE_NUMBER)

    print(i_return_sentinel_value(5))
    print(i_return_sentinel_value(-5))
