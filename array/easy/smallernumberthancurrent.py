# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array. [Leetcode - 1365]
# Example 1:
#   Input: nums = [8,1,2,2,3]
#   Output: [4,0,1,1,3]
#   Explanation: 
#       For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
#       For nums[1]=1 does not exist any smaller number than it.
#       For nums[2]=2 there exist one smaller number than it (1). 
#       For nums[3]=2 there exist one smaller number than it (1). 
#       For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
from typing import List


# Time complexity: O(n^2)
def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    result = [0] * len(nums)

    for i in range(len(nums)):
        count: int = 0

        for num in nums:
            if num < nums[i]:
                count += 1
        
        result[i] = count
    
    return result


# Time complexity: O(n)
def smallerNumbersThanCurrent_2(nums: List[int]) -> List[int]:
    sorted_nums = sorted(nums)
    order_dict = {}

    for i, num in enumerate(sorted_nums):
        if num not in order_dict:
            order_dict[num] = i
    
    result = []
    for num in nums:
        result.append(order_dict[num])
    
    return result


if __name__ == "__main__":
    nums = [8,1,2,2,3]
    # nums = [6,5,4,8]
    # nums = [7,7,7,7]
    print(smallerNumbersThanCurrent_2(nums))