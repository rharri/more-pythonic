import pickle
import time

CACHE_FILE_NAME = "cache.pickle"


# noinspection PyUnusedLocal
def foobar(d):
    """Perform expensive computation with d."""
    time.sleep(10)
    return 42


if __name__ == "__main__":
    try:
        with open(CACHE_FILE_NAME, "rb") as cache_file:
            print(pickle.load(cache_file))
    except FileNotFoundError:
        result = foobar("some large data set")
        with open(CACHE_FILE_NAME, "wb") as cache_file:
            pickle.dump(result, cache_file)
