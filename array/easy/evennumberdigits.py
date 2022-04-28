# Given an array nums of integers, return how many of them contain an even number of digits. [Leetcode - 1295]
import math
from typing import List


def findNumbers(nums: List[int]) -> int:
    count = 0
    for num in nums:
        if evenNumberDigits(num):
            count += 1
    
    return count


def evenNumberDigits(num: int) -> bool:
    digitCount = numberOfDigitsBetter(num)

    return digitCount % 2 == 0


def numberOfDigits(num: int) -> int:
    if num < 0:
        num *= -1

    if num == 0:
        return 1

    count = 0
    while num > 0:
        count += 1
        num //= 10

    return count


def numberOfDigitsBetter(num: int) -> int:
    if num < 0:
        num *= -1

    return int(math.log10(num)) + 1


if __name__ == "__main__":
    nums = [12, 9, 465, 7893, 1, 45]
    # nums = [555,901,482,1771]
    print(findNumbers(nums))