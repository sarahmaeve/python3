import re
import timeit

def strip_non_letters(phrase: str) -> str:
    """remove spaces, punctuation, numbers and return lowercase"""
    valid_letters = re.compile(r'[\W_]+', re.UNICODE)
    return valid_letters.sub('', phrase).lower()

def is_palindrome(candidate: str) -> bool:
    """starting from first letter and last letter, compare pairs of letters"""
    candidate = strip_non_letters(candidate)
    terminator = len(candidate) - 1
    for i in range(int(len(candidate) / 2) - 1):
        if candidate[i] != candidate[terminator - i]:
            return False
    return True

def is_palindrome_using_slices(candidate: str) -> bool:
    """Compare a string to its slice-reverse"""
    candidate = strip_non_letters(candidate)
    return candidate == candidate[::-1]

if __name__ == "__main__":
    TEST_ITERATIONS = 100000
    print("{}\nTime for {} iterations\n{}".format("-=" * 30, TEST_ITERATIONS, "-=" * 30))
    print("Palindrome using loop comparison: {} seconds".format(
        timeit.timeit(
            stmt="is_palindrome('Ed, I saw Harpo Marx ram Oprah W. aside.')",
            setup="from __main__ import is_palindrome", number=TEST_ITERATIONS)))
    print("Palindrome using slices: {} seconds".format(
        timeit.timeit(
            stmt="is_palindrome_using_slices('Ed, I saw Harpo Marx ram Oprah W. aside.')",
            setup="from __main__ import is_palindrome_using_slices", number=TEST_ITERATIONS)))
