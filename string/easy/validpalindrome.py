# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise. [Leetcode - 125]
def IsPalindrome(s: str) -> bool:
    new_str = ""

    for ch in s:
        if ((ord(ch) >= ord('0') and ord(ch) <= ord('9')) or 
            (ord(ch) >= ord('A') and ord(ch) <= ord('Z')) or 
            (ord(ch) >= ord('a') and ord(ch) <= ord('z'))):
            new_str += ch

    i = 0
    j = len(new_str) - 1

    while i < j:
        if new_str[i] == new_str[j]:
            i += 1
            j -= 1
        else:
            return False
    
    return True


if __name__ == "__main__":
    s = "abcddcba"
    # s = "abcdcba"
    # s = "abcdecba"
    print(IsPalindrome(s))