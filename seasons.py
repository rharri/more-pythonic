import enum
import random
import sys


class Seasons(enum.Enum):
    SUMMER = enum.auto()
    FALL = enum.auto()
    WINTER = enum.auto()
    SPRING = enum.auto


def random_season():
    """
    Returns a random season.
    :return: A random season.
    """
    return random.choice(list(Seasons))


def main():
    for _ in range(5):
        print(random_season())
    return 0


if __name__ == "__main__":
    sys.exit(main())
