'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        max_curr = max_global = nums[0]
        
        for i in nums[1:]:
            max_curr = max(i, max_curr+i)
            if max_curr > max_global: max_global = max_curr
        
        return max_global
            
