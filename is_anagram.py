from collections import Counter


def is_anagram(s1, s2):
    s1_count = Counter(s for s in s1.lower() if s.isalpha())
    s2_count = Counter(s for s in s2.lower() if s.isalpha())

    return s1_count == s2_count


if __name__ == "__main__":
    print(is_anagram("tea", "eat"))  # True
    print(is_anagram("tea", "treat"))  # False
    print(is_anagram("sinks", "skin"))  # False
    print(is_anagram("Listen", "silent"))  # True
    print(is_anagram("coins kept", "in pockets"))  # True
    print(is_anagram("a diet", "I'd eat"))  # True
    print(is_anagram("William Shakespeare", "I am a weakish speller"))  # True
