# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
#     Initially target array is empty.
#     From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
#     Repeat the previous step until there are no elements to read in nums and index.
# Return the target array. [Leetcode - 1389]
# Example 1
#   Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
#   Output: [0,4,1,3,2]
#   Explanation:
#       nums       index     target
#       0            0        [0]
#       1            1        [0,1]
#       2            2        [0,1,2]
#       3            2        [0,1,3,2]
#       4            1        [0,4,1,3,2]
from typing import List


def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
    target = [-1] * len(nums)

    for i in range(len(nums)):
        j = i

        while j != index[i]:
            target[j] = target[j - 1]
            j -= 1

        target[index[i]] = nums[i]

    return target


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4] 
    index = [0, 1, 2, 2, 1]

    # nums = [1, 2, 3, 4, 0] 
    # index = [0, 1, 2, 3, 0]

    # nums = [1]
    # index = [0]

    print(createTargetArray(nums, index))