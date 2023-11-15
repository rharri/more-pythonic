def required_and_optional(required_a, required_b, optional_a=None):
    print(required_a, required_b, optional_a)


def required_and_variadic(required_a, required_b, *args):
    print(required_a, required_b, args)


def required_and_keywords(required_a, required_b, **kwargs):
    print(required_a, required_b, kwargs)


if __name__ == "__main__":
    required_and_optional(1, 2)
    required_and_optional(1, 2, 3)
    required_and_optional(required_b=2, optional_a=3, required_a=1)

    required_and_variadic(1, 2, 3, 4, 5)

    required_and_keywords(1, 2, a=3, b=4, c=5)
