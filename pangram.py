"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    # convert cleaned up sentence into set (thus removing duplicates)
    # see if set is 26 char (e.g. contains at least 1 of each letter in alphabet)

    letters = set()

    for char in sentence:
        if char.isalpha():
            letters.add(char.lower())

    return len(letters) == 26


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
