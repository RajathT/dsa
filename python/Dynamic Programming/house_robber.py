'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        memo = [-1 for _ in range(len(nums))]
        
        def helper(n):
            if n < 0:
                return 0
            elif memo[n] != -1:
                return memo[n]
            else:
                memo[n] = max(nums[n] + helper(n-2), helper(n-1))
            return memo[n]
        
        return helper(len(nums)-1)
