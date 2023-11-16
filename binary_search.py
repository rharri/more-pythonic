import bisect
import cProfile
import pstats
import random
import timeit


def linear_search(numbers, target):
    steps = 1
    for num in numbers:
        if num == target:
            return True, steps
        steps += 1
    return False, steps


def binary_search(numbers, target):
    size = len(numbers)
    start = 0
    end = size - 1
    middle = (start + end) // 2

    steps = 1
    while start <= end:
        if numbers[middle] == target:
            return True, steps

        if numbers[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
        middle = (start + end) // 2
        steps += 1
    return False, steps


def bisect_search(numbers, target):
    i = bisect.bisect(numbers, target)
    if i != len(numbers) and numbers[i] == target:
        return True
    return False


def hash_search(numbers, target):
    return target in numbers, 1


if __name__ == "__main__":
    print(linear_search([3, 12, 22, 56, 75, 98, 102], 98))
    print(linear_search([3, 12, 22, 56, 75, 98, 102], 198))
    print(binary_search([3, 12, 22, 56, 75, 98, 102], 98))
    print(binary_search([3, 12, 22, 56, 75, 98, 102], 198))
    print(hash_search({3, 12, 22, 56, 75, 98, 102}, 98))
    print(hash_search({3, 12, 22, 56, 75, 98, 102}, 198))

    random_numbers = [random.randint(1, 1_000_000) for _ in range(100_000)]
    random_numbers.sort()

    t = random.randint(1, 1_000_000)
    print(f"Looking for {t=} in a sorted list of {len(random_numbers)} random numbers")

    duration1 = timeit.timeit("linear_search(random_numbers, t)", number=1000, globals=globals())
    duration2 = timeit.timeit("binary_search(random_numbers, t)", number=1000, globals=globals())
    duration3 = timeit.timeit("bisect_search(random_numbers, t)", number=1000, globals=globals())
    duration4 = timeit.timeit("hash_search(rn, t)", "rn = set(random_numbers)", number=1000, globals=globals())
    duration5 = timeit.timeit("rn = set(random_numbers)", number=1000, globals=globals())

    print(f"Linear: {duration1:.7f} seconds")  # O(n)
    print(f"Binary: {duration2:.7f} seconds")  # O(log n)
    print(f"Bisect: {duration3:.7f} seconds")  # O(log n)
    print(f"Hash-Based: {duration4:.7f} seconds")  # O(n) + O(1)

    print("For 1M sorted numbers:")
    print(f"\tbinary_search requires {(duration1 - duration2 // duration1):.2%} less time than linear_search.")
    print(f"\tbisect_search requires {(duration2 - duration3 // duration2):.2%} less time than binary_search.")
    print(f"\thash_search requires {(duration3 - duration4 // duration3):.2%} less time than bisect_search.")
    print(f"\tnote: building the set takes {duration5:.7f} seconds\n")

    print("PROFILE:")
    profile = cProfile.Profile()
    profile.enable()
    linear_search(random_numbers, t)
    binary_search(random_numbers, t)
    bisect_search(random_numbers, t)
    hash_search(random_numbers, t)
    profile.disable()
    pstats.Stats(profile).strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats()
