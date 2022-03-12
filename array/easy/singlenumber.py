# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. [Leetcode - 136]

from typing import List


def single_number(nums: List[int]) -> int:
    sum = 0

    for num in nums:
        # XOR of two same numbers is 0
        sum = sum ^ num

    return sum


if __name__ == "__main__":
    nums = [1, 2, 2, 1, 4]
    print(single_number(nums))