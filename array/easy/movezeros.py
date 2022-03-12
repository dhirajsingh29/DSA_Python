# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. 
# Note that you must do this in-place without making a copy of the array.
# [Leetcode - 283]

from typing import List


def move_zeros(nums: List[int]) -> None:
    
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != 0:
            i += 1
            continue

        if nums[i] == 0 and nums[j] != 0:
            # any number XORed with 0 returns the number
            nums[i] ^= nums[j]
            nums[j] = 0
            i += 1


if __name__ == "__main__":
    # nums = [0, 1, 0, 3, 12]
    nums = [0, 0, 1, 3, 12]
    move_zeros(nums)
    print(nums)