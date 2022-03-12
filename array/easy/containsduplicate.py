# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct [Leetcode - 217]

from typing import List


def contains_duplicate_1(nums: List[int]) -> bool:
    
    arr = []
    for num in nums:
        if num in arr:
            return True
        else:
            arr.append(num)

    return False


def contains_duplicate_2(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(contains_duplicate_2(nums))