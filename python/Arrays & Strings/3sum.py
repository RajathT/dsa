"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        
        i, n, res = 0, len(nums), []
        
        while i < n-2:
            j, k = i+1, n-1
            
            while((i>0 and nums[i]!=nums[i-1]) or i==0) and j<k:
                val = nums[i] + nums[j] + nums[k]
                if j>i+1 and nums[j] == nums[j-1]:
                    j += 1
                elif k<n-1 and nums[k]==nums[k+1]:
                    k -= 1
                elif val == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                elif val < 0:
                    j += 1
                else:
                    k -= 1
            
            i += 1
        return res
                    
                
                
            
                
                                
