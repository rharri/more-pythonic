def parse_ranges(ranges_string: str):
    """Returns an iterable based on comma-seperated numeric ranges."""
    pairs = (group.split("-") for group in ranges_string.split(","))
    return (
        num_in_range
        for start, stop in pairs
        for num_in_range in range(int(start), int(stop) + 1)
    )


if __name__ == '__main__':
    ranges = parse_ranges("1-2,4-4,8-13")
    print(next(ranges))
    print(next(ranges))
    print(next(ranges))
    print(next(ranges))
    print(next(ranges))
    print(next(ranges))
    print(next(ranges))
    print(next(ranges))
    print(next(ranges))
    print(next(ranges))  # raises StopIteration
