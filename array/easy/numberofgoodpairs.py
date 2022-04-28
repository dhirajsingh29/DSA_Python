# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j. [Leetcode - 1512]
# Example 1:
#   Input: nums = [1,2,3,1,1,3]
#   Output: 4
#   Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:
#   Input: nums = [1,2,3]
#   Output: 0
from typing import List


# Time Complexity: O(n^2) 
def goodPairCount(nums: List[int]) -> int:
    count = 0

    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    
    return count


# Time Complexity: O(n)
def goodPairCount_2(nums: List[int]) -> int:
    frequencyDict = {}
    count = 0
    frequency = 0

    for num in nums:
        if num not in frequencyDict:
            frequencyDict[num] = 1
        else:
            frequency = frequencyDict[num]
            count += frequency
            frequencyDict[num] = frequency + 1
    
    return count


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 3]
    # nums = [1, 1, 1, 1]
    # nums = [1, 2, 3]
    print(goodPairCount_2(nums))