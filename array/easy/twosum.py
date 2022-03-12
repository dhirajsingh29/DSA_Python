from typing import List


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order. [Leetcode - 1]
def two_sum(nums: List[int], target: int) -> List[int]:
    
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] in dict:
            return [dict[target - nums[i]], i]
        else:
            dict[nums[i]] = i
    
    return [-1, -1]


# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number [Leetcode - 167]
def two_sum_2(nums: List[int], target: int) -> List[int]:
    i = 0
    j = len(nums) - 1

    while (i < j):
        if nums[i] + nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j += 1

    return [-1, -1]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    # nums = [2, 7, 11, 15]
    # target = 10
    print(two_sum(nums, target))