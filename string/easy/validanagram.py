# Given two strings s and t, return true if t is an anagram of s, and false otherwise. [Leetcode - 242]
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

def valid_anagram(s: str, t: str) -> bool:
    dict = {}

    if len(s) != len(t):
        return False

    # initialize an array of length 26 with 0 
    charCount = [0]*26

    # ord function returns the Unicode code from a given character
    for i in range(len(s)):
        charCount[ord(s[i]) - ord('a')] += 1
        charCount[ord(t[i]) - ord('a')] -= 1

    for count in charCount:
        if count != 0:
            return False

    return True


if __name__ == "__main__":
    s = 'anagram'
    t = 'nagaram'

    # s = 'rat'
    # t = 'car'
    print(valid_anagram(s, t))