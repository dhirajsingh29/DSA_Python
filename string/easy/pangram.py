# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
# [Leetcode - 1832]
def CheckIfPangram(s: str) -> bool:
    # initialize an array of length 26 with 0 
    charCount = [0]*26

    for ch in s:
        charCount[ord(ch) - ord('a')] += 1

    for count in charCount:
        if count == 0:
            return False
        
    return True


if __name__ == "__main__":
    s = 'thequickbrownfoxjumpsoverthelazydog'
    # s = 'leetcode'

    print(CheckIfPangram(s))