# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1. [Leetcode - 387]
# Constraints:
#     1 <= s.length <= 105
#     s consists of only lowercase English letters.
def first_unique_character(s: str) -> int:
    count = [0] * 26

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    for i in range(len(s)):
        if count[ord(s[i]) - ord('a')] == 1:
            return i

    return -1


if __name__ == "__main__":
    s = "leetcode"
    # s = "aabb"
    # s = "loveleetcode"
    print(first_unique_character(s))