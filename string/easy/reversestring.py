# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory. [Leetcode - 344]
from typing import List


def reverse_string(s: List[str]) -> None:
    i = 0
    j = len(s) - 1

    while (i < j):
        ch = s[i]
        s[i] = s[j]
        s[j] = ch

        i += 1
        j -= 1


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    print(s)