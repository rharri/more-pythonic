import re
import this
from collections import Counter

if __name__ == "__main__":
    zen_of_python = "".join([this.d.get(char, char) for char in this.s])

    occurrences = Counter(char for char in zen_of_python if char.isalpha())
    top_three = occurrences.most_common(3)

    print("", end="\n")
    print("*" * 32)
    print(f"{'ANALYSIS':>20}")
    print("*" * 32)
    print(f"1. Top three most frequent letters in the 'Zen of Python': {", ".join(char for char, _ in top_three)}")

    words = re.split(r"\W+", zen_of_python.lower())
    starts_with_c = Counter(word for word in words if word.startswith("c"))

    print(f"2. Words that start with 'c': {", ".join(word for word in set(starts_with_c.elements()))}")

    most_frequent_word = Counter(words)
    print(f"3. Top three most frequent words: {", ".join(word for word, _ in most_frequent_word.most_common(3))}")

    print("", end="\n")
