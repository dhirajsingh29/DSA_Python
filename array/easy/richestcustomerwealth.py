# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.
# [Leetcode - 1672]
# Example:
#   Input: accounts = [[1,5],[7,3],[3,5]]
#   Output: 10
#   Explanation: 
#       1st customer has wealth = 6
#       2nd customer has wealth = 10 
#       3rd customer has wealth = 8
#       The 2nd customer is the richest with a wealth of 10.
from typing import List


class CustomerWealth:
    def maxWealth(self, accounts: List[List[int]]) -> int:
        max = -1

        for account in accounts:
            sum = 0

            for amount in account:
                sum += amount
            
            max = sum if sum > max else max
        
        return max


if __name__ == "__main__":
    # accounts = [[1,2,3],[3,2,1]]
    # accounts = [[1,5],[7,3],[3,5]]
    accounts = [[2,8,7],[7,1,3],[1,9,5]]

    customerWealth = CustomerWealth()
    print(customerWealth.maxWealth(accounts))