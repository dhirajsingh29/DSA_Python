# Remove Duplicates from Sorted Array [Leetcode - 26]

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    # index to track unique elements
    i = 0

    for j in range(1, len(nums)):

        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    
    return i


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 8, 8, 9]
    print(remove_duplicates(nums))